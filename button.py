from pygame import *

class Button:
    def __init__(self, window, screen_width, screen_height):
        self.window = window
        self.width = 100
        self.height = 50
        self.x = screen_width/2
        self.y = screen_height/2


        font.init()
        font1 = font.Font(None, 20)
   
    def reset(self):
        draw.rect(window, (255,255,255), rect.Rect(self.x, self.y, self_width, self_height))  
        self.window.blit(self.font1.render("Exit", True,(0,0,0)),(100,100))

        mouse = mouse.get_pos()
    def click(self):
        mouse1 = mouse.get_pos()
        if mouse[0] >= self.x and mouse1[0]<= self.x + self_width and mouse1[1]
            print(mouse1)


