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
pygame.display.set_caption("Rpg Miteux")

# Variables
player = Player()
map = Map()

# Animation player
pygame.time.set_timer(pygame.USEREVENT, 300)
counter = 0

'''Boucle Jeu'''
running = True
while running:
    print(pygame.Surface.get_at(screen, (player.rect.x, player.rect.y)))
    # Events
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
    if pressed[pygame.K_LEFT] or pressed[pygame.K_q]:
        player.image = player.tab_left[counter]
        player.move_left()
        if player.rect.x <= map.limit:
            map.move_right()

    if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
        player.image = player.tab_right[counter]
        player.move_right()
        if player.rect.x >= 792 - map.limit:
            map.move_left()

    if pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
        player.image = player.tab_down[counter]
        player.move_down()
        if player.rect.y >= 792 - map.limit:
            map.move_up()

    if pressed[pygame.K_UP] or pressed[pygame.K_z]:
        player.image = player.tab_up[counter]
        player.move_up()
        if player.rect.y <= map.limit:
            map.move_down()

    # Affichage
    if STAT == "menu":
        None
    if STAT == "spawn":
        # Fenêtre
        screen.blit(screen, (0, 0))
        screen.fill([0, 0, 0])
        # Map surface
        screen.blit(map.surface_collision_map, (-400, -1660))
        # Map collision
        screen.blit(map.collision_map, map.collision_map_rect)
        # Map neutre
        screen.blit(map.image, map.rect)
        # Player
        screen.blit(player.image, player.rect)
    clock.tick(60)
    pygame.display.flip()

pygame.quit()