import pygame
import time
import random
from player import *
from donkey import *
from fireball import *
from board import *
from coin import *

clock = pygame.time.Clock()
pygame.init()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (255,0,255)
block_size = 20
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height+50))
pygame.display.set_caption('Donkey Kong')


#all_sprite_list = pygame.sprite.Group()
#ladder_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
coin_list = pygame.sprite.Group()
fireball_list = pygame.sprite.Group()
donkey_list = pygame.sprite.Group()


############################


    
player = Player(40,540,'Kid_goku3.png')
player_list.add(player)

#########################    

######################################

queen = pygame.image.load('queen.png')
#donkey = pygame.image.load('kong.png')
lifepng = pygame.image.load('life.png')
res_zone = fireballdeath(20,540)
donkey_kong = Donkey(20,100,'kong.png')
donkey_list.add(donkey_kong)
reload(coin_list)


#####
font = pygame.font.SysFont(None , 35)
def message_to_screen(msg,color,x,y):
    screen_text = font.render(msg,True,color)
    screen.blit(screen_text , [x,y])
win=5
curr_posx=20
curr_posy=100
flag=0
life=3
gravitywork = 0
v=130
previous = 0
p=False
pp=2
gameover = False


while not p:
#################player operation keys
    if life == 0:
        gameover = True
        pp=1
        p=True
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           p=True
       elif event.type == pygame.KEYDOWN:
           if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.movement(-5,0)
           elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.movement(5,0)
           elif event.key == pygame.K_SPACE:
                player.movement(0,-10)
           elif event.key == pygame.K_UP or event.key == pygame.K_w:
                if gravitywork != 1:
                    player.movement(0,-5)
           elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.movement(0,5)
           elif event.key == pygame.K_q:
                p=True
       elif event.type == pygame.KEYUP:
           if event.key == pygame.K_LEFT or event.key == pygame.K_a:
               player.movement(5,0)
           elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
               player.movement(-5,0)
           elif event.key == pygame.K_UP or event.key == pygame.K_w:
                if gravitywork != 1:
                    player.movement(0,5)
           elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.movement(0,-5)
           elif event.key == pygame.K_SPACE:
                player.movement(0,10)


##############fireball movement

    if v==130:
        if len(fireball_list)<12:
            eee = donkey_kong.fetch()
            fireball = Fireball(eee,100)
            fireball_list.add(fireball)
        v=0
    else:
        v +=1

    for ss in fireball_list:
        ss.update(all_sprite_list)
        ss.gravity(all_sprite_list,ladder_list)

#    fireball.update(all_sprite_list)
#    fireball.gravity(all_sprite_list,ladder_list)
        
    
################     
    win = player.rescued()
    if win == 4:
        player.getposition()
        coin_list = pygame.sprite.Group()
        previous = score
        reload(coin_list)
        win=5
        pp=10
    score = previous + 5*(16 - len(coin_list))-25*(3-life)
    screen.fill(black)
    player.checkwall(all_sprite_list)
    player.collectcoin(coin_list)
    donkey_kong.update()
    message_to_screen('Score : ',green,40,610)
    message_to_screen(str(score),green,140,610)
    message_to_screen('Life : ',green,400,610)
    number = life
    while number!=0:
        screen.blit(lifepng,(560-number*30,605))
        number -=1
    hurt = player.checkcollision(fireball_list)
    if hurt == 2:
        life -= 1
        player.getposition()
        hurt = 1
    res_zone.ballkill(fireball_list)
    gravitywork = player.ladder_check(ladder_list)
    if gravitywork == 1:
        player.gravity(all_sprite_list,ladder_list)
#    player.bugfix(ladder_list)
#    player.update(all_sprite_list)
#    player.ladder_check(ladder_list)
    all_sprite_list.draw(screen)
#    screen.blit(donkey,(curr_posx,curr_posy))
    screen.blit(queen,(220,20))
    ladder_list.draw(screen)
    player_list.draw(screen)
    coin_list.draw(screen)
    fireball_list.draw(screen)
    donkey_list.draw(screen)
    pygame.display.flip()
    clock.tick(30)
while pp==1 or pp==6:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pp=2
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pp=2
    screen.fill(black)
    if win==4:
        message_to_screen('You Win',green,350,250)
    else:
        message_to_screen('You Lose',green,350,250)
    message_to_screen('Score : ',green,350,300)
    message_to_screen(str(score),green,450,300)
    message_to_screen("Press 'q' to exit",green,350,360)
    pygame.display.flip()
        
pygame.quit()
quit()



