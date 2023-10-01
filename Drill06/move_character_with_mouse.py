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

    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, character_x, character_y)
    hand.draw(x, y)
    for (temp_x, temp_y) in hand_list:
        hand.draw(temp_x, temp_y)
    update_canvas()
    frame = (frame + 1) % 8

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

character_x, character_y = TUK_WIDTH // 2, TUK_HEIGHT // 2

hand_list = []

while running:
    draw_scene()

    handle_events()

close_canvas()




