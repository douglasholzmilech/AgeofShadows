from entities.sprite_Sheet import spriteSheet
from entities.animation import animation

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.pos = [100, 450]
        self.speed = 4

        self.animations = {
            "idle": animation(spriteSheet("assets/images/player/idle.png", 4).get_frames(), speed=10),
            "walk": animation(spriteSheet("assets/images/player/walk.png", 6).get_frames(), speed=6),
            "run": animation(spriteSheet("assets/images/player/run.png", 8).get_frames(), speed=5),
            "jump": animation(spriteSheet("assets/images/player/jump.png", 4).get_frames(), speed=8, loop=False),
            "defend": animation(spriteSheet("assets/images/player/defend.png", 3).get_frames(), speed=8),
            "hurt": animation(spriteSheet("assets/images/player/hurt.png", 3).get_frames(), speed=6, loop=False),
            "dead": animation(spriteSheet("assets/images/player/dead.png", 5).get_frames(), speed=8, loop=False),
            "attack": animation(spriteSheet("assets/images/player/Attack1.png", 5).get_frames(), speed=5, loop=False),
            "attack2": animation(spriteSheet("assets/images/player/Attack2.png", 5).get_frames(), speed=5, loop=False),
            "attack3": animation(spriteSheet("assets/images/player/Attack3.png", 5).get_frames(), speed=5, loop=False),
            "run_attack": animation(spriteSheet("assets/images/player/runAttack.png", 5).get_frames(), speed=5, loop=False),
        }

        self.state = "idle"

    def set_state(self, new_state):
        if new_state != self.state:
            self.state = new_state
            self.animations[self.state].reset()

    def move(self, dx, dy):
        self.pos[0] += dx
        self.pos[1] += dy

    def update(self):
        self.animations[self.state].update()

        # Ações que tocam uma vez e voltam pro idle
        one_shot_states = ["attack", "attack2", "attack3", "run_attack", "hurt", "jump"]
        if self.state in one_shot_states and self.animations[self.state].finished:
            self.set_state("idle")

        # Morte não volta pro idle
        if self.state == "dead" and self.animations["dead"].finished:
            pass  # fica parado no último frame

    def draw(self):
        frame = self.animations[self.state].get_current_frame()
        self.screen.blit(frame, self.pos)