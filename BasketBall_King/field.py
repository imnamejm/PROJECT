from pico2d import *

class Field:
    def __init(self):
        self.image = load_image('field.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(0, 0)