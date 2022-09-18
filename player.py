import pygame

class Player():
    def __init__(self):
        self.speed = 3

        self.down_1 = pygame.image.load("assets/player/down_1.png")
        self.down_1 = pygame.transform.scale(self.down_1, (64, 64))
        self.down_2 = pygame.image.load("assets/player/down_2.png")
        self.down_2 = pygame.transform.scale(self.down_2, (64, 64))
        self.down_3 = pygame.image.load("assets/player/down_3.png")
        self.down_3 = pygame.transform.scale(self.down_3, (64, 64))
        self.tab_down = [self.down_1, self.down_2, self.down_3]

        self.left_1 = pygame.image.load("assets/player/left_1.png")
        self.left_1 = pygame.transform.scale(self.left_1, (64, 64))
        self.left_2 = pygame.image.load("assets/player/left_2.png")
        self.left_2 = pygame.transform.scale(self.left_2, (64, 64))
        self.left_3 = pygame.image.load("assets/player/left_3.png")
        self.left_3 = pygame.transform.scale(self.left_3, (64, 64))
        self.tab_left = [self.left_1, self.left_2, self.left_3]

        self.right_1 = pygame.image.load("assets/player/right_1.png")
        self.right_1 = pygame.transform.scale(self.right_1, (64, 64))
        self.right_2 = pygame.image.load("assets/player/right_2.png")
        self.right_2 = pygame.transform.scale(self.right_2, (64, 64))
        self.right_3 = pygame.image.load("assets/player/right_3.png")
        self.right_3 = pygame.transform.scale(self.right_3, (64, 64))
        self.tab_right = [self.right_1, self.right_2, self.right_3]

        self.up_1 = pygame.image.load("assets/player/up_1.png")
        self.up_1 = pygame.transform.scale(self.up_1, (64, 64))
        self.up_2 = pygame.image.load("assets/player/up_2.png")
        self.up_2 = pygame.transform.scale(self.up_2, (64, 64))
        self.up_3 = pygame.image.load("assets/player/up_3.png")
        self.up_3 = pygame.transform.scale(self.up_3, (64, 64))
        self.tab_up = [self.up_1, self.up_2, self.up_3]

        self.image = self.tab_down[0]
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 700

    def move_left(self):
        if self.rect.x >= 150:
            self.rect.x -= self.speed

    def move_right(self):
        if self.rect.x <= 642:
            self.rect.x += self.speed

    def move_up(self):
        if self.rect.y >= 150:
            self.rect.y -= self.speed

    def move_down(self):
        if self.rect.y <= 642:
            self.rect.y += self.speed