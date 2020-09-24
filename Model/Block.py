import pygame
from constants import WHITE, LIGHTGREEN


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, name, width=10, height=100):

        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name
        self.image = pygame.Surface([width, height])
        self.image.set_colorkey(WHITE)
        self.image.fill(LIGHTGREEN)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.change_x = 5
        self.change_y = 5

        self.UP = False
        self.DOWN = False

    def move(self):
        if self.UP:
            if self.rect.y > 5:
                self.rect.y -= 1
        if self.DOWN:
            if self.rect.y < 595 - self.height:
                self.rect.y += 1

    def reset(self):
        self.rect.y = self.y
        self.rect.x = self.x
        self.UP, self.DOWN = False, False
