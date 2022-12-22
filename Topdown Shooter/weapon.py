import pygame
import math
from settings import display, tilesize

class Weapon(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = tilesize
        self.height = tilesize
        self.image = pygame.image.load("sprites/weapon.png")
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.angle = 0
    
    def draw(self, mx, my):
        self.rect.x = self.x
        self.rect.y = self.y
        correction_angle = 45
        
        dx, dy = mx - self.rect.centerx, self.rect.centery - my
        self.angle = math.degrees(-math.atan2(-dy, dx)) - correction_angle

        rot_image = pygame.transform.rotate(self.image, self.angle)
        rot_image_rect = rot_image.get_rect(center = self.rect.center)

        display.blit(rot_image, rot_image_rect.topleft)
