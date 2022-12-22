import pygame
from settings import display, tilesize

class Cursor(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = tilesize*2
        self.height = tilesize*2
        self.image = pygame.image.load("sprites/cursor.png")

    def draw(self, mx, my):
        self.x = mx
        self.y = my
        display.blit(self.image, (mx-self.width/4, my-self.height/4))
