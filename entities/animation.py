class animation:
    def __init__(self, frames, speed=6, loop=True):
        self.frames = frames
        self.speed = speed
        self.loop = loop
        self.current_frame = 0
        self.timer = 0
        self.finished = False

    def update(self):
        if self.finished:
            return
        self.timer += 1
        if self.timer >= self.speed:
            self.timer = 0
            self.current_frame += 1
            if self.current_frame >= len(self.frames):
                if self.loop:
                    self.current_frame = 0
                else:
                    self.current_frame = len(self.frames) - 1
                    self.finished = True

    def reset(self):
        self.current_frame = 0
        self.timer = 0
        self.finished = False

    def get_current_frame(self):
        return self.frames[self.current_frame]