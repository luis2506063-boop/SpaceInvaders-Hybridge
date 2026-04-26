import pygame
import os
from ShipClass import Ship
from Enemy import Enemy, HEIGHT, WIDTH
from BulletClass import Bullet


PLAYER_IMAGE = pygame.image.load(os.path.join("img", "player_image.png"))
BULLET_IMAGE = pygame.image.load(os.path.join("img", "bullet_image.png"))

class Player(Ship):
    def __init__(self, x, y, x_speed, y_speed, health = 100):
        super(). __init__(x, y, health)
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.ship_img = PLAYER_IMAGE
        self.bullet_img = BULLET_IMAGE
        self.bullet_speed = -10
        self.max_health = health
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.creation_cooldown_counter = 0
        self.max_amount_bullets = 3

    def move(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.y > 0:
            self.y -= self.y_speed
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.y < HEIGHT - self.ship_img.get_height():
            self.y += self.y_speed
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.x < WIDTH - self.ship_img.get_width():
            self.x += self.x_speed
        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x > 0:
            self.x -= self.x_speed