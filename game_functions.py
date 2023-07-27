import pygame
import random
import pickle
import os


def game_floor():
    screen.blit(floor_base, (floor_x_pos, 750))
    screen.blit(floor_base, (floor_x_pos + 576, 750))


def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            die_sound.play()
            return False

    if bird_rect.top <= -100 or bird_rect.bottom >= 900:
        die_sound.play()
        return False
    return True


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    top_pipe = pipe_surface.get_rect(midbottom=(800, random_pipe_pos - 250))
    bottom_pipe = pipe_surface.get_rect(midtop=(800, random_pipe_pos))
    return bottom_pipe, top_pipe


def move_pipes(pipes, score):
    for pipe in pipes:
        pipe.centerx -= 5
        if pipe.centerx == 100:
            score += 1

    return pipes, score


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 800:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)
    return pipes


def reset_game():
    global bird_movement, pipe_list, game_active, score
    bird_rect.centery = 512
    bird_movement = 0
    pipe_list.clear()
    score = 0
    game_active = True


def load_high_score():
    if os.path.exists("high_score.txt"):
        with open("high_score.txt", "rb") as file:
            return pickle.load(file)
    else:
        return 0


def save_high_score(high_score):
    with open("high_score.txt", "wb") as file:
        pickle.dump(high_score, file)


def update_score(current_score, high_score):
    score_font = pygame.font.Font("font/PressStart2P-Regular.ttf", 36)
    score_surface = score_font.render(f"{current_score}", True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(288, 50))
    screen.blit(score_surface, score_rect)

    best_score_surface = score_font.render(f"High: {high_score}", True, (255, 255, 255))
    best_score_rect = best_score_surface.get_rect(center=(288, 680))
    screen.blit(best_score_surface, best_score_rect)


pygame.init()

clock = pygame.time.Clock()

gravity = 0.25
bird_movement = 0

screen = pygame.display.set_mode((576, 900))
score = 0
high_score = 0

background = pygame.image.load("assets/bg.png").convert_alpha()

bird = pygame.image.load("assets/bird2.png").convert()
bird_rect = bird.get_rect(center=(100, 512))

score_font = pygame.font.Font("font/PressStart2P-Regular.ttf", 36)
score_surface = score_font.render(f"Score: {score}", True, (255, 255, 255))
score_rect = score_surface.get_rect(center=(288, 112))
screen.blit(score_surface, score_rect)

floor_base = pygame.image.load("assets/ground.png").convert()
floor_base = pygame.transform.scale2x(floor_base)
floor_x_pos = 0

message = pygame.image.load("assets/flappy_bird.png").convert_alpha()
message = pygame.transform.scale2x(message)
game_over_rect = message.get_rect(center=(288, 312))

restart = pygame.image.load("assets/restart.png").convert_alpha()

# Buliding pipes

pipe_surface = pygame.image.load("assets/pipe.png")
pipe_list = []
pipe_height = [300, 400, 600]

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

game_active = True

# Sound

flap_sound = pygame.mixer.Sound("sound/flap.mp3")
die_sound = pygame.mixer.Sound("sound/hit.mp3")
hit_sound = pygame.mixer.Sound("sound/hit.mp3")
