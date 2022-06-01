import sys
import pygame
from constants import *

pygame.init()
screen_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("TEST")


# GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    m_pos = pygame.mouse.get_pos()

    screen_surface.fill(BLACK)
    rect = pygame.draw.rect(screen_surface, WHITE, pygame.Rect(300, 200,80,80) )
    rect_2 = pygame.draw.rect(screen_surface, (255,0,0), pygame.Rect(350, 150,40,40) )
    pygame.draw.line(screen_surface, (225,225,0), rect.center, m_pos)
    pygame.display.update()