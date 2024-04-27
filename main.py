from pygame import *
from button import Button
from sprites import Sprite, Hero
from random import randint
width = 700
height = 700
init()

info = display.Info()
screen_width,screen_height = info.current_w,info.current_h

window = display.set_mode((screen_width-200,screen_height-200))

game = True
pause = False

background = transform.scale(image.load("background.jpg"),(screen_width,screen_height))
clock = time.Clock()

btn1 = Button(window, screen_width, screen_height)

coin = Sprite(x=randint(0,screen_width), y=randint(0, screen_height))
submarine = Hero()

offset_x = -500

while game:

    window.blit(background, (0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                pause = not pause
        if e.type == MOUSEBUTTONDOWN:
            btn1.click()



    if pause:
        display.update()
        clock.tick(120)
        
        btn1.reset()
        btn1.click()
        continue

    
    offset_x += 5


    window.blit(background, (offset_x,0))
    coin.reset(window)
    submarine.reset(window)
    submarine.move()
    display.update()
    clock.tick(60)
        


