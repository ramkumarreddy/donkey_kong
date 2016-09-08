import pygame
from person import *

pygame.init()
black = (0,0,0)
green = (255,0,255)
block_size = 20
screen_width = 800
screen_height = 600

class Donkey(Person):
    flag=0
#    super(Donkey,self).__init__()
#    Person.__init__(self)
#        self.image = pygame.image.load('kong.png')
#       self.image.set_colorkey(black)
#       self.rect = self.image.get_rect()
#       self.rect.x = x 
#       self.rect.y = y 
    def update(self):
        if self.flag == 0:
            self.rect.x += 2
        if self.flag == 1:
            self.rect.x -= 2
        if self.rect.x > 450:
            self.flag =1
        if self.rect.x < 40:
            self.flag =0
    def fetch(self):
        return self.rect.x
