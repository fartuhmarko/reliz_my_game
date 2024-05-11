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
def stop_game():
    global game
    game = False

background = transform.scale(image.load("background.jpg"),(screen_width,screen_height))
clock = time.Clock()

btn1 = Button(window, screen_width, screen_height, stop_game)

font = font.Font(None, 30)

coin = Sprite(x=randint(0,400), y=randint(0,400))
submarine = Hero()

offset_x = -500
counter = 0
water = [-screen_width, 0, screen_width]
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                pause = not pause
        if e.type == MOUSEBUTTONDOWN:
            btn1.click()

    window.blit(font.render(f"К-сть монет: {counter}", True,(255,255,255)), (15,10))

    

    for i in range(0,2):
        water[i] += 5
        window.blit(background, ( water[i],0))

        if  water[i]> screen_width:
             water[i] = -screen_width

    

    if pause:
        for e in event.get():
            print(e)
            btn1.click()

        if e.type == QUIT:
            game= False

        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                pause = not pause
            

        display.update()
        clock.tick(120)
        
        btn1.reset()
        btn1.click()
        continue
    
    collide = submarine.rect.colliderect(coin.rect)

    if collide:
        counter +=1
    
    

    coin.reset(window)
    submarine.reset(window)
    submarine.move()
    display.update()
    clock.tick(60)
        


