from pygame import *
from button import Button
width = 700
height = 700
init()

info = display.Info
screen_width,screen_height = info.current_w,info.current_h

display.set_mode((screen_width,screen_height))

game = True
pause = False

background = transform.scale(image.load("8847584.jpg"),(screen_width,screen_height))
clock = time.Clock()

bnt1 = Button(window)

while game:

    window.blit(background, (0,0))
    for e in event.get()
    if e.type == QUIT:
        game = False
    if e.type == KEYDOWN:
        if e.key == K_ESCAPE:
            pause = not pause
        if e.type == MOUSEBUTTONDOWN:
            btn1.click()

    if pause:
        display.update()
        clock.tick(60)
        window.blit(background, (0,0))
        btn1.reset()
        btn1.click()

        continue

    window.blit(background, (0,0))


