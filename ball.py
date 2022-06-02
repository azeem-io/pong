from typing import Tuple
from constants import *
import pygame
import math
from score import ScoreManager
from sides import PaddleSide

from utils import map_value_to_range

class Ball():
    def __init__(self, radius : int ) -> None:
        self.radius = radius
        # self.color = WHITE
        self.speed = BALL_INITIAL_SPEED     
        self.rect = None
        self.x_pos =0
        self.y_pos = 0
        self.direction = (0, 0)
        self.reset()



    #manages initial direction | Rebound from horizontal walls
    #detects collision with vertical wall to change score
    def move(self, delta_time):
        self.x_pos += self.direction[0]*self.speed * delta_time
        self.y_pos += self.direction[1]*self.speed * delta_time

        if self.y_pos < TOP_LIMIT or self.y_pos > BOTTOM_LIMIT:
            self.direction = (self.direction[0], -self.direction[1])

        if self.x_pos < SCREEN_MARGIN:
            ScoreManager.score(PaddleSide.Right)
            self.reset(PaddleSide.Right)
        if self.x_pos > SCREEN_WIDTH - SCREEN_MARGIN:
            ScoreManager.score(PaddleSide.Left)
            self.reset(PaddleSide.Left)



    #rebounds the ball when it collides with the paddle
    #the angle of rebound depends on the point of collision 
    def rebound(self, rebound_direction:int, paddle_center, paddle_dist_range : Tuple ):
        dist_from_paddle_center = paddle_center - self.y_pos
        angle = map_value_to_range(dist_from_paddle_center, paddle_dist_range, (-MAX_REBOUND_ANGLE, MAX_REBOUND_ANGLE))
        angle = math.radians(angle)
        self.direction = (rebound_direction * math.cos(angle), -math.sin(angle))
        

    def draw(self, screen_surface):
        self.rect = pygame.draw.circle(screen_surface, WHITE, (self.x_pos, self.y_pos), self.radius)


    #resets the ball position and direction
    def reset(self, scoring_side : PaddleSide = PaddleSide.Left):
        self.x_pos = SCREEN_WIDTH/2
        self.y_pos = SCREEN_HEIGHT/2
        self.direction = ( 1 if scoring_side == PaddleSide.Right else -1, 0)



