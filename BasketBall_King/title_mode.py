from pico2d import  load_image, SDL_KEYDOWN, get_events, SDL_QUIT, SDLK_ESCAPE, clear_canvas, update_canvas, SDLK_SPACE
import game_framework
import play_mode
import tip_mode

def init():
    global image
    image = load_image('title.png')

def update():
    pass

def finish():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_mode(play_mode)


def draw():
    clear_canvas()
    image.draw(600, 400)
    update_canvas()

def pause1():
    pass

def resume():
    pass