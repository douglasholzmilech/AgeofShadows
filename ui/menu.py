import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 32)
        self.title_font = pygame.font.Font(None, 80)
        self.background = pygame.image.load(
            "assets/images/menu/menu.png"
        ).convert()

        self.background = pygame.transform.scale(
            self.background,
            self.screen.get_size()
        )
        button_width = 140
        button_height = 35
        x = (self.screen.get_width() - button_width) // 8
        y = 220
        self.buttons = {
            "PLAY": pygame.Rect(x, y, button_width, button_height),
            "SCORE": pygame.Rect(x, y + 42, button_width, button_height),
            "CONTROLS": pygame.Rect(x, y + 84, button_width, button_height),
            "STORE": pygame.Rect(x, y + 126, button_width, button_height),
            "EXIT": pygame.Rect(x, y + 168, button_width, button_height)
        }

    def run(self):
        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return "quit"


                if event.type == pygame.MOUSEBUTTONDOWN:

                    for name, rect in self.buttons.items():

                        if rect.collidepoint(event.pos):

                            return name.lower()


            self.draw()


    def draw(self):

        # Fundo
        self.screen.blit(self.background, (0, 0))


        # Título
        title = self.title_font.render(
            "Age of Shadow",
            True,
            (139, 0, 0)
        )

        self.screen.blit(
            title,
            (230, 80)
        )


        # Botões
        for name, rect in self.buttons.items():

            pygame.draw.rect(
                self.screen,
                (40, 40, 40),
                rect
            )

            pygame.draw.rect(
                self.screen,
                (139, 0, 0),
                rect,
                2
            )


            text = self.font.render(
                name,
                True,
                (255, 255, 255)
            )

            text_rect = text.get_rect(
                center=rect.center
            )

            self.screen.blit(
                text,
                text_rect
            )


        pygame.display.update()