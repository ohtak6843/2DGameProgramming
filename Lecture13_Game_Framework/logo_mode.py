from pico2d import *
import game_framework
import title_mode


def init():
    global image
    global logo_start_time

    image = load_image('tuk_credit.png')
    logo_start_time = get_time()
    pass


def finish():
    pass


def update():
    if get_time() - logo_start_time >= 2.0:
        game_framework.change_mode(title_mode)
    pass


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    pass


def handle_events():
    events = get_events()
    pass