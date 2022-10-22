import pygame
import button
import ball
#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))




#game loop
def start():
	pygame.display.set_caption('Start Menu')
	#button images
	start_img      = pygame.image.load('image/start_btn_kek.png').convert_alpha()
	options_img    = pygame.image.load('image/options.png').convert_alpha()
	exit_img       = pygame.image.load('image/exit.png').convert_alpha()
	#button instances
	start_button   = button.Button(240, 50, start_img, 0.8)
	options_button = button.Button(180, 185, options_img, 0.8)
	exit_button    = button.Button(268, 342, exit_img, 0.8)
	run = True
	while run:
		screen.fill((71,71,71))
		if start_button.draw(screen):
			print("elindult a jatek")
		if options_button.draw(screen):
			options()
		if exit_button.draw(screen):
				run = False
		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False

		pygame.display.update()

	pygame.quit()
def options():
	pygame.display.set_caption('Options Menu')
	#load button images
	easy_img      = pygame.image.load('image/easy_zold.png').convert_alpha()
	normal_img    = pygame.image.load('image/normal_piros.png').convert_alpha()
	hard_img      = pygame.image.load('image/Hard_piros.png').convert_alpha()
	back_img      = pygame.image.load('image/back.png').convert_alpha()
	#create button instances
	easy_button   = button.Button(250, 10, easy_img, 0.8)
	normal_button = button.Button(200, 134, normal_img, 0.8)
	hard_button   = button.Button(250, 249, hard_img, 0.8)
	back_button   = button.Button(247, 389, back_img, 0.8)
	sebbesseg = 7
	run = True
	while run:

		screen.fill((202, 228, 241))
		if back_button.draw(screen):
			start()
		if easy_button.draw(screen):
			#easy gomb zold
			easy_img = pygame.image.load('image/easy_zold.png').convert_alpha()
			easy_button = button.Button(250, 10, easy_img, 0.8)
			#normal gomb piros
			normal_img = pygame.image.load('image/normal_piros.png').convert_alpha()
			normal_button = button.Button(200, 134, normal_img, 0.8)
			#hard gomb piros
			hard_img = pygame.image.load('image/Hard_piros.png').convert_alpha()
			hard_button = button.Button(250, 249, hard_img, 0.8)
			sebbesseg = 7
			return sebbesseg 

		if normal_button.draw(screen):
			#normal gomb zold
			normal_img = pygame.image.load('image/normal_zold.png').convert_alpha()
			normal_button = button.Button(200, 134, normal_img, 0.8)
			#easy gomb piros
			easy_img = pygame.image.load('image/easy_piros.png').convert_alpha()
			easy_button = button.Button(250, 10, easy_img, 0.8)
			#hard gomb piros
			hard_img = pygame.image.load('image/Hard_piros.png').convert_alpha()
			hard_button = button.Button(250, 249, hard_img, 0.8)
			sebbesseg = 14
		if hard_button.draw(screen):
			#hard gomb zold
			hard_img = pygame.image.load('image/Hard_zold.png').convert_alpha()
			hard_button = button.Button(250, 249, hard_img, 0.8)
			#easy gomb piros
			easy_img = pygame.image.load('image/easy_piros.png').convert_alpha()
			easy_button = button.Button(250, 10, easy_img, 0.8)
			#normal gomb 
			normal_img = pygame.image.load('image/normal_piros.png').convert_alpha()
			normal_button = button.Button(200, 134, normal_img, 0.8)
			sebbesseg = 28
			return sebbesseg

		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False

		pygame.display.update()

	pygame.quit()

start()