import pygame
from Model.Block import Block
from Model.Ball import Ball
from Model.Computer import Computer
from constants import SCREEN_WIDTH

Player1 = Block(20, 200, "Player1")
Player2 = Block(SCREEN_WIDTH - 30, 200, "Player2")
Ball = Ball(390, 290, 20)
Computer = Computer(Player1, Player2, Ball)

block_list = pygame.sprite.Group()
ball_list = pygame.sprite.Group()

block_list.add(Player1)
block_list.add(Player2)
ball_list.add(Ball)

play = False
game_mode = ""
is_running = True


def set_default():
    Player1.reset()
    Player2.reset()
    Ball.reload()
