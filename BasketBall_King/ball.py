from pico2d import *
import game_world
import game_framework


class Ball:
    image = None
    def __init__(self, x = 600, y = 100, velocity = 1):
        if Ball.image is None:
            Ball.image = load_image('basicball.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50
