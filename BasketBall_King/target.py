from pico2d import *
import game_world
import game_framework

class Target:
    def __init__(self):
        self.image = load_image('target.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 400)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 200, self.y - 200, self.x + 200, self.y + 200