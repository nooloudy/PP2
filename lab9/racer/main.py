#Библиотеки
import pygame, sys
from pygame.locals import *
import random, time
# здесь я указываю путь на необходимые мне материалы
path_to_red_car = "C://Users//GTA//Desktop//pp2//lab9//racer//red_car.png" 
path_to_blue_car = "C://Users//GTA//Desktop//pp2//lab9//racer//blue_car.png"
path_to_street = "C://Users//GTA//Desktop//pp2//lab9//racer//AnimatedStreet.png"
path_to_crash_song = "C://Users//GTA//Desktop//pp2//lab9//racer//crash.wav"
path_to_song = "C://Users//GTA//Desktop//pp2//lab9//racer//background.wav"
path_to_coin = "C://Users//GTA//Desktop//pp2//lab9//racer//coin.png"
path_to_coin_song = "C://Users//GTA//Desktop//pp2//lab9//racer//coin_song.mp3"
#я начинаю писать свою игру
pygame.init()

#Включаем игровой время 
FPS = 60
FramePerSec = pygame.time.Clock()

#Цветы которым я буду ползоваться
blue  = (0, 0, 255)
red   = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

#Необходимые значание
window_x  = 400
window_y = 600
SPEED = 5
SPEED2 = 4
SCORE = 0
SCORE2=0

background = pygame.image.load(path_to_street)

#Здесь я генерироваль белую экран
screen = pygame.display.set_mode((window_x, window_y))
screen.fill(white)
pygame.display.set_caption("nooloudy^s racer")


font_small = pygame.font.SysFont("times new roman", 20)


#Включаем свою игровую музыку
song = pygame.mixer.Sound(path_to_song).play(-1)
#Я создал свою первую персонаж который будут мещать мне во время передвижение в игре
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path_to_red_car)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,window_x-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, window_x - 40), 0)
# Код когда игра будут прекращен
def game_over():
    screen.fill(black)
    self_font = pygame.font.SysFont('Times new roman',60)
    
    self_surface = self_font.render(' Game Over ', True, white)
    
    self_rect = self_surface.get_rect()
    
    self_rect.midtop = (window_x // 2, window_y // 2 )
    
    screen.blit(self_surface, self_rect) 
# здесь я создал свою вторую персонаж главный герой
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path_to_blue_car)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < window_x:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
# я создал монеты который во время движений появляется случайно и мне надо их собирать
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(path_to_coin)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, window_x - 40), 0)

    def move(self):
        global SCORE2
        self.rect.move_ip(0, SPEED2)
        if self.rect.top > window_y:
            self.kill()
        elif pygame.sprite.spritecollide(self, players, False):
            pygame.mixer.Sound(path_to_coin_song).play()
            self.kill()
            rand = random.randint(0,4)
            if rand == 0:
                SCORE2 += 5

            if rand == 3 or rand == 1:
                SCORE2 +=2

            if rand == 2 or rand == 4:
                SCORE2 +=1




#настройка спрайтов
P1 = Player()
E1 = Enemy()

#Создание групповых спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
players = pygame.sprite.Group()
players.add(P1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
coins = pygame.sprite.Group()

#Создание новыx event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
ADD_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_COIN, 2000)

#Работа с интерфейсом
while True:

    #Настроивать важных event
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.3
            SPEED2 += 0.25
        elif event.type == ADD_COIN:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, black)
    screen.blit(scores, (10,10))
    scores2 = font_small.render(str(SCORE2), True, black)
    screen.blit(scores2, (10,30))

    #Повторно нарисовать спрайтов
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)
    
        
    if SCORE2 % 10 == 1:
        SPEED += 0.01    

    #момент в которым главный геров и красная машина столькивается
    if pygame.sprite.spritecollideany(P1, enemies):
        song.pause()
        pygame.mixer.Sound(path_to_crash_song).play()
        time.sleep(1)

        game_over()

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)

#Осымен бәрі бітті ехууу!!!!!