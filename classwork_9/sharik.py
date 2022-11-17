import random
import pygame
from pygame.draw import *
from random import randint
pygame.init()
pygame.font.init()

FPS = 30
balls_number = 5
size_x, size_y = 900, 700
screen = pygame.display.set_mode((size_x, size_y))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

'''задаем изначальные параметры надписи'''
font = pygame.font.SysFont('Verdana.ttf', 60)
text_color = GREEN

'''создаем массивы для данных шариков'''
x = [0] * balls_number
y = [0] * balls_number
r = [0] * balls_number
v_x = [0] * balls_number
v_y = [0] * balls_number
color = [GREEN] * balls_number

def new_ball(i):
    '''рисует новый шарик '''
    global x, y, r, v_x, v_y, color
    r[i] = randint(20, 70)
    x[i] = randint(r[i], size_x - r[i])
    y[i] = randint(r[i], size_y - r[i])
    '''деление на FPS, чтобы скорость от него не зависела'''
    v_x[i] = (random.random() - 0.5) * 600 / FPS
    v_y[i] = (random.random() - 0.5) * 600 / FPS
    if((v_x == 0) and (v_y == 0)):
        v_y = 1
    color[i] = COLORS[randint(0, 5)]

def draw_balls():
    '''отрисовывает все шарики в игре'''
    global x, y, r, color, text_color, scores
    screen.fill(BLACK)
    for i in range(balls_number):
        circle(screen, color[i], (x[i], y[i]), r[i])
    text_surface = font.render('Scores: ' + str(scores), False, text_color)
    screen.blit(text_surface, (0, 0))

def click(event):
    '''проверяет, попали ли по шарику'''
    global x, y, r
    click_pos = event.pos
    for i in range(balls_number):
        if ((click_pos[0] - x[i]) ** 2 + (click_pos[1] - y[i]) ** 2 <= r[i] ** 2):
            return i
    return -1

def update_position():
    '''перемещение шарика, сообщение очков игрокам'''
    global x, y, r, v_x, v_y, color, text_color
    for i in range(balls_number):
        x[i] += v_x[i]
        y[i] += v_y[i]
    draw_balls()
    pygame.display.update()

def get_scores(i):
    '''увеличивает очки, генерирует новый шарик после того, как его поймали'''
    global scores, text_color, color
    scores += 10
    screen.fill(BLACK)
    text_color = color[i]
    new_ball(i)
    draw_balls()
    pygame.display.update()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

scores = 0
for i in range(balls_number):
    new_ball(i)
draw_balls()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            number_catched = click(event)
            if(number_catched != -1):
                get_scores(number_catched)

    update_position()
    for i in range(balls_number):
        if(x[i] - r[i] < 0) or (x[i] + r[i] > size_x):
            v_x[i] = -v_x[i]
        if(y[i] - r[i] < 0) or (y[i] + r[i] > size_y):
            v_y[i] = -v_y[i]

pygame.quit()