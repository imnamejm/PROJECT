from pico2d import *
import game_world
import game_framework

class Target:
    def __init__(self, x = 600, y = 600, pattern = 1, velocity = 1):
        self.image = load_image('target.png')
        self.x, self.y, self.pattern, self.velocity = x, y, pattern, velocity


    def update(self):
        if self.pattern == 1:
            if self.x > 750:
                self.velocity = -1
            elif self.x < 450:
                self.velocity = 1
            self.x += self.velocity * 50 * game_framework.frame_time


    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 200, self.y - 150, self.x + 200, self.y + 150

