import pygame
from constants import *
import random
import globals

#Tamano del sprite original del enemigo, si usas otro, pon aqui su tamano
ORIGINAL_SIZE=(60,154)
MIN_WIDTH = 15
MAX_WIDTH = 25

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()

        #Tamano aleatorio
        self.width = random.randint(MIN_WIDTH, MAX_WIDTH)
        self.height = (self.width/ORIGINAL_SIZE[0])*ORIGINAL_SIZE[1]

        self.surf = pygame.image.load('sprites/missile.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (self.width,self.height))
        self.mask = pygame.mask.from_surface(self.surf)

        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, SCREEN_WIDTH),
                random.randint(-100, -20)
            )
        )
        
        #Velocidad semi-aleatoria, aumenta con la velocidad global del juego
        self.speed = (random.randint(1,2) / 10 ) * (1 + (globals.game_speed/2))

    def update(self, delta_time):
        self.rect.move_ip(0, self.speed * delta_time)
        self.mask = pygame.mask.from_surface(self.surf)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()