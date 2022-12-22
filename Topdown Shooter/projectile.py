import pygame
import math
from settings import display, tilesize

projectiles = []

class Projectile(object):
    def __init__(self, x, y, mx, my, offset_angle):
        projectiles.append(self)
        self.x = x
        self.y = y
        self.width = tilesize/2
        self.height = tilesize/2
        self.image = pygame.image.load("sprites/projectile.png")
        self.rect = self.image.get_rect()
        self.mx = mx
        self.my = my
        self.speed = 2
        self.dx = self.mx - self.x
        self.dy = self.my - self.y
        self.offset_angle = offset_angle
        self.destroy = False
        #Handle projectile animation on impact
        self.animation = [  pygame.image.load("sprites/projectileImpact/projectileImpact1.png"),
                            pygame.image.load("sprites/projectileImpact/projectileImpact2.png"),
                            pygame.image.load("sprites/projectileImpact/projectileImpact3.png"),
                            pygame.image.load("sprites/projectileImpact/projectileImpact4.png"),
                            pygame.image.load("sprites/projectileImpact/projectileImpact5.png"),
                            pygame.image.load("sprites/projectileImpact/projectileImpact6.png"),
                            pygame.image.load("sprites/projectileImpact/projectileImpact7.png"),
                            pygame.image.load("sprites/projectileImpact/projectileImpact8.png")]
        self.animationTick = 0
        self.animationIndex = 0
    
    def update(self, walls, enemies):
        if self.speed > 0:
            angle = math.atan2(self.dy, self.dx)
            self.x += self.speed * math.cos(angle + self.offset_angle/30)
            self.y += self.speed * math.sin(angle + self.offset_angle/30)
            self.draw()
            self.collisionDetection(walls, enemies, angle)
        else:
            if self.animationTick == 3:
                if self.animationIndex < 8:
                    self.image = self.animation[self.animationIndex]
                else:
                    self.destroy = True
                    self.x = 10000
                self.animationTick = 0
                self.animationIndex += 1
            self.animationTick += 1
        if not self.destroy:
            self.draw()

    def draw(self):
        self.rect.x = self.x
        self.rect.y = self.y
        correction_angle = 45

        angle = math.degrees(math.atan2(-self.dy, self.dx)) - correction_angle

        rot_image = pygame.transform.rotate(self.image, angle)
        rot_image_rect = rot_image.get_rect(center = self.rect.center)

        display.blit(rot_image, rot_image_rect.topleft)
                    
    def collisionDetection(self, walls, enemies, angle):
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                self.speed = 0

        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                self.speed = 0
                enemy.health -= 1
                #if enemy dies, remove it
                if enemy.health < 1:
                    enemy.destroy = True
                    enemy.rect.x = 10000

                #else, if it is still alive, apply knockback and change sprite
                elif enemy.destroy == False:
                    enemy.getHit()
                    enemy.x += 12*enemy.speed * math.cos(angle)
                    enemy.y += 12*enemy.speed * math.sin(angle)
                    enemy.enemy_hit_timer = 0.0


        