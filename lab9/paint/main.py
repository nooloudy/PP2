import pygame
import random
import sys

window_x = 1350
window_y = 700

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)
green = (0,255,0)
blue = (0,0,255)
gray = (127,127,127)
purple = (240,0,255)
orange = (255,100,10)
lime = (180,255,100)
pink = (255,100,180)
pygame.init()
brush_size = 0
active_color = black 
active_figure = 0
pygame.display.set_caption('nooloudy^s paint')
screen = pygame.display.set_mode((window_x, window_y))
painting = []
FPS = pygame.time.Clock()
position_of_mouse = (0,0)
size = (0,0)
thickness = 0

def figure_button():
    pygame.draw.line(screen, black, (250,0), (250,85),5)
    square_button = pygame.draw.rect(screen, black, [260,10,50,50])
    pygame.draw.rect(screen, white, [270,20,30,30])
    circle_button = pygame.draw.rect(screen, black, [320,10,50,50])
    pygame.draw.circle(screen, white, (345,35), 16)
    
    list_of_figure = [square_button, circle_button]
    return list_of_figure



def draw_menu(size, color):
    pygame.draw.rect(screen, gray, [0,0,window_x, 85])
    pygame.draw.line(screen, black, (0,85) , (window_x, 85), 9)
    XL_button = pygame.draw.rect(screen, black, [10,10,50,50])
    pygame.draw.circle(screen, white, (35,35), 20)
    L_button = pygame.draw.rect(screen, black, [70,10,50,50])
    pygame.draw.circle(screen, white, (95,35), 15)
    M_button = pygame.draw.rect(screen, black, [130,10,50,50])
    pygame.draw.circle(screen, white, (155,35), 10)
    S_button = pygame.draw.rect(screen, black, [190,10,50,50])
    pygame.draw.circle(screen, white, (215,35), 5)
    
    brush_list = [XL_button, L_button, M_button, S_button] 

    if size == 20:
        pygame.draw.rect(screen, green, [10,10,50,50], 3)
    elif size == 15:
        pygame.draw.rect(screen, green, [70,10,50,50], 3)
    elif size == 10:
        pygame.draw.rect(screen, green, [130,10,50,50], 3)
    elif size == 5:
        pygame.draw.rect(screen, green, [190,10,50,50], 3)


    pygame.draw.circle(screen, color ,(window_x - 200, 35), 30)
    pygame.draw.circle(screen, 'dark gray', (window_x - 200, 35), 30, 3)

    yellow_color = pygame.draw.rect(screen, yellow, [window_x - 35, 10, 20, 20])
    blue_color = pygame.draw.rect(screen, blue, [window_x - 35, 30, 20, 20])
    red_color = pygame.draw.rect(screen, red, [window_x - 35, 50, 20, 20])
    black_color = pygame.draw.rect(screen, black, [window_x - 55, 10, 20, 20])
    orange_color = pygame.draw.rect(screen, orange, [window_x - 55, 30, 20,20])
    green_color = pygame.draw.rect(screen, green, [window_x - 55, 50, 20,20])
    purple_color = pygame.draw.rect(screen, purple, [window_x - 75, 10,20,20])
    lime_color = pygame.draw.rect(screen, lime, [window_x - 75, 30, 20, 20 ])
    pink_color = pygame.draw.rect(screen, pink, [window_x - 75, 50,20,20])
    eraser_button = pygame.draw.rect(screen, black,[380,10,50,50])
    color_rect  = [yellow_color, blue_color, red_color, black_color, orange_color, green_color,purple_color,lime_color,pink_color,eraser_button]
    list_of_color = [yellow, blue,red,black,orange, green, purple, lime, pink,white]
    
    return brush_list, color_rect, list_of_color

def draw_painting(paints):
    for i in range(len(paints)):
        pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])
square , circle = figure_button()
shape = 'rectangle'
while True:
    screen.fill(white)
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
   
    if left_click and mouse[1] > 70:
        painting.append((active_color, mouse, brush_size))
    if mouse[1] > 70:
        pygame.draw.circle(screen, active_color, mouse, brush_size)
    
    brushes, colors,list_colors = draw_menu(brush_size, active_color)
    
    figure = figure_button()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_figure = 0
                    brush_size = 20 - (i * 5)
                    shape = ''
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = list_colors[i]
        
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if figure[0].collidepoint(event.pos):
                brush_size = 0
                shape = 'rectangle'
            if figure[1].collidepoint(event.pos):
                brush_size = 0
                shape = 'circle'
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position_of_mouse = event.pos
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            size = (event.pos[0] - position_of_mouse[0], event.pos[1] - position_of_mouse[1])
        
    if shape == "rectangle": 
        pygame.draw.rect(screen, active_color, (position_of_mouse, size), 5)
    if shape == "circle":
        pygame.draw.circle(screen, active_color, position_of_mouse, max(abs(size[0]), abs(size[1])), 5)
        
    draw_painting(painting)
    figure_button()
    pygame.display.update()
    FPS.tick(60)