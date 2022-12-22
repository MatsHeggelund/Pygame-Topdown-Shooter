import time
import pygame
from player import *
from enemy import *
from tilemap import *
from cursor import *
from weapon import *
from projectile import *
from settings import *

pygame.init()

player = Player() 
tilemap = Tilemap()
cursor = Cursor()
weapon = Weapon()
sprite_sheet_image = pygame.image.load("sprites/spritesheet.png").convert_alpha()
pygame.mouse.set_visible(False)

#Cursor timer variables
cursor_boolswitch = False
cursor_timer = 0.0
cursor_clock = time.time()
cursor_time = time

#enemy spawnrate variables
enemy_boolswitch = False
enemy_timer = 0.0
enemy_clock = time.time()
enemy_time = time


def draw():
    for wall in tiles:
        wall.draw(sprite_sheet_image) #draw floor tiles

    player.draw(sprite_sheet_image) #draw player

    weapon.x = player.rect.x 
    weapon.y = player.rect.y + player.height/3
    weapon.draw(mx/zoomSize, my/zoomSize) # draw weapon

    for enemy in enemies: #draw and update enemies
        enemy.update(player.rect.x, player.rect.y)

    for projectile in projectiles: #draw and update projectiles
        projectile.update(walls, enemies)

    cursor.draw(mx/zoomSize, my/zoomSize) # draw cursor

def getCursorClick():
    global cursor_timer, cursor_clock, cursor_time, cursor_boolswitch
    if cursor_timer > player.attackSpeed:
        cursor_boolswitch = True
    else:
        cursor_time = time.time()
        cursor_timer += (cursor_time-cursor_clock)
        cursor_clock = cursor_time

    if cursor_boolswitch:
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            Projectile(weapon.rect.x, weapon.rect.y, mx/zoomSize, my/zoomSize, 0)
            #Triple shot
            #Projectile(weapon.rect.x, weapon.rect.y, mx/zoomSize, my/zoomSize, 5)
            #Projectile(weapon.rect.x, weapon.rect.y, mx/zoomSize, my/zoomSize, -5)
            #Quintuple shot
            #Projectile(weapon.rect.x, weapon.rect.y, mx/zoomSize, my/zoomSize, 3)
            #Projectile(weapon.rect.x, weapon.rect.y, mx/zoomSize, my/zoomSize, -3)
 
            cursor_boolswitch = False
            cursor_clock = time.time()
            cursor_timer = 0.0

def spawnEnemyOnTimer():
    global enemy_timer, enemy_clock, enemy_time, enemy_boolswitch
    if enemy_timer > spawnrate:
        enemy_boolswitch = True
    else:
        enemy_time = time.time()
        enemy_timer += (enemy_time-enemy_clock)
        enemy_clock = enemy_time

    if enemy_boolswitch:
        pos = tilemap.getRandomFloorTile()
        #Get enemy spawn position distance from players current position
        distance_from_player = math.sqrt((pos[0] - player.rect.x)**2 + (pos[1] - player.rect.y)**2)
        #if the position isnt inside a wall, andif the enemy spawns far enough away from the player, make it
        if pos != (0, 0) and distance_from_player > 3*tilesize:
            Enemy(pos[0], pos[1])
        enemy_boolswitch = False
        enemy_clock = time.time()
        enemy_timer = 0.0

running = True
while running:
    #get position of cursor
    mx, my = pygame.mouse.get_pos()

    # Run draw function
    draw()

    #Change player look direction based on cursor position and player position
    if mx/zoomSize > player.rect.x:
        player.direction = 1
    else: 
        player.direction = -1

    # Exit the game if user exits
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
    
    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move(walls, -player.speed, 0)
    if key[pygame.K_d]:
        player.move(walls, player.speed, 0)
    if key[pygame.K_w]:
        player.move(walls, 0, -player.speed)
    if key[pygame.K_s]:
        player.move(walls, 0, player.speed)

    # Handle cursor input delay based on player attack speed  
    getCursorClick()

    spawnEnemyOnTimer()
    
    # Display surface on the screen and update
    clock.tick(60)
    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0,0))
    pygame.display.update()
