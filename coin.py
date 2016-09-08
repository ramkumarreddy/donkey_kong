import pygame
import random

pygame.init()
black = (0,0,0)
green = (255,0,255)
block_size = 20
screen_width = 800
screen_height = 600

class coin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('rsz_coin.png')
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def reload(coin_list):
	q=0
	aa=block_size
	bb=180
	cc=180
	dd=560
	ee=24
	while q<4:
	    randx = random.randrange(aa,bb)
	    randy = random.randrange(ee*block_size,dd)
	    coins = coin(randx,randy)
	    coin_list.add(coins)
	    aa +=cc
	    bb +=cc
	    if q==2:
		aa += 40
		ee=23
		dd=24*20
	    q += 1
	q=0
	aa=block_size
	bb=240
	cc=240
	while q<3:
	    randx = random.randrange(aa,bb)
	    randy = random.randrange(20*block_size,22*block_size)
	    coins = coin(randx,randy)
	    coin_list.add(coins)
	    aa +=cc
	    bb +=cc
	    q += 1
	q=0
	aa=block_size
	bb=240
	cc=240
	while q<3:
	    randx = random.randrange(aa,bb)
	    randy = random.randrange(16*block_size,18*block_size)
	    coins = coin(randx,randy)
	    coin_list.add(coins)
	    aa +=cc
	    bb +=cc
	    q += 1
	q=0
	aa=block_size
	bb=240
	cc=240
	while q<3:
	    randx = random.randrange(aa,bb)
	    randy = random.randrange(12*block_size,14*block_size)
	    coins = coin(randx,randy)
	    coin_list.add(coins)
	    aa +=cc
	    bb +=cc
	    q += 1
	q=0
	aa=block_size
	bb=240
	cc=240
	while q<3:
	    randx = random.randrange(aa,bb)
	    randy = random.randrange(8*block_size,10*block_size)
	    coins = coin(randx,randy)
	    coin_list.add(coins)
	    aa +=cc
	    bb +=cc
	    q += 1
