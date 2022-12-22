import pygame
import time
import math
from settings import display, tilesize

enemies = []
spawnrate = 0.1

class Enemy(object):
    def __init__(self, x, y):
        enemies.append(self)
        self.x = x
        self.y = y
        self.width = tilesize
        self.height = tilesize
        self.image = pygame.image.load("sprites/enemy.png")
        self.rect = self.image.get_rect()
        self.destroy = False
        self.health = 7
        self.speed = 0.4
        self.enemy_hit_timer = 2.0
        self.enemy_hit_clock = time.time()
        self.enemy_hit_time = time
        self.detectRadius = 5*tilesize
        self.direction = 1
    
    def update(self, px, py):
        if self.destroy == False:
            dx = px - self.rect.x
            dy = py - self.rect.y
            #angle between self and player
            angle = math.atan2(dy, dx)
            #get the distance from the player
            distance_from_player = math.sqrt((self.x - px)**2 + (self.y - py)**2)

            #Change which way enemy is facing based on position relative to players position
            if px > self.x and distance_from_player < self.detectRadius:
                self.direction = 1
            elif px < self.x and  distance_from_player < self.detectRadius:
                self.direction = -1

            if distance_from_player < self.detectRadius:
                #If the enemy is within range of the player, move
                self.x += self.speed * math.cos(angle)
                self.y += self.speed * math.sin(angle)

            self.draw()
            self.getHit()
        
    def draw(self):
        self.rect.x = self.x
        self.rect.y = self.y
        #flip sprite based on direction
        if self.direction == 1:
            self.image = pygame.transform.flip(self.image, False, False)
        elif self.direction == -1:
            self.image = pygame.transform.flip(self.image, True, False)

        display.blit(self.image, (self.rect.x, self.rect.y))
    
    def getHit(self):
        #if timer surpasses 0.5 seconds, revert to original image
        if self.enemy_hit_timer > 0.5:
            self.image = pygame.image.load("sprites/enemy.png")
        else: 
            #else, update timer. Set image to enemy_hit
            self.enemy_hit_time = time.time()
            self.enemy_hit_timer += (self.enemy_hit_time-self.enemy_hit_clock)
            self.enemy_hit_clock = self.enemy_hit_time
            self.image = pygame.image.load("sprites/enemy_hit.png")

