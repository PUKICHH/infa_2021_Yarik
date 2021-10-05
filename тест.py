import pygame
import math
pygame.init()
screen = pygame.display.set_mode((1200, 800))
#цвета
WHITE = (255,255,255)
BLACK = (0,0,0)


#задник константы
r1 = pygame.Rect(0, 0, 1200, 100)
r2 = pygame.Rect(0, 150, 1200, 100)
r3 = pygame.Rect(0, 100, 1200, 50)
r4 = pygame.Rect(0, 250, 1200, 150)
r5 = pygame.Rect(0, 400, 1200, 100)
r6 = pygame.Rect(0, 500, 1200, 300)
pi = 3.14


#задник
pygame.draw.rect(screen, (20, 47, 200), r1, 0)
pygame.draw.rect(screen, (200, 165, 200), r2, 0)
pygame.draw.rect(screen, (161, 165, 200), r3, 0)
pygame.draw.rect(screen, (199, 118, 147), r4, 0)
pygame.draw.rect(screen, (199, 115, 20), r5, 0)
pygame.draw.rect(screen, (82, 134, 199), r6, 0)


#чайки
pi = 3.14
pygame.draw.arc(screen, WHITE, (500, 200, 100, 50), 0, pi, 3)
pygame.draw.arc(screen, WHITE, (600, 200, 100, 50), 0, pi, 3)
pygame.draw.arc(screen, WHITE, (200, 50, 100, 50), 0, pi, 3)
pygame.draw.arc(screen, WHITE, (300, 50, 100, 50), 0, pi, 3)
pygame.draw.arc(screen, WHITE, (250, 335, 100, 50), 0, pi, 3)
pygame.draw.arc(screen, WHITE, (350, 335, 100, 50), 0, pi, 3)


#тело
pygame.draw.ellipse(screen, WHITE, (400, 550, 280, 100))
pygame.draw.ellipse(screen, WHITE, (620, 560, 120, 50))
pygame.draw.ellipse(screen, WHITE, (700, 540, 100, 60))
pygame.draw.ellipse(screen, WHITE, (700, 540, 100, 60))
pygame.draw.ellipse(screen, BLACK, (750, 550, 20, 10))


#ноги
image1 = pygame.Surface((300, 300))
image1.fill ((0,255,255))
image1.set_colorkey((0,255,255))
pygame.draw.ellipse(image1, WHITE, (10,10,100,50), 0)
new_image1 = pygame.transform.rotate(image1, 300)
screen.blit(new_image1, (280, 600))


image2 = pygame.Surface((300, 300))
image2.fill ((0,255,255))
image2.set_colorkey((0,255,255))
pygame.draw.ellipse(image2, WHITE, (10,10,100,30), 0)
new_image2 = pygame.transform.rotate(image2, 340)
screen.blit(new_image2, (430, 670))


image3 = pygame.Surface((300, 300))
image3.fill ((0,255,255))
image3.set_colorkey((0,255,255))
pygame.draw.ellipse(image3, WHITE, (0,0,70,30), 0)
new_image3 = pygame.transform.rotate(image3, 300)
screen.blit(new_image3, (310, 620))


image4 = pygame.Surface((300, 300))
image4.fill ((0,255,255))
image4.set_colorkey((0,255,255))
pygame.draw.ellipse(image4, WHITE, (0,0,100,30), 0)
new_image4 = pygame.transform.rotate(image4, 340)
screen.blit(new_image4, (470, 660))


#крылья и хвост
x1 = 550
y1 = 500
pygame.draw.polygon(screen, (255, 255, 255), [[x1,y1+100],[x1-10,y1],[x1-100,y1-100],[x1-70,y1],[x1-50,y1+70],[x1-60,y1+100]],0)
x2 = 500
y2 = 500
pygame.draw.polygon(screen, (255, 255, 255), [[x2,y2+100],[x2-10,y2],[x2-150,y2-100],[x2-70,y2],[x2-50,y2+70],[x2-60,y2+100]],0)
pygame.draw.polygon(screen, (WHITE), [[420,590,],[320,540],[300,600],[410,610]],0)


#клюв и когти
pygame.draw.polygon(screen, (255, 255, 0), [[780,550],[850,545],[860,545],[850,565],[800,570]] , 0)
pygame.draw.line(screen,(BLACK), (790,560), (857,550), 1)


#рыба
pygame.draw.ellipse(screen, (72, 209, 204), (800,700,100,40),0)
pygame.draw.circle(screen, (0, 191, 255), (880,720), 10, 0)
pygame.draw.circle(screen, (BLACK), (880,720), 5, 0)
pygame.draw.polygon(screen, (72, 209, 204), [[800, 720], [760, 715], [765, 750]], 0) 
pygame.draw.polygon(screen, (128, 128, 0), [[850, 700], [820, 685], [870, 690], [870, 700]], 0)
pygame.draw.polygon(screen, (128, 128, 0), [[815, 735], [805, 745], [835, 750], [830, 738]], 0)
pygame.draw.polygon(screen, (128, 128, 0), [[865, 740], [855, 745], [885, 750], [880, 738]], 0)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()