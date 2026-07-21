import pygame
from ui.menu import Menu

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Age of Shadow")

        self.running = True
        self.state = "menu"

        self.clock = pygame.time.Clock()

        # Cria o menu apenas uma vez
        self.menu = Menu(self.screen)


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


                elif result == "credits":
                    self.show_credits()


                elif result == "exit":
                    self.running = False



            elif self.state == "game":

                self.game_loop()


            self.clock.tick(60)



    def game_loop(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False


        self.screen.fill((50, 50, 50))


        # Aqui entra seu jogo:
        # player.update()
        # enemy.update()
        # colisões...


        pygame.display.update()



    # =========================
    # Telas temporárias do menu
    # =========================

    def show_score(self):
        print("Tela de Score")


    def load_game(self):
        print("Tela de Load")


    def show_controls(self):
        print("Tela de Controles")


    def show_credits(self):
        print("Tela de Créditos")