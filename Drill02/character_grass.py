import pico2d
import math

from pico2d import *
from math import *

open_canvas()

# fill here

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
degree = -90

while(True):
    while(x < 780):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.001)

    while(y < 550):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x , y)
        y = y + 2
        delay(0.001)

    while(x > 20):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 2
        delay(0.001)

    while(y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y - 2
        delay(0.001)

    while(x < 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.001)

    while(degree < 270):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = 400 + 210 * cos(degree / 360 * 2 * pi)
        y = 300 + 210 * sin(degree / 360 * 2 * pi)
        degree = degree + 2
        delay(0.01)

    degree = -90


close_canvas()
