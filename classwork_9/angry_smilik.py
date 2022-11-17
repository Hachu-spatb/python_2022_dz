import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill((255, 255, 255))

pygame.draw.circle(screen, (255, 255, 0), (200, 175), 120)
pygame.draw.circle(screen, (0, 0, 0), (200, 175), 120, 2)

pygame.draw.circle(screen, (255, 0, 0), (155, 155), 23)
pygame.draw.circle(screen, (0, 0, 0), (155, 155), 23, 1)

pygame.draw.circle(screen, (255, 0, 0), (250, 155), 17)
pygame.draw.circle(screen, (0, 0, 0), (250, 155), 17, 1)

pygame.draw.circle(screen, (0, 0, 0), (155, 155), 10)
pygame.draw.circle(screen, (0, 0, 0), (250, 155), 10)

pygame.draw.rect(screen, (0, 0, 0), (150, 240, 105, 20))

pygame.draw.line(screen, (0, 0, 0), (80, 70), (180, 115), 20)
pygame.draw.line(screen, (0, 0, 0), (320, 70), (225, 115), 20)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()