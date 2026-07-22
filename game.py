import pygame
from ui.menu import Menu
from maps.world import World
from maps.world_map import WorldMap
from maps.map1 import Map1
from entities.player import Player

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Age of Shadow")
        self.running = True
        self.state = "menu"
        self.clock = pygame.time.Clock()
        self.menu = Menu(self.screen)
        self.world = WorldMap(self.screen)
        self.map1 = Map1(self.screen)
        self.player = Player(self.screen)

    def run(self):
        while self.running:
            if self.state == "menu":
                result = self.menu.run()
                if result == "play":
                    self.state = "game"
                elif result == "score":
                    self.show_score()
                elif result == "controls":
                    self.show_controls()
                elif result == "store":
                    self.show_store()
                elif result == "exit":
                    self.running = False

            elif self.state == "game":
                self.game_loop()
            elif self.state == "map1":

                self.map1_loop()
            self.clock.tick(60)

    def game_loop(self):
        while self.state == "game" and self.running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        self.state = "menu"
                        return

                selected_level = self.world.handle_event(event)

                if selected_level == 1:
                    self.state = "map1"
                    return
            self.world.update()
            self.world.draw()
            pygame.display.update()
            self.clock.tick(60)

    def map1_loop(self):

        # Estados que travam o personagem até terminarem
        busy_states = [
            "attack", "attack2", "attack3", "run_attack",
            "hurt", "dead", "jump"
        ]

        # Limite de altura que o personagem pode subir no mapa
        # (ajuste esse valor conforme o "chão"/topo da sua arte)
        TOP_LIMIT_Y = 400

        screen_width, screen_height = self.screen.get_size()

        while self.state == "map1" and self.running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        self.state = "game"
                        return

                    if self.player.state not in busy_states:
                        if event.key == pygame.K_SPACE:
                            self.player.set_state("jump")
                        elif event.key == pygame.K_1:
                            keys = pygame.key.get_pressed()
                            if keys[pygame.K_0]:
                                self.player.set_state("run_attack")
                            else:
                                self.player.set_state("attack")
                        elif event.key == pygame.K_2:
                            self.player.set_state("attack2")
                        elif event.key == pygame.K_3:
                            self.player.set_state("attack3")

            keys = pygame.key.get_pressed()

            if self.player.state not in busy_states:

                running_key = keys[pygame.K_0]
                defending = keys[pygame.K_4]
                moving_up = keys[pygame.K_w]
                moving_down = keys[pygame.K_s]
                moving_left = keys[pygame.K_a]
                moving_right = keys[pygame.K_d]

                speed = self.player.speed * 2 if running_key else self.player.speed

                if defending:
                    self.player.set_state("defend")

                elif moving_left or moving_right or moving_up or moving_down:

                    if moving_left:
                        self.player.move(-speed, 0)
                    if moving_right:
                        self.player.move(speed, 0)
                    if moving_up:
                        self.player.move(0, -speed)
                    if moving_down:
                        self.player.move(0, speed)

                    self.player.set_state("run" if running_key else "walk")

                else:
                    self.player.set_state("idle")

                # --- Limites de tela ---
                frame = self.player.animations[self.player.state].get_current_frame()
                frame_width, frame_height = frame.get_size()

                # Esquerda / Direita: não passa da borda da tela
                if self.player.pos[0] < 0:
                    self.player.pos[0] = 0
                elif self.player.pos[0] > screen_width - frame_width:
                    self.player.pos[0] = screen_width - frame_width

                # Cima: limitado por TOP_LIMIT_Y
                if self.player.pos[1] < TOP_LIMIT_Y:
                    self.player.pos[1] = TOP_LIMIT_Y

                # Baixo: não passa da borda da tela
                elif self.player.pos[1] > screen_height - frame_height:
                    self.player.pos[1] = screen_height - frame_height

            self.map1.update()
            self.map1.draw()

            self.player.update()
            self.player.draw()

            pygame.display.update()
            self.clock.tick(60)

    def show_score(self):
        print("Tela de Score")

    def show_controls(self):
        print("Tela de Controles")

    def show_store(self):
        print("Tela da loja")