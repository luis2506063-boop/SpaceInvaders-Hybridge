import pygame
import random
import os
from ShipClass import Ship

current_dir = os.path.dirname(__file__)

WIDTH, HEIGHT = 800, 600

# Clase Enemy

class Enemy(Ship):
    COLOR = {
        'blue': ('enemy_blue_image.png', 'shot_blue.png'),
        'green': ('enemy_green_image.png', 'shot_green.png'),
        'purple': ('enemy_purple_image.png', 'shot_purple.png'),
    }

    def __init__(self, speed, x=50, y=50, color='blue', health=100):
        super().__init__(x, y, health)
        ship_file, bullet_file = self.COLOR[color]
        self.ship_img = pygame.image.load(os.path.join(current_dir, 'img', ship_file))
        self.bullet_img = pygame.image.load(os.path.join(current_dir, 'img', bullet_file))
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.speed = speed

    def move(self):
        self.y += self.speed

    def create(self, amount):
        enemies = []
        for _ in range(amount):
            enemy = Enemy(x=random.randrange(20, WIDTH - self.ship_img.get_width() - 20),
                         y=random.randrange(-1000, -100),
                         color = random.choice(['blue', 'green', 'purple']),
                         speed = self.speed)
            enemies.append(enemy)
        return enemies

    def increase_speed(self):
        self.speed *= 1.1

def main():
    pygame.init()
    run = True
    clock = pygame.time.Clock()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    enemies = Enemy(1).create(5)

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for enemy in enemies:
            enemy.move()

        WIN.fill((0,0,0))
        for enemy in enemies:
            enemy.draw(WIN)
        pygame.display.update()

    pygame.quit()