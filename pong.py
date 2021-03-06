'''
This modules is a basic example of moving rectangular
shapes or images around the screen.
Author: Derek Peacock
Author: Nick Day
'''
import pygame
global is_jumping, jump_count, paddle_x, paddle_y, paddle_height, paddle_width
global ball_x, ball_y, ball_width, ball_height, ball_x_direction, ball_y_direction
BALL_VELOCITY = 5

def move_ball():
    global paddle_x, paddle_y
    global ball_x, ball_y, ball_height, ball_width, ball_x_direction, ball_y_direction

    if(ball_y > (game_window.get_height() - ball_height)):
        ball_y_direction = -BALL_VELOCITY

    if(ball_x > (game_window.get_width() - ball_width)):
        ball_x_direction = -BALL_VELOCITY

    if(ball_y < 0):
        ball_y_direction = BALL_VELOCITY

    if(ball_x < 0):
        ball_x_direction = BALL_VELOCITY

    if( abs(paddle_x - ball_x) == 0 ):
        ball_x_direction = BALL_VELOCITY

    ball_x = ball_x + ball_x_direction
    ball_y = ball_y + ball_y_direction
   

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

    pygame.draw.ellipse(game_window, (0,255, 0), 
         (ball_x, ball_y, ball_width, ball_height))

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

# Ball

ball_x = 100
ball_y = 100
ball_width = 25
ball_height = 25

ball_x_direction = BALL_VELOCITY
ball_y_direction = BALL_VELOCITY

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
    move_ball()

    # Draw Everything

    draw()

pygame.quit()