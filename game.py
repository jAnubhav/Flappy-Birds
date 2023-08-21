import pygame
from random import randrange
from time import sleep

pygame.init()

# Setting of the screen
screen = pygame.display.set_mode((288, 510))
pygame.display.set_caption('Flappy Birds')

# Setting up the images
icon = pygame.image.load('images\\toucan.png').convert_alpha()
bg = pygame.image.load('images\\bg.png').convert_alpha()
ground = pygame.image.load('images\\base.png').convert_alpha()
bird = pygame.image.load('images\\bird.png').convert_alpha()
pipe = (
    pygame.image.load('images\\pipe.png').convert_alpha(),
    pygame.transform.rotate(pygame.image.load('images\\pipe.png').convert_alpha(), 180)
)

# Global Variables
x_pipe1 = 380
x_pipe2 = 534
y_pipe1 = randrange(-285, -55, 3)
y_pipe2 = randrange(-285, -55, 3)
y_bird = 240
x_change = 0
x_crash1 = range(x_pipe1 - 30, x_pipe1 + 27)
x_crash2 = range(x_pipe2 - 30, x_pipe2 + 27)
y_crash1 = range(y_pipe1 + 320, y_pipe1 + 370)
y_crash2 = range(y_pipe2 + 320, y_pipe2 + 370)
i = 0
crash_flag = False

# Game Loop
status = True
while status:

    # Showing of the main images
    pygame.display.set_icon(icon)
    screen.blit(bg, (0, 0))
    screen.blit(bird, (88, y_bird))

    screen.blit(pipe[1], (x_pipe1, y_pipe1))
    screen.blit(pipe[0], (x_pipe1, y_pipe1 + 395))
    screen.blit(ground, (0, 400))
    
    screen.blit(pipe[1], (x_pipe2, y_pipe2))
    screen.blit(pipe[0], (x_pipe2, y_pipe2 + 395))
    screen.blit(ground, (0, 400))

    pygame.display.update()
    
    # Creation new pipes
    x_pipe1 -= 1
    x_crash1 = range(x_pipe1 - 23, x_pipe1 + 27)
    if x_pipe1 == -40:
        x_pipe1 = 288
        y_pipe1 = randrange(-285, -55)
        y_crash1 = range(y_pipe1 + 320, y_pipe1 + 370)
    
    x_pipe2 -= 1
    x_crash2 = range(x_pipe2 - 23, x_pipe2 + 27)
    if x_pipe2 == -40:
        x_pipe2 = 288
        y_pipe2 = randrange(-285, -55)
        y_crash2 = range(y_pipe2 + 320, y_pipe2 + 370)

    # Change in birds position
    y_bird += x_change

    if 88 in x_crash1:
        if y_bird not in y_crash1:
            status = False
    
    if 88 in x_crash2:
        if y_bird not in y_crash2:
            status = False

    # Main key actions
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            status = False
        
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_UP:
                x_change = -3

            if events.key == pygame.K_DOWN:
                x_change = 3
        
        if events.type == pygame.KEYUP:
            x_change = 0

screen.blit(bg, (0, 0))
screen.blit(ground, (0, 400))
pygame.display.update()

pygame.quit()

