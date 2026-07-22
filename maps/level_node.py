import pygame

class LevelNode:

    def __init__(self, number, x, y):
        self.number = number
        self.radius = 10
        self.x = x
        self.y = y
        self.pos = (x, y)

        # apenas o primeiro nível começa desbloqueado
        self.unlocked = (number == 1)

        self.completed = False

    def draw(self, screen, font):

        if self.completed:
            color = (0, 255, 0)

        elif self.unlocked:
            color = (255, 0, 0)

        else:
            color = (60, 60, 60)

        pygame.draw.circle(
            screen,
            color,
            self.pos,
            self.radius,
            3  # espessura da borda
        )

        text = font.render(str(self.number), True, (0,0,0))
        rect = text.get_rect(center=self.pos)
        screen.blit(text, rect)

    def clicked(self, mouse_pos):
        x, y = self.pos
        mx, my = mouse_pos

        return (mx-x)**2 + (my-y)**2 <= self.radius**2