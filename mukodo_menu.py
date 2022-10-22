import pygame
import numpy as np
from paddle import Paddle
from ball import Ball
import time
import cv2
import mediapipe as mp
from pygame import display,movie
import button

pygame.init()
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("image")






#game loop
def start(ball):
    pygame.display.set_caption('Start Menu')
    #button images
    start_img      = pygame.image.load('image/start_btn_kek.png').convert_alpha()
    options_img    = pygame.image.load('image/options.png').convert_alpha()
    exit_img       = pygame.image.load('image/exit.png').convert_alpha()
    #button instances
    start_button   = button.Button(210, 50, start_img, 0.8)
    options_button = button.Button(140, 185, options_img, 0.8)
    exit_button    = button.Button(240, 342, exit_img, 0.8)
    run = True
    valtozo = 0
    while run:
        screen.fill((71,71,71))
        if start_button.draw(screen):
            jatek(ball)
        if options_button.draw(screen):
            options()
        if exit_button.draw(screen):
            valtozo += 1
            if valtozo == 2:
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
    
    run = True
    while run:

        screen.fill((202, 228, 241))
        if back_button.draw(screen):
            start(ball)
            
            
            
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
            ball = Ball(WHITE, 10, 10, 7)
            
    
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
            ball = Ball(WHITE, 10, 10, 10)
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
            ball = Ball(WHITE, 10, 10, 14)
           

        #event handler
        for event in pygame.event.get():
            #quit game
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

def jatek(ball):
    paddleA = Paddle(WHITE, 10, 100)    
    paddleA.rect.x = 20
    paddleA.rect.y = 200

    paddleB = Paddle(WHITE, 10, 100)
    paddleB.rect.x = 670
    paddleB.rect.y = 200


    
    
    ball.rect.x = 345
    ball.rect.y = 195


    # This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()

    # Add the 2 paddles and the ball to the list of objects
    all_sprites_list.add(paddleA)
    all_sprites_list.add(paddleB)
    all_sprites_list.add(ball)

    # The loop will carry on until the user exits the game (e.g. clicks the close button).

    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()

    # Initialise player scores
    scoreA = 0
    scoreB = 0
    valtozo = True
    # camera
    mpDraw = mp.solutions.drawing_utils
    

    pTime= 0
    cTime = 0
    carryOn = True
    while carryOn:
        
        if valtozo == False:
            time.sleep(2)
            valtozo = True

    # --- Main event loop
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                carryOn = False  # Flag that we are done so we exit this loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                    carryOn = False
    #------------------------------------------------------------------------------------------
        success, img = cap.read()
        flipped = cv2.flip(img, 1)
        img = cv2.flip(img, 1)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = flipped.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    if 300 < cx < 690:
                        paddleB.rect.y = cy
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for ko, fa in enumerate(handLms.landmark):
                    z, s, n = flipped.shape
                    nb, nj = int(fa.x*s), int(fa.y*z)
                    if -50 < nb < 300:
                        paddleA.rect.y = nj
    #------------------------------------------------------------------------------------------

                mpDraw.draw_landmarks(flipped, handLms, mpHands.HAND_CONNECTIONS)
        all_sprites_list.update()

        # Check if the ball is bouncing against any of the 4 walls:
        if ball.rect.x >= 690:
            scoreA += 1
            ball.velocity[0] = -ball.velocity[0]
            ball.rect.x = 345
            ball.rect.y = 195
            paddleA.rect.x = 20
            paddleA.rect.y = 200
            paddleB.rect.x = 670
            paddleB.rect.y = 200
            valtozo = False
        if ball.rect.x <= 0:
            scoreB += 1
            ball.velocity[0] = -ball.velocity[0]
            ball.rect.x = 345
            ball.rect.y = 195
            paddleA.rect.x = 20
            paddleA.rect.y = 200
            paddleB.rect.x = 670
            paddleB.rect.y = 200
            valtozo = False
        if ball.rect.y > 490:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]
        if scoreA == 10 or scoreB == 10:
            break
        # Detect collisions between the ball and the paddles
        if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
            ball.bounce()

        # --- Drawing code should go here
        # First, clear the screen to black.
        
        screen.fill(BLACK)
        # Draw the net
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

        # Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen)

        # Display scores:
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, WHITE)
        screen.blit(text, (250, 10))
        text = font.render(str(scoreB), 1, WHITE)
        screen.blit(text, (420, 10))

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        
        #cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3,(255,0,255),3) #ki irasa az fps-t
        cv2.line(img,(300,800),(300,0),(255,255,255),10)

        cv2.imshow("image", flipped)
        cv2.waitKey(1)
    # Once we have exited the main program loop we can stop the game engine:
    pygame.quit()
ball = Ball(WHITE, 10, 10, 7)
start(ball)
