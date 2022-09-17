import pygame

class Map(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("assets/map/map_default_layer.png")
        self.image = pygame.transform.rotozoom(self.image, 0.0, 2.0)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = -500
        self.speed = 3
        self.limit = 60

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed