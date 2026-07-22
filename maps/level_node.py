import pygame

class LevelNode:

    def __init__(self, number, x, y):
        self.number = number
        self.radius = 20
        self.x = x
        self.y = y
        self.pos = (x, y)

        # apenas o primeiro nível começa desbloqueado
        self.unlocked = (number == 1)

        self.completed = False

    def draw(self, screen, font):

        if self.completed:
            color = (0, 180, 0)

        elif self.unlocked:
            color = (200, 200, 50)

        else:
            color = (80, 80, 80)

        pygame.draw.circle(screen, color, self.pos, self.radius)

        text = font.render(str(self.number), True, (0,0,0))
        rect = text.get_rect(center=self.pos)
        screen.blit(text, rect)

    def clicked(self, mouse_pos):
        x, y = self.pos
        mx, my = mouse_pos

        return (mx-x)**2 + (my-y)**2 <= self.radius**2