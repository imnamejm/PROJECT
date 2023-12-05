from pico2d import *
import game_framework
import title_mode
import tip_mode
import random

import game_world
from ball import Ball
from target import Target
from field import Field
from ring import Ring
from item import Item
from bird import Bird
from cloud import Cloud
from RETRY import Retry

field_x, field_y = 1200, 800
mouse_click = False

def init():
    global field
    global target
    global ball
    global ring
    global item
    global bird
    global cloud
    global score
    global retry
    global item_use
    global item_time

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

    bird = [Bird() for _ in range(2)]
    game_world.add_objects(bird, 3)

    cloud = [Cloud() for _ in range(3)]
    game_world.add_objects(cloud, 3)

    retry = Retry()
    game_world.add_object(retry, 3)

    score = 0
    item_use = False
    item_time = 5


def handle_events():
    events = get_events()

    global x, y
    global score
    global mouse_click
    global item_use
    global item_time

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

        elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
            retry.not_drawing()
            ball.init()
            target.init()
            ring.init()
            field.init()
            item.init()
            for i in range(3):
                cloud[i].init()
            for i in range(2):
                bird[i].init()
            score = 0
            item_time = 5
            item_use = False

        elif event.type == SDL_KEYDOWN and event.key == SDLK_t:
            target.stop()
            ring.stop()
            item.use_item()
            item_use = True

def finish():
    game_world.clear()
    pass

def update():
    global score
    global item_time
    ball_state = ball.ball_statement()
    ring.get_ball(ball_state)

    game_world.update()

    # 충돌체크
    if ball_state == 2:
        if game_world.ring_ball_col(ball, ring):
            ball.stop()
            ring.stop()
            target.stop()
            retry.do_drawing()

        if game_world.goal(ball, ring):
            score += 1
            ball.bgm.play(1)
            if item_use and item_time > 0:
                score += 1
                item_time -= 1

    if ball_state == 2 or ball_state == 1:
        if 30 <= score < 60:
            if game_world.collide(ball, bird[0]):
                ball.stop()
                ring.stop()
                target.stop()
                bird[0].stop()
                retry.do_drawing()

            if game_world.collide(ball, bird[1]):
                ball.stop()
                ring.stop()
                target.stop()
                bird[1].stop()
                retry.do_drawing()

    target.score_load(score)
    ring.score_load(score)
    field.score_load(score)
    for i in range(3):
        cloud[i].score_load(score)
    for i in range(2):
        bird[i].score_load(score)



def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause1():
    pass

def resume():
    pass
