from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')


def handle_events():
    global running
    global x, y
    global hand_list

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.button == SDL_BUTTON_LEFT and event.type == SDL_MOUSEBUTTONDOWN:
            hand_list.append((x, y))
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def draw_scene():
    global frame
    global x, y
    global hand_list
    global character_x, character_y

    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, character_x, character_y)
    hand.draw(x, y)
    if len(hand_list) > 0:
        for temp_x, temp_y in hand_list:
            hand.draw(temp_x, temp_y)
    update_canvas()
    frame = (frame + 1) % 8

def character_move():
    global frame
    global x, y
    global hand_list
    global character_x, character_y
    global first_x, first_y
    global i

    x1, y1 = first_x, first_y
    x2, y2 = hand_list[0]

    t = i / 1000

    character_x = (1 - t) * x1 + t * x2
    character_y = (1 - t) * y1 + t * y2

    i = i + 10

    if i > 1000:
        del hand_list[0]
        i = 1
        first_x, first_y = character_x, character_y

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

character_x, character_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
first_x, first_y = TUK_WIDTH // 2, TUK_HEIGHT // 2

hand_list = []

i = 1

while running:
    draw_scene()
    if len(hand_list) > 0:
        character_move()

    delay(0.01)

    handle_events()

close_canvas()




