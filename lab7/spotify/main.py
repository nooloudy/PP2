import pygame, sys
import os
from pygame.locals import *
import random


pygame.init()
cnt = 0
musics = []
dir_path = r"C:\Users\GTA\Desktop\pp2\lab7\spotify\music"
os.chdir(dir_path)

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        musics.append(path)

pygame.mixer.music.load(musics[cnt])
pygame.mixer.music.play()

weidht = 800
height = 500

display = pygame.display.set_mode((weidht,height))
pygame.display.set_caption('nooloudy')

stop_bool = False
next_bool = False
back_bool = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                stop_bool = not stop_bool
                if stop_bool:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            if event.key == pygame.K_RIGHT:
                next_bool = True
                cnt+=1
                if next_bool:
                    if cnt < len(musics):
                        pygame.mixer.music.load(musics[cnt])
                        pygame.mixer.music.play(0)
                    else:
                        pygame.mixer.music.load(musics[cnt])
                        pygame.mixer.music.play(0)
                        
            if event.key == pygame.K_LEFT:
                back_bool = True
                if back_bool:
                    if cnt > 0 and cnt < len(musics):
                        pygame.mixer.music.load(musics[cnt-1])
                        pygame.mixer.music.play(0)
                        cnt-=1
                elif cnt == 0:
                    pygame.mixer.music.load(musics[len(musics)])
                    pygame.mixer.music.play(0)
    pygame.display.flip()

print("That's all")

