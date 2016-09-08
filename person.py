import pygame

pygame.init()
black = (0,0,0)
green = (255,0,255)
block_size = 20
screen_width = 800
screen_height = 600

class Person(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
