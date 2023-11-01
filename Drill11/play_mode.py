from pico2d import *
import game_framework

import game_world
from grass import Grass
from bird import Bird

# bird = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            bird.handle_event(event)
            pass

def init():
    global grass
    global bird, bird2, bird3, bird4, bird5, bird6, bird7, bird8, bird9, bird10

    running = True

    grass = Grass()
    game_world.add_object(grass, 0)

    bird = Bird()
    game_world.add_object(bird, 1)

    bird2 = Bird()
    game_world.add_object(bird2, 1)

    bird3 = Bird()
    game_world.add_object(bird3, 1)

    bird4 = Bird()
    game_world.add_object(bird4, 1)

    bird5 = Bird()
    game_world.add_object(bird5, 1)

    bird6 = Bird()
    game_world.add_object(bird6, 1)

    bird7 = Bird()
    game_world.add_object(bird7, 1)

    bird8 = Bird()
    game_world.add_object(bird8, 1)

    bird9 = Bird()
    game_world.add_object(bird9, 1)

    bird10 = Bird()
    game_world.add_object(bird10, 1)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    # delay(0.1)


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

