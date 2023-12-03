from pico2d import load_image, get_time, clear_canvas, update_canvas
import game_framework
import play_mode

def init():
    global image
    global running
    global tip_start_time

    image = load_image('tip.png')
    running = True
    tip_start_time = get_time()

def update():
    global tip_start_time

    if get_time() - tip_start_time >= 3.0:
        game_framework.pop_mode(play_mode)

def finish():
    global image
    del image

def handle_events():
    pass

def draw():
    clear_canvas()
    image.draw(600, 400)
    update_canvas()

def pause1():
    pass

def resume():
    pass