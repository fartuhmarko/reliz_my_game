import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, img_name="coin.png", x=200, y=200, width=75, height=75, speed=0):
        super().__init__()
        self.image = pygame.image.load(img_name)
        self.image = pygame.transform.scale(self.image, (width,height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Hero(Sprite):
    def __init__(self):
        super().__init__("submarine.png", 200,200,75,75,10)
        self.money = 0
        self.health = 100
        self.armor = 100
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y <620:
            self.rect.y += self.speed
    
        
        




