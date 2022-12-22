import pygame

pygame.display.set_caption("Aspen")
tilesize = 16
zoomSize = 6
clock = pygame.time.Clock()
win_width = 20*tilesize*zoomSize
win_height = 12*tilesize*zoomSize
WINDOW_SIZE = (win_width, win_height)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
display = pygame.Surface((win_width/zoomSize, win_height/zoomSize))


