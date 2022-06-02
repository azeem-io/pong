from constants import *
import pygame
from sides import PaddleSide

class ScoreManager():
    scores = [0,0]

    @classmethod  
    def show_score(cls,screen_surface, score_font:pygame.font.Font):
        text_surface = score_font.render(f"{cls.scores[0]}    {cls.scores[1]}", True, WHITE)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH/2 , 35))
        screen_surface.blit(text_surface, text_rect)

    @classmethod
    def score(cls, side : PaddleSide):
        cls.scores[int(side)] += 1
        

