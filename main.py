import pygame
import sys
from game_functions import *

# Variables
high_score = load_high_score()
# start the game
pygame.init()

pygame.display.set_caption("Flappy Bird")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_high_score(high_score)
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 10
                flap_sound.play()
            if event.key == pygame.K_SPACE and not game_active:
                reset_game()

        if event.type == SPAWNPIPE and game_active:
            pipe_list.extend(create_pipe())
            pipe_list, score = move_pipes(pipe_list, score)

    screen.blit(background, (0, 0))
    if game_active:
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird, bird_rect)
        # Draw pipes
        draw_pipes(pipe_list)
        pipe_list, score = move_pipes(pipe_list, score)
        # Check for collision
        game_active = check_collision(pipe_list)
        if game_active:
            update_score(score, high_score)
            if score > high_score:
                high_score = score
    else:
        screen.blit(message, game_over_rect)
        update_score(score, high_score)

    # Create the floor
    floor_x_pos -= 1
    game_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)
