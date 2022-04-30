'''
This modules is a basic example of moving rectangular
shapes or images around the screen.
Author: Derek Peacock
'''
import pygame
global is_jumping, jump_count, paddle_x, paddle_y, paddle_height, paddle_width


def move_paddle():
    '''
    Move the paddle left, right, up or down with arrow keys as well
    as jumping if the space bar is pressed.
    '''
    global is_jumping, jump_count, paddle_x, paddle_y, paddle_height, paddle_width
    JUMP_HEIGHT = 8

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and paddle_x > velocity:
        paddle_x -= velocity

    if (keys[pygame.K_RIGHT] and 
        paddle_x < SCREEN_WIDTH - paddle_width - velocity):
            paddle_x += velocity

    if (is_jumping == False):

        if keys[pygame.K_UP] and paddle_y > velocity:
            paddle_y -= velocity
        
        if (keys[pygame.K_DOWN] and paddle_y < 
            SCREEN_HEIGHT - paddle_height - velocity):
            paddle_y += velocity

        if (keys[pygame.K_SPACE]): is_jumping = True
    else:
        if jump_count >= -JUMP_HEIGHT:
            negative = 1
            if(jump_count < 0): negative = -1
            paddle_y -= (jump_count ** 2) * 0.5 * negative
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = JUMP_HEIGHT
    return


def draw():
    '''
    Draw the background and the characters as images.  Draw a rectangle
    to represent the paddle.
    '''
    game_window.blit(background, (0,0))
    game_window.blit(character, (100,100))

    pygame.draw.rect(game_window, (255, 0, 0), 
        (paddle_x, paddle_y, paddle_width, paddle_height))

    pygame.display.update()
    return


pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 340

game_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Derek's Pong 0")

# Load the Background and Player's Character

background = pygame.image.load('images/green_background_600.png')
character = pygame.image.load('images/0_Golem_Running_002.png')

# Rectangular Sprite

paddle_x = 50
paddle_y = 50
paddle_width = 20
paddle_height = 80

velocity = 5
playing = True

is_jumping = False
jump_count = 10

# Main Game Loop

print(__doc__)

while playing:
    pygame.time.delay(50)

    # Check all the events since last time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    
    # Update Everything

    move_paddle()

    # Draw Everything

    draw()

pygame.quit()