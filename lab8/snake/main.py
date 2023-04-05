import pygame
import random
import sys
snake_speed = 10
 
window_x = 800
window_y = 600
 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
 
pygame.init()
#Я тут кароч создал интерфейс и дал ему название
screen = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('nooloudy^s snake')
# Тут я начал взмаимодействия с игровом времени
FPS = pygame.time.Clock()
# Ну здесь я создал свой игровой персонаж
snake_position = [100, 50]

snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# С помощью библиотеки random сгенерирую яблока
apple_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
 
apple_spawn = True
 
direction = 'RIGHT'
change_to = direction

score = 0
level = 0
#На этой функции я создал счетчик на очко
def show_score():

    self_font = pygame.font.SysFont('Times new roman', 20)

    self_surface = self_font.render('Score : ' + str(score), True, black)

    self_rect = self_surface.get_rect()

    self_rect.midtop = (50, 7)

    screen.blit(self_surface, self_rect)
# А на этой функции я создал счетчик на уровень который мой персонаж поднимается
def show_level():
    
    self_font = pygame.font.SysFont('Times new roman',20)
    
    self_surface = self_font.render('Level : ' + str(level), True, black)
    
    self_rect = self_surface.get_rect()
    
    self_rect.midtop = (50, 30)
    
    screen.blit(self_surface, self_rect)
# функция которая отвечает что игра закончилось и показывает все заработанные достижение в игре
def game_over():
    
    screen.fill(black)
    
    self_font = pygame.font.SysFont('times new roman', 50)

    self_surface = self_font.render('Your Score is : ' + str(score), True, red)
    self_surface2 = self_font.render('Your Level is : ' + str(level), True, red)

    self_rect = self_surface.get_rect()
    
    self_rect2 = self_surface2.get_rect()
    
    self_rect.midtop = (window_x / 2, window_y / 4)
    
    self_rect2.midtop = (window_x // 2, window_y // 2)
    
    screen.blit(self_surface, self_rect)
    
    screen.blit(self_surface2, self_rect2)
    
    pygame.display.flip()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #здесь я указываю направление чтоб мой персонаж двигалась по командование
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
# я написал эту чтоб змея не разделялась на две направлений одновреммено и две клавиши не нажимали одновреммено
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
#перемещение змеи
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
# Сначала механизм роста тела змеи
# если мой персонаж касается до яблока добавляеть очки и он будут увеличить свой размер
# если он касается 5 раз то он улучшается на 1 уровень
# если он мой персонаж касается до яблока то яблока будут сново генерироваться
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == apple_position[0] and snake_position[1] == apple_position[1]:
        score += 10
        apple_spawn = False
        if score % 50 == 0:
            snake_speed += 1
            level += 1
    else:
        snake_body.pop()
         
    if not apple_spawn:
        apple_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
         
    apple_spawn = True
    screen.fill(white)
     
    for pos in snake_body:
        pygame.draw.rect(screen, red,pygame.Rect(pos[0], pos[1], 10, 10))
    
    pygame.draw.rect(screen, red, pygame.Rect(apple_position[0], apple_position[1], 10, 10))
#здесь я указываю в каком положение игра будет прекращена
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score()
    show_level()

    pygame.display.update()

    FPS.tick(snake_speed)