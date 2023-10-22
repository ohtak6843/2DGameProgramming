from pico2d import *

WINDOW_WIDTH, WINDOW_HEIGHT = 1600, 900
open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)


balls = load_image('Balls.png')
stick = load_image('Stick.png')
heart = load_image('Heart.png')
table = load_image('Table.jpg')


while (True):
    table.draw(800, 450, 1600, 1000)
    balls.draw(400, 0, 150, 150)  # 1/10 사이즈
    stick.draw(500, 500, 240, 240)  # 1/5 사이즈
    heart.draw(800, 200, 66, 60)  # 1/10 사이즈
    update_canvas()
    # handle_events()
    delay(0.1)
