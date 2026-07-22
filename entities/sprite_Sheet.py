import pygame

class spriteSheet:
    def __init__(self, path, frame_count):
        self.sheet = pygame.image.load(path).convert_alpha()
        self.frame_count = frame_count
        self.frame_width = self.sheet.get_width() // frame_count
        self.frame_height = self.sheet.get_height()

    def get_frames(self):
        frames = []
        for i in range(self.frame_count):
            rect = pygame.Rect(
                i * self.frame_width,
                0,
                self.frame_width,
                self.frame_height
            )
            frames.append(self.sheet.subsurface(rect))
        return frames