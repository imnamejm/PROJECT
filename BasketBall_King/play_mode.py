from pico2d import *
import game_framework

import game_world
from ball import Ball
from target import Target
from field import Field

field_x, field_y = 1200, 800
mouse_click = False

def handle_events():

    events = get_events()

    global x, y
    global mouse_click

    for event in events:

        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                mouse_click = True
        elif event.type == SDL_MOUSEBUTTONUP:
            if event.button == SDL_BUTTON_LEFT:
                mouse_click = False
        elif event.type == SDL_MOUSEMOTION:
            if mouse_click:
                x, y = event.x, field_y - 1 - event.y
                ball.put_mouse(x, y)
            elif not mouse_click:
                x, y = event.x, field_y - 1 - event.y
                if y > 400:
                    x, y = event.x, field_y - 1 - event.y
                    ball.save_mouse(x, y)






def init():
    global field
    global target
    global ball

    running = True

    field = Field()
    game_world.add_object(field, 0)

    target = Target()
    game_world.add_object(target, 1)

    ball = Ball()
    game_world.add_object(ball, 1)

def finish():
    game_world.clear()
    pass

def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass
