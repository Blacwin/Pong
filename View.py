import pygame
from constants import SEABLUE, BLACK
from Model.GameManager import Player1, Player2, Ball, block_list, ball_list

screen_mode = "menu"


def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)


class GameWindow:
    def __init__(self, screen_tuple_px):
        self.width_px = screen_tuple_px[0]
        self.width_px = screen_tuple_px[1]

        self.surface = pygame.display.set_mode(screen_tuple_px)

        self.erase_and_update()

    def draw(self):
        self.surface.fill(SEABLUE)
        pygame.draw.rect(self.surface, BLACK, [400, 0, 400, 600])
        if screen_mode == "menu":
            blit_alpha(self.surface, Player1.image, (Player1.rect.x, Player1.rect.y), 70)
            blit_alpha(self.surface, Player2.image, (Player2.rect.x, Player2.rect.y), 70)
            blit_alpha(self.surface, Ball.image, (Ball.rect.x, Ball.rect.y), 70)
        elif screen_mode == "game":
            block_list.draw(self.surface)
            ball_list.draw(self.surface)

    def update_caption(self, title):
        pygame.display.set_caption(title)

    def erase_and_update(self):
        self.surface.fill(BLACK)
        pygame.display.flip()

