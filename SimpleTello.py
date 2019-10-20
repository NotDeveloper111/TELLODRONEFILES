import tellopy as tp
import pygame as py
tl = tp.Tello()

tp.Tello.connect(tl)
speed = 50
RotateSpeed = 90
Move_ySpeed = 50
Go = [False, False, False, False]
py.init()
screen = py.display.set_mode((300, 30))
py.display.set_caption("Tello")

run = True

while run:
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
            py.quit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_w:
                tp.Tello.forward(tl, speed)
            elif event.key == py.K_d:
                tp.Tello.right(tl, speed)
            elif event.key == py.K_s:
                tp.Tello.backward(tl, speed)
            elif event.key == py.K_a:
                tp.Tello.left(tl, speed)
            elif event.key == py.K_q:
                tp.Tello.takeoff(tl)
            elif event.key == py.K_e:
                tp.Tello.land(tl)
            elif event.key == py.K_RIGHT:
                tp.Tello.clockwise(tl, RotateSpeed)
            elif event.key == py.K_RIGHT:
                tp.Tello.counter_clockwise(tl, RotateSpeed)
            elif event.key == py.K_r:
                tp.Tello.up(tl,Move_ySpeed)
            elif event.key == py.K_f:
                tp.Tello.down(tl,Move_ySpeed)
        if event.type == py.KEYUP:
            if event.key == py.K_w:
                tp.Tello.forward(tl, 0)
            elif event.key == py.K_s:
                tp.Tello.right(tl, 0)
            elif event.key == py.K_a:
                tp.Tello.backward(tl, 0)
            elif event.key == py.K_d:
                tp.Tello.left(tl, 0)
            elif event.key == py.K_RIGHT:
                tp.Tello.clockwise(tl, 0)
            elif event.key == py.K_RIGHT:
                tp.Tello.counter_clockwise(tl, 0)
            elif event.key == py.K_r:
                tp.Tello.up(tl, 0)
            elif event.key == py.K_f:
                tp.Tello.down(tl, 0)
