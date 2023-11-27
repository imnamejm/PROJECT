from pico2d import *
import game_framework
import game_world

class Item:
    def __init__(self):
        self.image = load_image('item.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(50, 750)