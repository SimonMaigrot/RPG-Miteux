import pygame
from player import Player
from map import Map
pygame.init()

# Important
WIDTH = 896
HEIGHT = 896
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
STAT = "spawn"

# Variables
player = Player()
map = Map()

# Animation player
pygame.time.set_timer(pygame.USEREVENT, 300)
counter = 0

'''Boucle Jeu'''
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.USEREVENT:
            counter += 1

    if counter >= 3:
        counter = 0
    # Movement
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        player.image = player.tab_left[counter]
        player.move_left()
        if player.rect.x <= map.limit:
            map.move_right()

    if pressed[pygame.K_RIGHT]:
        player.image = player.tab_right[counter]
        player.move_right()
        if player.rect.x >= 896 - map.limit:
            map.move_left()

    if pressed[pygame.K_DOWN]:
        player.image = player.tab_down[counter]
        player.move_down()
        if player.rect.y >= 792 - map.limit:
            map.move_up()

    if pressed[pygame.K_UP]:
        player.image = player.tab_up[counter]
        player.move_up()
        if player.rect.y <= map.limit:
            map.move_down()

    # Affichage
    if STAT == "menu":
        None
    if STAT == "spawn":
        screen.blit(screen, (0, 0))
        screen.fill([0, 0, 0])
        screen.blit(map.image, map.rect) 
        screen.blit(player.image, player.rect)
    clock.tick(60)
    pygame.display.flip()

pygame.quit()