from ball import Ball
from constants import *
import pygame
from enum import Enum

from sides import PaddleSide



class Paddle():
    def __init__(self, side : PaddleSide) -> None:
        self.height = INITIAL_PADDLE_HEIGHT
        self.speed =  PADDLE_INITIAL_SPEED
        self.left = SCREEN_MARGIN if side == PaddleSide.Left else SCREEN_WIDTH - SCREEN_MARGIN - PADDLE_WIDTH
        self.top = SCREEN_HEIGHT/2 - INITIAL_PADDLE_HEIGHT/2 
        self.rect = None
        self.rebound_direction = 1 if side == PaddleSide.Left else -1
        self.is_down_key_pressed = False
        self.is_up_key_pressed = False

    def press_down_key(self):
        self.is_down_key_pressed = True

    def release_down_key(self):
        self.is_down_key_pressed = False

    def press_up_key(self):
        self.is_up_key_pressed = True
    
    def release_up_key(self):
        self.is_up_key_pressed = False

    def move(self, delta_time : float):
        if self.is_down_key_pressed:
            paddle_bottom = self.top + self.height  
            dist_to_bottom = BOTTOM_LIMIT - paddle_bottom
            self.top += min(dist_to_bottom, self.speed * delta_time)
        elif self.is_up_key_pressed:
            dist_to_top = self.top - TOP_LIMIT
            self.top -= min(dist_to_top, self.speed * delta_time)


    def draw(self, screen_surface):
        self.rect = pygame.draw.rect(screen_surface, WHITE,  pygame.Rect(self.left, self.top , PADDLE_WIDTH, self.height))

    def check_collision(self, ball :Ball):
        if self.rect.colliderect(ball.rect):
            ball.rebound(self.rebound_direction, self.top + self.height / 2, (-self.height/2 , self.height/2))

    