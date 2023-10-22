from pico2d import *


open_canvas(1280, 1024)


balls = load_image('Balls.png')
stick = load_image('Stick.png')
heart = load_image('Heart.png')


while (True):
    balls.draw(400, 0, 150, 150)  # 1/10 사이즈
    stick.draw(500, 500, 240, 240)  # 1/5 사이즈
    heart.draw(800, 200, 66, 60)  # 1/10 사이즈
    update_canvas()
    delay(0.1)
