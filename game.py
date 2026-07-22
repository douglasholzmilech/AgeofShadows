import pygame
from ui.menu import Menu
from maps.world import World
from maps.world_map import WorldMap

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Age of Shadow")
        self.running = True
        self.state = "menu"
        self.clock = pygame.time.Clock()
        self.menu = Menu(self.screen)
        self.world = WorldMap(self.screen)

    def run(self):
        while self.running:
            if self.state == "menu":
                result = self.menu.run()
                if result == "play":
                    self.state = "game"
                elif result == "score":
                    self.show_score()
                elif result == "load":
                    self.load_game()
                elif result == "controls":
                    self.show_controls()
                elif result == "store":
                    self.show_store()
                elif result == "exit":
                    self.running = False

            elif self.state == "game":
                self.game_loop()
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
            self.world.update()
            self.world.draw()
            pygame.display.update()
            self.clock.tick(60)

    def show_score(self):
        print("Tela de Score")

    def load_game(self):
        print("Tela de Load")

    def show_controls(self):
        print("Tela de Controles")

    def show_store(self):
        print("Tela da loja")