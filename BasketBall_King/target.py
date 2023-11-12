from pico2d import *

class Target:
    def __init__(self, x = 600, y = 600, velocity = 1):
        self.image = load_image('target.png')
        self.x, self.y, self.velocity = x, y, velocity


    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 200, self.y - 150, self.x + 200, self.y + 150

