import pygame
from constants import WHITE, LIGHTGREEN, BLACK


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, diameter=20):
        super().__init__()
        self.x = 390
        self.y = 290
        self.image = pygame.Surface([diameter, diameter])
        self.image.set_colorkey(WHITE)
        self.image.fill(BLACK)
        pygame.draw.circle(self.image, LIGHTGREEN, (10, 10), 10)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.speed_x = 1
        self.speed_y = 1

        self.cont_x = 0
        self.cont_y = 0

        self.switch = False

    def movement(self):
        if self.rect.x > 780 or self.rect.x < 5:
            self.speed_x = self.speed_x * -1
        if self.rect.y > 580 or self.rect.y < 5:
            self.speed_y = self.speed_y * -1
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def stop_the_ball(self):
        if not self.switch:
            self.switch = True
            self.cont_x = self.speed_x
            self.speed_x = 0
            self.cont_y = self.speed_y
            self.speed_y = 0

    def start_the_ball(self):
        if self.switch:
            self.speed_x = self.cont_x
            self.speed_y = self.cont_y
            self.switch = False

    def reload(self):
        self.rect.x = self.x
        self.rect.y = self.y