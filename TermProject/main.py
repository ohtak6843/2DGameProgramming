from pico2d import *
from heart import *

WINDOW_WIDTH, WINDOW_HEIGHT = 1600, 900


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def create_world():
    global running
    global HP
    global balls
    global stick
    global table
    global hearts

    HP = 6

    running = True

    balls = load_image('Balls.png')
    stick = load_image('Stick.png')
    table = load_image('Table.jpg')

    hearts = Heart()


def update_world():
    hearts.update()


    


open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)
create_world()

while running:
    table.draw(800, 450, 1600, 1000)  # 2/5 사이즈
    balls.draw(400, 0, 150, 150)  # 1/10 사이즈
    stick.draw(500, 500, 240, 240)  # 1/5 사이즈
    hearts.draw(HP)
    update_canvas()
    handle_events()
    delay(0.1)
