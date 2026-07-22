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

            LevelNode(1, 120, 450),
            LevelNode(2, 250, 430),
            LevelNode(3, 450, 450),
            LevelNode(4, 400, 380),
            LevelNode(5, 335, 330),

            LevelNode(6, 228, 320),
            LevelNode(7, 100, 220),
            LevelNode(8, 300, 140),
            LevelNode(9, 360, 180),
            LevelNode(10, 500, 220),

            LevelNode(11, 440, 270),
            LevelNode(12, 500, 330),
            LevelNode(13, 520, 390),
            LevelNode(14, 650, 330),
            LevelNode(15, 720, 230),

            LevelNode(16, 620, 110),
            LevelNode(17, 500, 120),
            LevelNode(18, 610, 180),
            LevelNode(19, 560, 260),
            LevelNode(20, 600, 300),
        ]

    def update(self):
        pass

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