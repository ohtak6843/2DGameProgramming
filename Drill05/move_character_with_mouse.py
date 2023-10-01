from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def character_move():
    global character_x, character_y
    global x, y
    global frame

    x1, y1 = character_x, character_y
    x2, y2 = x, y

    for i in range(0, 1000 + 1, 10):
        t = i / 1000
        character_x = (1 - t) * x1 + t * x
        character_y = (1 - t) * y1 + t * y
        draw_scene()
        delay(0.01)

    x = random.randint(0, TUK_WIDTH)
    y = random.randint(0, TUK_HEIGHT)

def draw_scene():
    global frame
    global x, y
    global character_x, character_y

    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, character_x, character_y)
    hand.draw(x, y)
    update_canvas()
    frame = (frame + 1) % 8

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

character_x = TUK_WIDTH // 2
character_y = TUK_HEIGHT // 2

while running:
    character_move()

    handle_events()

close_canvas()




