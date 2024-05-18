from pygame import *
from button import Button
from sprites import Sprite, Hero
from random import randint
import time as ptime
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

background = transform.scale(image.load("1_game_background.png"),(screen_width,screen_height))
clock = time.Clock()

btn1 = Button(window, screen_width, screen_height, stop_game)
font.init()

font1 = font.Font(None, 30)

coin = Sprite(x=randint(0,400), y=randint(0,400))
submarine = Hero()
stone1 = Sprite(x=randint(1000,1500), y=randint(0,400), img_name="Rock1_1.png")
stone2 = Sprite(x=randint(1000,1500), y=randint(0,400), img_name="Rock1_1.png")
stone3 = Sprite(x=randint(1000,1500), y=randint(0,400), img_name="Rock1_1.png")

offset_x = -500
counter = 0
water = [-screen_width, 0, screen_width]
game = True
while game:

    coin.rect.x -= 4
    stone1.rect.x -= 6
    stone2.rect.x -= 6
    stone3.rect.x -= 6

    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                pause = not pause
        if e.type == MOUSEBUTTONDOWN:
            btn1.click()
    

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
    
    
    collided = submarine.rect.colliderect(coin.rect)

    collide1 = submarine.rect.colliderect(stone1.rect)
    collide2 = submarine.rect.colliderect(stone2.rect)
    collide3 = submarine.rect.colliderect(stone3.rect)


    if collide1:
        window.blit(font1.render("YOU LOSE", True, (255,0,0)), (width / 2 - 150, height / 2 - 50))
        display.update()
        ptime.sleep(2)
        game = False
    if collide2:
        window.blit(font1.render("YOU LOSE", True, (255,0,0)), (width / 2 - 150, height / 2 - 50))
        display.update() 
        ptime.sleep(2)
        game = False

    if collide3:
        window.blit(font1.render("YOU LOSE", True, (255,0,0)), (width / 2 - 150, height / 2 - 50))
        display.update()
        ptime.sleep(2)
        game = False

    if counter == 15:
        window.blit(font1.render("YOU WIN", True, (0,255,0)), (width / 2 - 150, height / 2 - 50))
        display.update()
        ptime.sleep(2)
        game = False



    if collided:
        counter +=1
        coin.rect.x = 1000
        coin.rect.y = randint(1,350)

    
    if coin.rect.x <= 0:
        coin.rect.x = randint(500,1500)
        coin.rect.y = randint(5,250)

    if stone1.rect.x <= 0:
        stone1.rect.x = randint(1000,1500)
        stone1.rect.y = randint(5,250)

    if stone2.rect.x <= 0:
        stone2.rect.x = randint(1000,1500)
        stone2.rect.y = randint(5,250)

    if stone1.rect.x <= 0:
        stone2.rect.x = randint(1000,1500)
        stone3.rect.y = randint(5,250)
    
    
    
    window.blit(font1.render(f"К-сть монет: {counter}", True,(255,255,255)), (15,10))
    stone1.reset(window)
    stone2.reset(window)
    stone3.reset(window)

    coin.reset(window)
    submarine.reset(window)
    submarine.move()
    display.update()
    clock.tick(60)
        


