import math

from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def render_all(x, y):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
    

def run_circle():
    print("CIRCLE")

    cx, cy, r = 400, 300, 200
    for degree in range(-90, 270, 5):
        x = cx + r * math.cos(math.radians(degree))
        y = cy + r * math.sin(math.radians(degree))
        render_all(x, y)

def run_rectangle():
    print("RECTANGLE")

    # Bottom Line
    for x in range(400, 750 + 1, 10):
        render_all(x, 90)

    # Right Line
    for y in range(90, 550 + 1, 10):
        render_all(750, y)

    # Top Line
    for x in range(750, 50 - 1, -10):
        render_all(x, 550)

    # Left Line
    for y in range(550, 90 - 1, -10):
        render_all(50, y)

    # Bottom Line
    for x in range(50, 450 + 1, 10):
        render_all(x, 90)

while True:
    run_rectangle()
    run_circle()

close_canvas()
