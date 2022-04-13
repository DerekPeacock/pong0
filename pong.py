'''
This modules is a basic example of moving rectangular
shapes or images around the screen.
Author: Derek Peacock
'''
import pygame
pygame.init()

screenWidth = 600
screenHeight = 340

game_window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Derek's Pong 0")

# Load the Background and Player's Character

background = pygame.image.load('images/green_background_600.png')
character = pygame.image.load('images/0_Golem_Running_002.png')

# Rectangular Sprite

global paddle_x
paddle_x = 50

global paddle_y
paddle_y = 50

global paddle_width
paddle_width = 20

global paddle_height
paddle_height = 80

global velocity; velocity = 5
global playing; playing = True

global isJumping
isJumping = False

global jumpCount
jumpCount = 10

def movePaddle():
    '''
    Move the paddle left, right, up or down with arrow keys as well
    as jumping if the space bar is pressed.
    '''
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and paddle_x > velocity:
        paddle_x -= velocity

    if (keys[pygame.K_RIGHT] and 
        paddle_x < screenWidth - paddle_width - velocity):
        paddle_x += velocity

    if not(isJumping):

        if keys[pygame.K_UP] and paddle_y > velocity:
            paddle_y -= velocity
        
        if (keys[pygame.K_DOWN] and paddle_y < 
            screenHeight - paddle_height - velocity):
            paddle_y += velocity

        if (keys[pygame.K_SPACE]):
            isJumping = True
    else:
        if jumpCount >= -10:
            negative = 1
            if(jumpCount < 0):
                negative = -1
            paddle_y -= (jumpCount ** 2) * 0.5 * negative
            jumpCount -= 1
        else:
            isJumping = False
            jumpCount = 10
    
    return

def draw():
    
    game_window.blit(background, (0,0))
    game_window.blit(character, (100,100))

    pygame.draw.rect(game_window, (255, 0, 0), 
        (paddle_x, paddle_y, paddle_width, paddle_height))

    pygame.display.update()

# Main Game Loop

while playing:
    pygame.time.delay(50)

    # Check all the events since last time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    
    movePaddle()

    # Draw Everything

    draw()

pygame.quit()


