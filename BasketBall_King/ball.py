from pico2d import *
import game_world
import game_framework


class Ball:
    image = None
    def __init__(self, x = 600, y = 20, velocity = 1):
        if Ball.image is None:
            Ball.image = load_image('basicball.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.velocity * 100 * game_framework.frame_time

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30
