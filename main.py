import pygame
import sys
import random

# Functions


def game_floor():
    screen.blit(floor_base, (floor_x_pos, 750))
    screen.blit(floor_base, (floor_x_pos + 576, 750))


def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False

    if bird_rect.top <= -100 or bird_rect.bottom >= 900:
        return False
    return True


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    top_pipe = pipe_surface.get_rect(midbottom=(800, random_pipe_pos - 250))
    bottom_pipe = pipe_surface.get_rect(midtop=(800, random_pipe_pos))
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5

    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 800:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)
    return pipes


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
floor_x_pos = 0

message = pygame.image.load("assets/Game_Over.png").convert_alpha()
game_over_rect = message.get_rect(center=(288, 112))
restart = pygame.image.load("assets/restart.png").convert_alpha()

# Buliding pipes

pipe_surface = pygame.image.load("assets/pipe.png")
pipe_list = []
pipe_height = [300, 400, 600]

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

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
                bird_movement -= 10
            if event.key == pygame.K_SPACE and game_active == False:
                bird_rect.centery = (100, 512)
                bird_movement = 0
                pipe_list.clear()
                game_active = True
        if event.type == SPAWNPIPE and game_active:
            pipe_list.extend(create_pipe())

    screen.blit(background, (0, 0))
    if game_active:
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird, bird_rect)
        # Draw pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        # Check for collision
        game_active = check_collision(pipe_list)
    else:
        screen.blit(message, game_over_rect)

    # Create the floor
    floor_x_pos -= 1
    game_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)
