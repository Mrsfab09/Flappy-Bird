import pygame
import sys
import random

# Functions


def game_floor():
    screen.blit(floor_base, (floor_x_pos, 750))
    screen.blit(floor_base, (floor_x_pos + 576, 750))


def check_collision():
    if bird_rect.top <= -100 or bird_rect.bottom >= 900:
        return False
    return True


# Variables

pygame.init()
clock = pygame.time.Clock()

gravity = 0.25
bird_movement = 0

screen = pygame.display.set_mode((576, 900))

background = pygame.image.load("assets/bg.png").convert_alpha()

bird = pygame.image.load("assets/bird2.png").convert()
bird_rect = bird.get_rect(center=(100, 512))

floor_base = pygame.image.load("assets/ground.png").convert()
floor_base = pygame.transform.scale2x(floor_base)

# Game Loop
floor_x_pos = 0
game_active = True

# start the game

pygame.display.set_caption("Flappy Bird")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 12
            if event.key == pygame.K_SPACE and game_active == False:
                bird_rect.centery = (100, 512)
                bird_movement = 0
                game_active = True

    screen.blit(background, (0, 0))
    if game_active:
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird, bird_rect)
        # Check for collision
        game_active = check_collision()
    else:
        print("Game Over")

    # Create the floor
    floor_x_pos -= 1
    game_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)
