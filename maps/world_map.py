import pygame
from maps.level_node import LevelNode

class WorldMap:

    def __init__(self, screen):

        self.screen = screen
        self.background = pygame.image.load(
            "assets/images/mapa/mapa.png"
        ).convert()

        self.background = pygame.transform.scale(
            self.background,
            self.screen.get_size()
        )
        self.font = pygame.font.Font(None, 28)

        self.levels = [

            LevelNode(1, 80, 500),
            LevelNode(2, 180, 460),
            LevelNode(3, 300, 420),
            LevelNode(4, 430, 390),
            LevelNode(5, 560, 340),

            LevelNode(6, 700, 300),
            LevelNode(7, 650, 220),
            LevelNode(8, 540, 170),
            LevelNode(9, 420, 150),
            LevelNode(10, 300, 180),

            LevelNode(11, 180, 220),
            LevelNode(12, 100, 300),
            LevelNode(13, 180, 370),
            LevelNode(14, 320, 320),
            LevelNode(15, 450, 280),

            LevelNode(16, 600, 420),
            LevelNode(17, 500, 520),
            LevelNode(18, 350, 540),
            LevelNode(19, 200, 520),
            LevelNode(20, 700, 520),
        ]

    def draw(self):

        self.screen.blit(self.background, (0, 0))

        # liga os níveis
        for i in range(len(self.levels) - 1):
            pygame.draw.line(
                self.screen,
                (180, 180, 180),
                self.levels[i].pos,
                self.levels[i + 1].pos,
                4
            )

        # desenha os níveis
        for level in self.levels:
            level.draw(self.screen, self.font)

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            for level in self.levels:

                if level.unlocked and level.is_clicked(event.pos):
                    return level.number

    def complete_level(self, number):

        self.levels[number - 1].completed = True

        if number < len(self.levels):
            self.levels[number].unlocked = True