import pygame
from person import *

pygame.init()
black = (0,0,0)
green = (255,0,255)
block_size = 20
screen_width = 800
screen_height = 600


class Player(Person):
    chanx = 0
    chany = 0
#    Person.__init__(self)
#        pygame.sprite.Sprite.__init__(self)
#       self.image = pygame.image.load('Kid_goku3.png')
#       self.image.set_colorkey(black)
#       self.rect = self.image.get_rect()
#       self.rect.x = x
#        self.rect.y = y
    def movement(self,x,y):
        self.chanx += x
        self.chany += y
    def checkwall(self,walls):
        self.rect.x += self.chanx
        block_hit_list = pygame.sprite.spritecollide(self , walls, False)
        for block in block_hit_list:
            if self.chanx>0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        self.rect.y += self.chany
        block_hit_list = pygame.sprite.spritecollide(self , walls, False)
        for block in block_hit_list:
            if self.chany>0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
    def collectcoin(self,coins):
        coin_hit_list = pygame.sprite.spritecollide(self , coins , True)
    def gravity(self,walls,ladders):
        self.rect.y += 1
        block_hit_list = pygame.sprite.spritecollide(self , walls, False)
        ladders_hit_list = pygame.sprite.spritecollide(self , ladders, False)
        if len(block_hit_list)==0:
            if len(ladders_hit_list)==0:
                self.movement(0,1)
            else:
                self.chany = 0
        else:
            self.chany = 0
#        if len(ladders_hit_list) != 0:
#            self.chany=0
        self.rect.y = self.rect.y - 1
#    def bugfix(self,ladders):
#       ladder_hit_list = pygame.sprite.spritecollide(self , ladders, False)
#       if len(ladder_hit_list)!=0:
#           self.chany = 0


        
    def ladder_check(self,ladders):
        self.rect.y += 3 
        ladder_hit_list = pygame.sprite.spritecollide(self , ladders , False)
        self.rect.y -=3
        if len(ladder_hit_list)==0:
            return 1;
        if len(ladder_hit_list)!=0:
            return 2;
    def checkcollision(self,fireballs):
        fireball_hit_list = pygame.sprite.spritecollide(self , fireballs, True)
        if len(fireball_hit_list)!=0:
            return 2;
        else:
            return 1;
    def getposition(self):
        self.rect.x = 20
        self.rect.y = 540
    def rescued(self):
        if self.rect.y <= 20 and (self.rect.x>200 and self.rect.x<320):
            return 4;
    def fetch_position(self):
	l=[self.rect.x,self.rect.y]
	return l
