import pygame
import sys

pygame.init()

FPS = 60
red = (255,0,0)
white = (255,255,255)
W = 1000
H = 800
r = 25

display = pygame.display.set_mode((W,H))
pygame.display.set_caption('nooloudy')
clock = pygame.time.Clock()
rect = display.get_rect()

x = 100
y = 100

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
    display.fill(white)
    pygame.draw.circle(display, red, (x,y), r)
    
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and x < rect.right - r:
                x+=20
            if event.key == pygame.K_LEFT and x > rect.left + r:
                x-=20
            if event.key == pygame.K_UP and y > rect.top + r:
                y-=20
            if event.key == pygame.K_DOWN and y < rect.bottom - r:
                y+=20

    pygame.display.flip()

    

    clock.tick(FPS) 

print("That's all")