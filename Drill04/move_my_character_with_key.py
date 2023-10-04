from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('Animation_Sheet.png')


def handle_events():
    global running, dirX, dirY
    global frame, frame_add
    global left_dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirX += 1
                frame_add += 1
                left_dir = False
            elif event.key == SDLK_LEFT:
                dirX -= 1
                frame_add += 1
                left_dir = True
            elif event.key == SDLK_UP:
                dirY += 1
                frame_add += 1
            elif event.key == SDLK_DOWN:
                dirY -= 1
                frame_add += 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX -= 1
                frame_add -= 1
            elif event.key == SDLK_LEFT:
                dirX += 1
                frame_add -= 1
            elif event.key == SDLK_UP:
                dirY -= 1
                frame_add -= 1
            elif event.key == SDLK_DOWN:
                dirY += 1
                frame_add -= 1

def draw_idle_animation(x, y):
    global frame, frame_add
    global left_dir

    idle_animation_frame_max = 10

    idle_animation_left_point = [0, 28, 57, 86, 115, 144, 173, 202, 231, 260]
    idle_animation_right_point =[26, 55, 84, 113, 142, 171, 200, 229, 258, 287]

    frame += 1
    if frame >= idle_animation_frame_max: frame = 0

    if left_dir == False:
        character.clip_draw(idle_animation_left_point[frame], 878 - 29, idle_animation_right_point[frame] - idle_animation_left_point[frame], 29,
                            x, y, (idle_animation_right_point[frame] - idle_animation_left_point[frame]) * 7, 29 * 7)
    elif left_dir == True:
        character.clip_composite_draw(idle_animation_left_point[frame], 878 - 29, idle_animation_right_point[frame] - idle_animation_left_point[frame], 29,
                            0, 'h', x, y, (idle_animation_right_point[frame] - idle_animation_left_point[frame]) * 7, 29 * 7)

def draw_LR_move(x, y):
    global frame, frame_add
    global left_dir

    LR_move_frame_max = 12

    LR_left_point = [0, 25, 51, 77, 103, 130, 158, 186, 219, 251, 281, 308]
    LR_right_point = [23, 49, 75, 101, 128, 156, 184, 217, 249, 279, 306, 331]

    frame += frame_add
    if frame >= LR_move_frame_max: frame = 0

    if left_dir == False:
        character.clip_draw(LR_left_point[frame], 878 - 175, LR_right_point[frame] - LR_left_point[frame], 25,
                            x, y, (LR_right_point[frame] - LR_left_point[frame]) * 7, 25 * 7)
    elif left_dir == True:
        character.clip_composite_draw(LR_left_point[frame], 878 - 175, LR_right_point[frame] - LR_left_point[frame], 25,
                                      0, 'h', x, y, (LR_right_point[frame] - LR_left_point[frame]) * 7, 25 * 7)

def draw_up_move(x, y):
    global frame, frame_add
    global left_dir

    up_move_frame_max = 6

    up_move_left_point = [0, 31, 63, 96, 129, 161]
    up_move_right_point =[29, 61, 94, 127, 159, 192]

    frame += frame_add
    if frame >= up_move_frame_max: frame = 0

    if left_dir == False:
        character.clip_draw(up_move_left_point[frame], 878 - 277, up_move_right_point[frame] - up_move_left_point[frame], 31,
                            x, y, (up_move_right_point[frame] - up_move_left_point[frame]) * 7, 31 * 7)
    elif left_dir == True:
        character.clip_composite_draw(up_move_left_point[frame], 878 - 277, up_move_right_point[frame] - up_move_left_point[frame], 31,
                            0, 'h', x, y, (up_move_right_point[frame] - up_move_left_point[frame]) * 7, 31 * 7)

def draw_down_move(x, y):
    global frame, frame_add
    global left_dir

    down_move_frame_max = 10

    down_move_left_point = [0, 22, 48, 72, 95, 120, 145, 169, 193, 217]
    down_move_right_point =[20, 46, 70, 93, 118, 143, 167, 191, 215, 239]

    frame += frame_add
    if frame >= down_move_frame_max: frame = 0

    if left_dir == False:
        character.clip_draw(down_move_left_point[frame], 878 - 416, down_move_right_point[frame] - down_move_left_point[frame], 29,
                            x, y, (down_move_right_point[frame] - down_move_left_point[frame]) * 7, 29 * 7)
    elif left_dir == True:
        character.clip_composite_draw(down_move_left_point[frame], 878 - 416, down_move_right_point[frame] - down_move_left_point[frame], 29,
                                      0, 'h', x, y, (down_move_right_point[frame] - down_move_left_point[frame]) * 7, 29 * 7)

def draw_scene(x, y):
    global frame, frame_add
    global left_dir

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if dirX == 0 and dirY == 0:
        draw_idle_animation(x, y)
    elif dirY == 0:
        draw_LR_move(x, y)
    elif dirY > 0:
        draw_up_move(x, y)
    elif dirY < 0:
        draw_down_move(x, y)

running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame = 0
frame_add = 0

dirX = 0
dirY = 0

left_dir = False

while running:
    clear_canvas()

    draw_scene(x, y)

    update_canvas()
    handle_events()

    x += dirX * 20
    y += dirY * 20

    if x < 100: x = 100
    elif x + 100 > TUK_WIDTH: x = TUK_WIDTH - 100

    if y < 100: y = 100
    elif y + 100 > TUK_HEIGHT: y = TUK_HEIGHT - 100

    delay(0.1)


close_canvas()