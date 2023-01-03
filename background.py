import pygame
from constants import *

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()

        self.surf = pygame.image.load("sprites/Blue Nebula 8 - 1024x1024.png")
        background_width = SCREEN_WIDTH * 2 #doble ancho
        background_height = (background_width/self.surf.get_width())*self.surf.get_height()
        self.surf = pygame.transform.scale(self.surf, (background_width, background_height))
        self.rect = self.surf.get_rect(
            bottomleft=(0,SCREEN_HEIGHT)
        )
        #Usamos 2 surface para hacer un buen loop del fondo
        #Se mueven juntos y cuando uno desaparece de pantalla se mueve
        #hasta abajo, y asi se van repitiendo
        self.surf2 = self.surf
        self.rect2 = self.surf2.get_rect(
            bottomleft=self.rect.topleft
        )
        self.ypos = 0
        self.ypos2 = background_height-SCREEN_HEIGHT

    def update(self, delta_time):
        self.ypos += .05 * delta_time
        self.ypos2 += .05 * delta_time
        self.rect.y = int(self.ypos)
        self.rect2.y = int(self.ypos2)
        if self.rect.y > SCREEN_HEIGHT:
            self.ypos = self.rect2.y - self.surf2.get_height()
            self.rect.y = self.ypos
        if self.rect2.y > SCREEN_HEIGHT:
            self.ypos2 = self.rect.y - self.surf.get_height()
            self.rect2.y = self.ypos2

    def render(self, dest):
        dest.blit(self.surf, self.rect)
        dest.blit(self.surf2, self.rect2)