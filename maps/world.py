import pygame

class World:
    def __init__(self, screen):
        self.screen = screen

        # Carrega o mapa (por enquanto apenas uma imagem)
        self.background = pygame.image.load(
            "assets/images/mapa/mapa.png"
        ).convert()

        self.background = pygame.transform.scale(
            self.background,
            self.screen.get_size()
        )

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.background, (0, 0))