#библиотеки
import pygame
import random
import sys
#размер дисплея и квадратика
window_x = 800
window_y = 600
block_size = 40
#цветы
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
grey = (170, 180, 170)
yellow = (180,180,0)
#важные элементы
sec = 0
score = 0
snake_speed = 10

direction = 'RIGHT'
change_to = direction
#начало игры
pygame.init()
FPS = pygame.time.Clock() #игровая время
pygame.display.set_caption('nooloudy^s snake')
screen = pygame.display.set_mode((window_x , window_y))
#код который показывает заработанный очко во время игры
def ShowScore():
    
    self_font = pygame.font.SysFont('TImes New Roman', 20)
    self_surface = self_font.render('Score : ' +str(score), True, white)
    self_rect = self_surface.get_rect()
    self_rect.midtop = (60, 8)
    screen.blit(self_surface, self_rect)
#код который выводят о завершение игры
def game_over():
    
    screen.fill(black)
    self_font = pygame.font.SysFont('Times New Roman', 60)
    self_surface = self_font.render('Game Over', True, white)
    self_rect = self_surface.get_rect()
    self_rect.midtop = (window_x // 2 , window_y / 4)
    screen.blit(self_surface, self_rect)
#я здесь начал над создание змеи
class Snake():
    
    def __init__(self):
        self.x, self.y = block_size, block_size
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, block_size, block_size)
        self.body = [pygame.Rect(self.x - block_size, self.y, block_size, block_size)]
    
    def update(self):
        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir * block_size
        self.head.y += self.ydir * block_size
        self.body.remove(self.head)
#создание фрукты 
class Apple():
    
    def __init__(self):
        #здесь я исползую функцию от библиотеки рандом чтобы случайным образом призывет себе фрукты
        self.x = int(random.randint(0, window_x) / block_size) * block_size
        self.y = int(random.randint(0, window_y) / block_size) * block_size
        self.rect = pygame.Rect(self.x, self.y, block_size, block_size)
    
    def update(self):
        #рисование фрукты или добавлять на дисплей
        pygame.draw.rect(screen, red, self.rect)
#создание особый фрукты
class GoldApple():
    def __init__(self):
        #здесь тоже я исползую фукнция от библиотеки рандом чтобы случайным образом призыват себе особые фрукты
        self.x = int(random.randint(0, window_x) / block_size) * block_size
        self.y = int(random.randint(0, window_y) / block_size) * block_size
        self.rect = pygame.Rect(self.x, self.y, block_size, block_size)
    
    def update(self): 
        #рисование особый фрукты   
        pygame.draw.rect(screen, yellow, self.rect)
#создание сетки
def grid():
    
    for x in range(0, window_x, block_size):
        for y in range(0 ,window_y, block_size):
            
            rect = pygame.Rect(x,y,block_size,block_size)
            pygame.draw.rect(screen,grey, rect, 1)

snake = Snake()
apple = Apple()
goldapple = GoldApple()

time_event = pygame.USEREVENT
pygame.time.set_timer(time_event, 1000) # 1000мс у нас ровно на 1секунд 
flag = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == time_event:
            sec += 1
        if event.type == pygame.KEYDOWN: #создание над направлением змеи
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
        # я написал эту чтоб змея не разделялась на две направлений одновреммено и две клавиши не нажимали одновреммено
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    # движение змеи
    if direction == 'UP':
        snake.xdir = 0
        snake.ydir = -1
    if direction == 'DOWN':
        snake.xdir = 0
        snake.ydir = 1
    if direction == 'LEFT':
        snake.xdir = -1
        snake.ydir = 0
    if direction == 'RIGHT':
        snake.xdir = 1
        snake.ydir = 0
    screen.fill(black)
    snake.update()
    grid()#я призываю себе сетку 
    
    rand = random.randint(0,5)

    if flag:
        apple.update()
    if flag == False:
        goldapple.update()

    if sec > 2:
        if rand == 0:
            flag = False
            goldapple =GoldApple()
        else:
            flag = True
            apple = Apple()
        sec = 0
    if snake.head.x < 0 or snake.head.x > window_x - block_size:
        game_over()
    if snake.head.y < 0 or snake.head.y > window_y - block_size:
        game_over()
    
    
    pygame.draw.rect(screen, green, snake.head)
    
    for square in snake.body:
        pygame.draw.rect(screen ,green, square)
        if snake.head.x == square.x and snake.head.y == square.y:
            game_over()
        if square.x == apple.x and square.y == apple.y:
            apple = Apple()
        if square.x == goldapple.x and square.y == goldapple.y:
            goldapple = GoldApple()
    
    if snake.head.x == apple.x and snake.head.y == apple.y:
        score += 1
        snake_speed+=0.1
        snake.body.append(pygame.Rect(square.x, square.y, block_size, block_size))
        
        if rand == 0:
            flag = False
            goldapple = GoldApple()
        else:
            flag = True
            apple = Apple()
        sec = 0
    if snake.head.x == goldapple.x and snake.head.y == goldapple.y:
        score += 3
        snake_speed += 0.3
        snake.body.append(pygame.Rect(square.x, square.y, block_size, block_size))
        
        if rand == 0:
            flag = False
            goldapple = GoldApple()
        else:
            flag = True
            apple = Apple()
        sec = 0
    
    ShowScore()
    pygame.display.update()
    FPS.tick(snake_speed)