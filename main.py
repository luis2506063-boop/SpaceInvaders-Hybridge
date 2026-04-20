import pygame
from pygame import mixer
import os

#Vamos a agregar mas librerias.

pygame.init()

#Game Window
WIDTH, HEIGHT = 800, 600
TITLE = 'Space Invaders Hybridge'
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

#Background
BACKGROUND = pygame.image.load(os.path.join('img', 'background.png'))
ICON_IMAGE = pygame.image.load(os.path.join('img', 'title_icon.png'))
pygame.display.set_icon(ICON_IMAGE)

#player
PLAYER_IMAGE = pygame.image.load(os.path.join('img', 'player_image.png'))
BULLET_IMAGE = pygame.image.load(os.path.join('img', 'bullet_image.png'))

try:
    mixer.music.load(os.path.join('sounds', 'background_song.mp3'))
except:
    print('Music not found')
    pass
