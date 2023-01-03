import pygame
from constants import *

#Tamano original del sprite del cohete, cambialo aqui si mueves el sprite
ORIGINAL_SIZE = (272,512)
WIDTH = 50
HEIGHT = (WIDTH/ORIGINAL_SIZE[0])*ORIGINAL_SIZE[1]
SPEED = 1

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        self.surf = pygame.image.load("sprites/rocket.png").convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (WIDTH,HEIGHT))
        self.update_mask()

        #Guardar para manejar bien las rotaciones
        self.original_surf = self.surf 
        self.lastRotation = 0
        
        self.rect = self.surf.get_rect(
            center=(
                (SCREEN_WIDTH/2) - (WIDTH/2),
                (SCREEN_HEIGHT - HEIGHT)
            )
        )

    def update(self, movement, delta_time):
        self.rect.move_ip(SPEED * movement * delta_time, 0)

        #Rotacion. Quiza deberia usar directamente el angulo de la cara pero eso se me ocurrio despues hehohoh
        rotation = 45 * movement * -1
        self.surf = pygame.transform.rotate(self.original_surf, self.lerp(self.lastRotation, rotation, .5))
        self.lastRotation = rotation
        self.update_mask()

        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH: self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0: self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT: self.rect.bottom = SCREEN_HEIGHT

    def lerp(self, a: float, b: float, t: float) -> float:
        #Funcion copiada sin escrupulos
        return (1 - t) * a + t * b

    def update_mask(self):
        #Mascara tiene un 80% del tamano para 'perdonar' al jugador en ciertas colisiones
        maskSurface = self.surf
        maskSurface = pygame.transform.scale(maskSurface, (WIDTH*.8,HEIGHT*.8))
        self.mask = pygame.mask.from_surface(maskSurface)