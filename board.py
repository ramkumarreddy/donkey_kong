import pygame
from person import *

pygame.init()
black = (0,0,0)
green = (255,0,255)
block_size = 20
screen_width = 800
screen_height = 600



all_sprite_list = pygame.sprite.Group()
ladder_list = pygame.sprite.Group()

class board(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
    def fetchwall(self):
	return self.rect.x
    

class ladderprint(Person):
    akjsd = 0



wall = board(0,0,block_size,screen_height)
all_sprite_list.add(wall)
wall = board(block_size,0,screen_width-block_size,block_size)
all_sprite_list.add(wall)
wall = board(block_size,screen_height-block_size,screen_width-block_size,block_size)
all_sprite_list.add(wall)
wall = board(screen_width-block_size,block_size,block_size,screen_height-2*block_size)
all_sprite_list.add(wall)

###
wall = board(10*block_size,3*block_size,3*block_size,block_size)
all_sprite_list.add(wall)
w=3
while w < 7:
    ladder = ladderprint(13*block_size,w*block_size,'ladder4.png')
    ladder_list.add(ladder)
    w +=1
wall = board(14*block_size,3*block_size,2*block_size,block_size)
all_sprite_list.add(wall)
####
wall = board(block_size,7*block_size,25*block_size,block_size)
all_sprite_list.add(wall)
wall = board(27*block_size,7*block_size,4*block_size,block_size)
all_sprite_list.add(wall)
w=0
while w < 4:
    ladder = ladderprint(26*block_size,(w+7)*block_size,'ladder4.png')
    ladder_list.add(ladder)
    w +=1
###
wall = board(11*block_size,11*block_size,28*block_size,block_size)
all_sprite_list.add(wall)
wall = board(8*block_size,11*block_size,2*block_size,block_size)
all_sprite_list.add(wall)
w=0
while w < 4:
    ladder = ladderprint(10*block_size,(w+11)*block_size,'ladder4.png')
    ladder_list.add(ladder)
    w +=1

####
wall = board(block_size,15*block_size,20*block_size,block_size)
all_sprite_list.add(wall)
wall = board(22*block_size,15*block_size,8*block_size,block_size)
all_sprite_list.add(wall)
w=0
while w < 4:
    ladder = ladderprint(21*block_size,(w+15)*block_size,'ladder4.png')
    ladder_list.add(ladder)
    w +=1
#####
wall = board(8*block_size,19*block_size,7*block_size,block_size)
all_sprite_list.add(wall)
wall = board(16*block_size,19*block_size,12*block_size,block_size)
all_sprite_list.add(wall)
wall = board(29*block_size,19*block_size,10*block_size,block_size)
all_sprite_list.add(wall)
w=0
while w < 4:
    ladder = ladderprint(28*block_size,(w+19)*block_size,'ladder4.png')
    ladder_list.add(ladder)
    w +=3
w=0
while w < 4:
    ladder = ladderprint(15*block_size,(w+19)*block_size,'ladder4.png')
    ladder_list.add(ladder)
    w +=1
#########   
wall = board(block_size,23*block_size,22*block_size,block_size)
all_sprite_list.add(wall)
wall = board(24*block_size,23*block_size,7*block_size,block_size)
all_sprite_list.add(wall)
w=0
while w < 6:
    ladder = ladderprint(23*block_size,(w+23)*block_size,'ladder4.png')
    ladder_list.add(ladder)
    w +=1
###
wall = board(34*block_size,25*block_size,6*block_size,block_size)
all_sprite_list.add(wall)

