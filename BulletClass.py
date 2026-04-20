

import pygame

#Clase Bullets(Balas)

class Bullet:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, speed):
        self.y += speed

    def colision(self, obj):
        offset = (int(self.x - obj.x), int(self.y - obj.y))
        return self.mask.overlap(obj.mask, offset)





