

import pygame

from score import ScoreManager

pygame.init() 

import sys

from ball import Ball
from constants import *
from paddle import Paddle, PaddleSide
from utils import center_dashed_line


FPS = 60


screen_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Ping Pong")

pygame.key.set_repeat(1, 10)

clock = pygame.time.Clock()

score_font = pygame.font.SysFont('Ariel', 64)


paddle_1 = Paddle(PaddleSide.Left )
paddle_2 = Paddle(PaddleSide.Right)
ball = Ball(8)
# GAME LOOP
running = True
while running:
    
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
            running = False
            pygame.quit()
            sys.exit()
    

        elif event.type == pygame.KEYDOWN:
          
            if event.key == pygame.K_w:
                paddle_1.press_up_key()
            elif event.key == pygame.K_s:
                paddle_1.press_down_key()
      
            if event.key == pygame.K_UP:
                paddle_2.press_up_key()
            elif event.key == pygame.K_DOWN:
                paddle_2.press_down_key()
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                paddle_1.release_up_key()
            elif event.key == pygame.K_s:
                paddle_1.release_down_key()

            if event.key == pygame.K_UP:
                paddle_2.release_up_key()
            elif event.key == pygame.K_DOWN:
                paddle_2.release_down_key()


       
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
        #         print("KEY STROKE UNPRESSED")
    delta_time = clock.tick(FPS) / 1000
    


    paddle_1.move(delta_time)
    paddle_2.move(delta_time)
    ball.move(delta_time)

    screen_surface.fill(BLACK)
    ScoreManager.show_score(screen_surface, score_font)
    paddle_1.draw(screen_surface)
    paddle_2.draw(screen_surface)
    ball.draw(screen_surface)

    center_dashed_line(screen_surface)

    paddle_1.check_collision(ball)
    paddle_2.check_collision(ball)

    pygame.display.update()

    
