import pygame

class Map1:

    def __init__(self, screen):

        self.screen = screen

        self.maps = []

        for i in range(1, 6):
            image = pygame.image.load(
                f"assets/images/mapa/map1/{i}.png"
            ).convert_alpha()

            image = pygame.transform.scale(
                image,
                self.screen.get_size()
            )

            self.maps.append(image)

        self.current_map = 0

        # Controle do scroll da camada 2 (índice 1)
        self.scroll_speed_2 = 0.5
        self.scroll_x_2 = 0
        self.scroll_width_2 = self.maps[1].get_width()

        # Controle do scroll da camada 5 (índice 4)
        self.scroll_speed_5 = 1
        self.scroll_x_5 = 0
        self.scroll_width_5 = self.maps[4].get_width()

    def update(self):
        self.scroll_x_2 -= self.scroll_speed_2
        if self.scroll_x_2 <= -self.scroll_width_2:
            self.scroll_x_2 = 0

        self.scroll_x_5 -= self.scroll_speed_5
        if self.scroll_x_5 <= -self.scroll_width_5:
            self.scroll_x_5 = 0

    def draw(self):
        for index, image in enumerate(self.maps):
            if index == 1:
                self.screen.blit(image, (self.scroll_x_2, 0))
                self.screen.blit(image, (self.scroll_x_2 + self.scroll_width_2, 0))
            elif index == 4:
                self.screen.blit(image, (self.scroll_x_5, 0))
                self.screen.blit(image, (self.scroll_x_5 + self.scroll_width_5, 0))
            else:
                self.screen.blit(image, (0, 0))