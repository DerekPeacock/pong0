import pygame
pygame.init()

screenWidth = 600
screenHeight = 400

game_window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Derek's Pong 0")

# Rectangular Sprite

paddle_x = 50
paddle_y = 50
paddle_width = 20
paddle_height = 80

velocity = 5
playing = True

isJumping = False
jumpCount = 10

def movePaddle():
    return

# Main Game Loop

while playing:
    pygame.time.delay(50)

    # Check all the events since last time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    
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

    movePaddle()


    # Draw Everything

    game_window.fill((0, 0, 0))

    pygame.draw.rect(game_window, (255, 0, 0), 
        (paddle_x, paddle_y, paddle_width, paddle_height))

    pygame.display.update()
    
pygame.quit()


