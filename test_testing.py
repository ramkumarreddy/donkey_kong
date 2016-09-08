from person import *
from player import * 
from board import *
from donkey import *
from coin import *
from fireball import *




player_list = pygame.sprite.Group()
coin_list = pygame.sprite.Group()
fireball_list = pygame.sprite.Group()
donkey_list = pygame.sprite.Group()


player = Player(40,540,'Kid_goku3.png')
donkey_kong = Donkey(20,100,'kong.png')
fireball = Fireball(20,40)
fireball_list.add(fireball)
reload(coin_list)

player.movement(5,0)
player.checkwall(all_sprite_list)
player.movement(-5,0)
assert player.fetch_position() == [45,540]

player.movement(0,5)
player.checkwall(all_sprite_list)
player.movement(0,-5)
assert player.fetch_position() == [45,540]

for i in range(200):
	donkey_kong.update()
	assert 20<=donkey_kong.fetch()<=452

a=set(all_sprite_list)
b=set(ladder_list)
c=set(coin_list)
d=set(fireball_list)

assert a.intersection(b) == set([])

assert c.intersection(a) == set([])
	
assert c.intersection(b) == set([])
for i in range(184):
	fireball.update(all_sprite_list)
	assert fireball.fetchposition() == [20+(i+1)*4,40]
	assert d.intersection(a) == set([])













