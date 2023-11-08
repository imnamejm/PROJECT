from pico2d import *

class Target:
    def __init__(self):
        self.image = load_image('농구 골대.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 400)