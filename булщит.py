import pygame
from pygame.draw import *
from random import randint
import numpy as np
pygame.init()

FPS = 10                                            #частота кадров
screen = pygame.display.set_mode((800, 600))        #размер окна

RED = (255, 0, 0)                                   #список цветов
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
TITLE = (255, 140, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

    
def new_ball():
    global x, y, r, color, v_x, v_y
    x = randint(30, 770)
    y = randint(30, 570)
    r = randint(10, 30)
    color = COLORS[randint(0, 5)]
    v_x = randint(-10, 10)
    v_y = randint(-10, 10)
    circle(screen, color, (x, y), r)
    
def new_aim():
    global x_aim, y_aim, r_aim, R_aim, color_aim_1, color_aim_2
    x_aim = randint(100, 700)
    y_aim = randint(100, 500)
    R_aim = randint(10, 30)
    r_aim = R_aim // 3
    n = randint(0, 5)
    color_aim_1 = COLORS[n]
    color_aim_2 = COLORS[5 - n]
    circle(screen, color_aim_1, (x_aim, y_aim), R_aim)
    circle(screen, color_aim_2, (x_aim, y_aim), r_aim)

def click(event):
    distance = ((event.pos[0] - x_aim)**2 + (event.pos[1] - y_aim)**2)**0.5 
    if distance <= r_aim:
        return 5*(35 - R_aim)
    elif distance <= R_aim:
        return (35 - R_aim)
    for i in range(num):
        distance = ((event.pos[0] - X[i])**2 + (event.pos[1] - Y[i])**2)**0.5 
        if distance <= R[i]:
            return (35 - R[i])
    return 0
    
pygame.display.update()
clock = pygame.time.Clock()
finished = False
points = 0  
num = 3                                          #одновременное количество шаров на экране
X = [0]*num                                      #списки для хранения данных о шарах
Y = [0]*num
V_x = [0]*num
V_y = [0]*num
R = [0]*num
Col = [0]*num

player_name = input("Как вас зовут? ")           #запись имени игрока

while not finished:
    screen.fill(BLACK)
    for i in range (num):                        #создаем "num" шаров и записываем их параметры
        new_ball()
        X[i] = x
        Y[i] = y
        V_x[i] = v_x
        V_y[i] = v_y
        R[i] = r
        Col[i] = color

    new_aim()                                    #создаем бонусную мишень 
    
    font = pygame.font.Font(None, 30)            #табло очков
    text = font.render('Score: ' + str(points), True, WHITE)
    screen.blit(text, (0, 0)) 
    
    pygame.display.update() 
    clock.tick(FPS)
    for event in pygame.event.get():             #диспетчеризация событий
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            points += click(event)
                
    #загатовка параметров для движения бонусной мишени: ось вращения + направление
    rot_x = x_aim + randint(30, 50)               
    rot_y = y_aim + randint(30, 50) 
    if randint(0, 1) == 0:
        a = 0.1 
    else:
        a = -0.1 

    for t in range(30):                          #движение шаров и бонусной мишени
        screen.fill(BLACK)
        for i in range(num):
            X[i] += V_x[i]
            Y[i] += V_y[i]
            if X[i] < 30 or X[i] > 770:          #обработка столкновений со стенами
                V_x[i] = -V_x[i]
            elif Y[i] < 30 or Y[i] > 570:
                V_y[i] = -V_y[i]
            circle(screen, Col[i], (X[i], Y[i]), R[i])

        #поворот бонусной мишени
        x_tmp = (x_aim - rot_x)*np.cos(a) - (y_aim - rot_y)*np.sin(a) + rot_x
        y_tmp = (x_aim - rot_x)*np.sin(a) + (y_aim - rot_y)*np.cos(a) + rot_y
        x_aim = int(x_tmp)
        y_aim = int(y_tmp)
        circle(screen, color_aim_1, (x_aim, y_aim), R_aim)
        circle(screen, color_aim_2, (x_aim, y_aim), r_aim)
        
        font = pygame.font.Font(None, 30)        #табло очков
        text = font.render('Score: ' + str(points), True, WHITE)
        screen.blit(text, (0, 0)) 

        pygame.display.update() 
        clock.tick(FPS)
        for event in pygame.event.get():         #диспетчеризация событий
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                points += click(event)

                    
pygame.quit()