import pygame

class Map(pygame.sprite.Sprite):
    def __init__(self):
        # Map neutre
        self.image = pygame.image.load("assets/map/map_default_layer.png")
        self.image = pygame.transform.scale(self.image, (2560, 2560))
        self.rect = self.image.get_rect()
        self.rect.x = -400
        self.rect.y = -1660
        # Map collision
        self.collision_map = pygame.image.load("assets/map/map_colorless_layer.png")
        self.collision_map = pygame.transform.scale(self.collision_map, (2560, 2560))
        self.collision_map_rect = self.collision_map.get_rect()
        self.collision_map_rect.x = -400
        self.collision_map_rect.y = -1660
        # Map surface
        self.surface_collision_map = pygame.Surface((2560, 2560))
        # Divers
        self.speed = 3
        self.limit = 150

    def move_left(self):
        self.rect.x -= self.speed
        self.collision_map_rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed
        self.collision_map_rect.x += self.speed

    def move_up(self):
        self.rect.y -= self.speed
        self.collision_map_rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed
        self.collision_map_rect.y += self.speed