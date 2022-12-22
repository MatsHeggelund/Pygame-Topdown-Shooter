import pygame
from random import randint
from settings import tilesize, display

walls = [] # List to hold the walls
tiles = []

class Tilemap(object):
    def __init__(self):
        self.map = [
                    [10,2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,11],
                    [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5],
                    [4, 0, 0, 0, 0, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
                    [4, 0, 0, 0, 6, 5,10,13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
                    [4, 0, 0, 0,12, 2,13, 1, 0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 0, 5],
                    [4, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 6, 5, 4, 0, 0, 0, 5],
                    [4, 0, 0, 0, 6, 6, 6, 6, 0, 0, 0, 0, 0, 5, 3, 4, 0, 0, 0, 5],
                    [4, 0, 0, 0, 5, 3, 3, 4, 0, 0, 0, 0, 0,12, 2,13, 0, 0, 0, 5],
                    [4, 0, 0, 0,12, 2, 2,13, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 5],
                    [4, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
                    [4, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5],
                    [8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9]
                ]
        self.mapHeight = len(self.map)
        self.mapWidth = len(self.map[0])

    def getRandomFloorTile(self):
        row = randint(0, self.mapHeight-1)
        col = randint(0, self.mapWidth-1)
        if self.map[row][col] == 0:
            return col*tilesize, row*tilesize
        else:
            return 0, 0

class Wall(object):
    def __init__(self, x, y, index):
        tiles.append(self)
        self.x = x
        self.y = y
        self.width = tilesize
        self.height = tilesize
        self.rect = pygame.Rect(self.x, self.y, tilesize, tilesize)
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
        self.index = index
        if self.index != 0 and self.index != 1 and self.index != 6:
            walls.append(self)
    
    def draw(self, sheet):
        if self.index == 0: # Floor tile
            self.chooseSprite(sheet, 2, 3)

        if self.index == 1: # Wall Front
            self.chooseSprite(sheet, 1, 1)

        if self.index == 2: # Wall Block Top
            self.chooseSprite(sheet, 4, 6)
            self.chooseSprite(sheet, 0, 0)

        if self.index == 3: # Wall Block
            self.chooseSprite(sheet, 4, 6)

        if self.index == 4: # Wall Block Left
            self.chooseSprite(sheet, 4, 6)
            self.chooseSprite(sheet, 16, 2)

        if self.index == 5: # Wall Block Right
            self.chooseSprite(sheet, 4, 6)
            self.chooseSprite(sheet, 18, 2)

        if self.index == 6: # Wall Top
            self.chooseSprite(sheet, 2, 3)
            self.chooseSprite(sheet, 0, 0)

        if self.index == 7: # Wall Block Front
            self.chooseSprite(sheet, 1, 1)

        if self.index == 8: # Wall Block LeftFront
            self.chooseSprite(sheet, 4, 6)
            self.chooseSprite(sheet, 16, 3)

        if self.index == 9: # Wall Block RightFront
            self.chooseSprite(sheet, 4, 6)
            self.chooseSprite(sheet, 18, 3)

        if self.index == 10: # Wall TopLeft Corner
            self.chooseSprite(sheet, 4, 6)
            self.chooseSprite(sheet, 16, 0)

        if self.index == 11: # Wall TopRight Corner
            self.chooseSprite(sheet, 4, 6)
            self.chooseSprite(sheet, 18, 0)

        if self.index == 12: # Wall BottomLeft L Corner
            self.chooseSprite(sheet, 4, 6)
            self.chooseSprite(sheet, 19, 2)

        if self.index == 13: # Wall BottomRight L Corner
            self.chooseSprite(sheet, 4, 6)
            self.chooseSprite(sheet, 20, 2)
            
        display.blit(self.image, (self.x, self.y))

    def chooseSprite(self, sheet, xpos, ypos):
        self.image.blit(sheet, (0,0), (xpos*tilesize,ypos*tilesize, self.width, self.height))

#Create the walls based on tilemap
for row in range(Tilemap().mapHeight):
    for col in range(Tilemap().mapWidth):
        for index in range(max(Tilemap().map[row])+1):
            if Tilemap().map[row][col] == index:
                Wall(col*tilesize, row*tilesize, index)
