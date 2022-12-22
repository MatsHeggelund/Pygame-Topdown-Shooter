import pygame
import math
from settings import display, tilesize

class Player(object):
    def __init__(self):
        self.width = tilesize
        self.height = tilesize
        self.rect = pygame.Rect(tilesize*3, tilesize*3, self.width, self.height)
        self.speed = 1
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
        self.direction = 1
        self.attackSpeed = 1/100 # 1 / projectiles per second

    def draw(self, sheet):
        self.image.blit(sheet, (0,0), (6*tilesize, 15*tilesize, self.width, self.height))
        #Rotate image surface based on player looking direction
        if self.direction == 1:
            self.image = pygame.transform.flip(self.image, False, False)
        elif self.direction == -1:
            self.image = pygame.transform.flip(self.image, True, False)

        display.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, walls, dx, dy):
        if dx != 0:
            self.collisionDetection(walls, dx, 0)
        if dy != 0:
            self.collisionDetection(walls, 0, dy)
    
    def collisionDetection(self, walls, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
