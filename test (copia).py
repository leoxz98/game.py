import pygame
import sys
from pygame.locals import*
from random import*
import os

pygame.init()
fuente = pygame.font.Font(None, 20)	
screen = pygame.display.set_mode((800,600))
sprite_link = pygame.image.load(os.path.join("imagen", "listSpritex2v2.png"))
color3 = pygame.Color(255,255,255)
velocidadx = 0
velocidady = 0
posx = 0
posy = 100
sprite_section = (0, 0, 31, 33)
move = "down"
movement = False
s = 0
attack = False
a = 0

while True:


	superficie = pygame.Surface((100,100))
	superficie.blit(sprite_link, (0,0), sprite_section)
	ubicacionx = str(posx)
	ubicaciony = str(posy)
	mensaje = fuente.render(ubicacionx,1,color3)
	mensaje2 = fuente.render(ubicaciony,1,color3)


	screen.fill((0,0,0))
	screen.blit(superficie,(posx,posy))

	posx += velocidadx
	posy += velocidady

	for evento in pygame.event.get():

		if evento.type == QUIT:
			pygame.quit()
			sys.exit()
		elif evento.type == pygame.KEYDOWN:
			if evento.key == pygame.K_LEFT:
				velocidadx = -0.2
				move = "left"
				movement = True
				s=0
				
				
			elif evento.key == pygame.K_RIGHT:
				velocidadx = +0.2
				move = "right"
				movement = True
				s=0

			
			elif evento.key == pygame.K_UP:
				velocidady = -0.2
				move = "up"
				movement = True
				s=0
				
			elif evento.key == pygame.K_DOWN:
				velocidady = 0.2
				move = "down"
				movement = True
				s=0
			elif evento.key == pygame.K_z:
				movement = True
				attack = True





		elif evento.type == pygame.KEYUP:
			if evento.key == pygame.K_LEFT:
				if pygame.key.get_pressed()[K_DOWN]:
					move = "down"
				elif pygame.key.get_pressed()[K_UP]:
					move = "up"
				else:
					movement = False
				if pygame.key.get_pressed()[K_RIGHT]:
					velocidadx = 0.2
					move = "right"
					movement = True
				else:
					velocidadx = 0
				
			elif evento.key == pygame.K_RIGHT:
				if pygame.key.get_pressed()[K_DOWN]:
					move = "down"
				elif pygame.key.get_pressed()[K_UP]:
					move = "up"
				else:
					movement = False
				if pygame.key.get_pressed()[K_LEFT]:
					velocidadx = -0.2
					move = "left"
					movement = True
				else:
					velocidadx = 0
				
			elif evento.key == pygame.K_UP:
				if pygame.key.get_pressed()[K_LEFT]:
					move = "left"
				elif pygame.key.get_pressed()[K_RIGHT]:
					move = "right"
				else:
					movement = False
				if pygame.key.get_pressed()[K_DOWN]:
					velocidady = 0.2
					move = "down"
					movement = True
				else:
					velocidady = 0
				
			elif evento.key == pygame.K_DOWN:
				if pygame.key.get_pressed()[K_LEFT]:
					move = "left"
				elif pygame.key.get_pressed()[K_RIGHT]:
					move = "right"
				else:
					movement = False
				if pygame.key.get_pressed()[K_UP]:
					velocidady = -0.2
					move = "up"
					movement = True
				else:
					velocidady = 0

	# animacion
	down = [(0, 0, 32, 32), (0, 59, 32 , 32)]
	up = [(122, 0, 32 ,32), (122, 59 ,32, 32)]
	left = [(59, 0, 32, 32), (59, 59, 32, 32)]
	right = [(180, 0 ,32,32), (180, 59 , 32, 32)]
	attack_left = [(59,120,32,32),(48,180,54,32)]
	attack_right = [(180,120,32,32),(168,180,54,32)]
	attack_up = [(120,120,32,32),(120,168,32,54)]
	attack_down = [(0,120,32,32),(0,168,32,54)]
	if movement:
		if move == "down":
			if round(s)%2==0:
				sprite_section = down[0]
			else:
				sprite_section = down[1]
		elif move == "up":
			if round(s)%2==0:
				sprite_section = up[0]
			else:
				sprite_section = up[1]
		elif move == "left":
			if round(s)%2==0:
				sprite_section = left[0]
			else:
				sprite_section = left[1]
		elif move == "right":
			if round(s)%2==0:
				sprite_section = right[0]
			else:
				sprite_section = right[1]
	##################################################
		if attack:
			if move == "down":
				if round(a)%2==0:
					sprite_section = attack_down[0]
				else:
					sprite_section = attack_down[1]
			elif move == "up":
				if round(a)%2==0:
					sprite_section = attack_up[0]
				else:
					sprite_section = attack_up[1]
			elif move == "left":
				if round(a)%2==0:
					sprite_section = attack_left[0]
				else:
					sprite_section = attack_left[1]
			elif move == "right":
				if round(a)%2==0:
					sprite_section = attack_right[0]
				else:
					sprite_section = attack_right[1]


		s += 0.005
		a += 0.01





	screen.blit(mensaje,(0,0))
	screen.blit(mensaje2,(0,10))

	pygame.display.update()
