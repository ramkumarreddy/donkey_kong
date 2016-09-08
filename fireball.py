import pygame

pygame.init()
black = (0,0,0)
green = (255,0,255)
block_size = 20
screen_width = 800
screen_height = 600

class Fireball(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.flag=0
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('rsz_fireball3(1).png')
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self,walls):
        self.rect.x += 5
        collide_list = pygame.sprite.spritecollide(self,walls,False)
        if len(collide_list)!=0:
            self.flag=1
        self.rect.x -= 10
        collide_list = pygame.sprite.spritecollide(self,walls,False)
        if len(collide_list)!=0:
            self.flag=0
        self.rect.x +=5
        if(self.flag==0):
            self.rect.x +=4
        else:
            self.rect.x -=4
    def gravity(self,walls,ladders):
        self.rect.y += 1
        block_hit_list = pygame.sprite.spritecollide(self , walls, False)
        ladders_hit_list = pygame.sprite.spritecollide(self , ladders, False)
        if len(block_hit_list)==0:
            if len(ladders_hit_list)==0:
                self.rect.y += 5
  #              self.movement(0,1)
            else:
                self.chany = 0
        else:
            self.chany = 0
#        if len(ladders_hit_list) != 0:
#            self.chany=0
        self.rect.y = self.rect.y - 1
    def fetchposition(self):
	return [self.rect.x,self.rect.y]

class fireballdeath(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40,40])
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
    def ballkill(self,fireballs):
        hit_list = pygame.sprite.spritecollide(self,fireballs,True)
