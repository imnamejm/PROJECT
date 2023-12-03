from pico2d import *
import game_framework
import title_mode
import tip_mode

import game_world
from ball import Ball
from target import Target
from field import Field
from ring import Ring
from item import Item
from settings import Setting
from settings import Pause
from cloud import Cloud

field_x, field_y = 1200, 800
mouse_click = False

def handle_events():

    events = get_events()

    global x, y
    global score
    global mouse_click

    for event in events:

        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                mouse_click = True
                x, y = event.x, field_y - 1 - event.y
                ball.put_mouse(x, y)
        elif event.type == SDL_MOUSEBUTTONUP:
            if event.button == SDL_BUTTON_LEFT:
                mouse_click = False
                ball.save_mouse()
        elif event.type == SDL_MOUSEMOTION:
            if mouse_click:
                x, y = event.x, field_y - 1 - event.y
                ball.move_mouse(x, y)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_k:
            score += 10
        elif event.type == SDL_KEYDOWN and event.key == SDLK_y:
            game_framework.push_mode(tip_mode)



def init():
    global field
    global target
    global ball
    global ring
    global item
    global setting
    global pause
    global cloud
    global score

    running = True

    field = Field()
    game_world.add_object(field, 0)

    target = Target()
    game_world.add_object(target, 1)

    ring = Ring()
    game_world.add_object(ring, 2)

    ball = Ball()
    game_world.add_object(ball, 1)

    item = Item()
    game_world.add_object(item, 2)

    pause = Pause()
    game_world.add_object(pause, 2)

    setting = Setting()
    game_world.add_object(setting, 2)

    cloud = Cloud()
    game_world.add_object(cloud, 3)

    score = 0

def finish():
    game_world.clear()
    pass

def update():
    global score
    ball_state = ball.ball_statement()

    game_world.update()
    if ball_state == 2:
        if game_world.ring_ball_col(ball, ring):
            ball.stop()
            ring.stop()
            target.stop()

        if game_world.goal(ball, ring):
            score += 1
    target.score_load(score)
    ring.score_load(score)
    field.score_load(score)
    cloud.score_load(score)

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause1():
    pass

def resume():
    pass
