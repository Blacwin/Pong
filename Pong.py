import pygame
import pygame_gui

import Control
import View
from GUI import PonGUI
from Model import GameManager
from Model.GameManager import Player1, Player2, Computer
from constants import SIZE


def main():
    pygame.init()

    game_window = View.GameWindow(SIZE)
    game_window.update_caption("Pong")

    Control.ui_manager = pygame_gui.UIManager(SIZE)
    Control.pongui = PonGUI(Control.ui_manager)

    ball = GameManager.Ball

    mode = None

    player1_score = 0
    player2_score = 0

    clock = pygame.time.Clock()

    framer_limit = 400

    # ------Mainloop-------
    while GameManager.is_running:
        dt_s = float(clock.tick(framer_limit) * 1e-3)

        Control.listen()

        if mode != View.screen_mode:
            timer = 0
            player1_score = 0
            player2_score = 0
        mode = View.screen_mode

        ball.movement()
        for block in GameManager.block_list:
            block.move()

        if ball.rect.x <= 28:
            if Player1.rect.y - 10 <= ball.rect.y <= Player1.rect.y + 100:
                ball.speed_x = ball.speed_x * -1
            else:
                player2_score += 1
                ball.reload()
        elif ball.rect.x >= 750:
            if Player2.rect.y - 10 <= ball.rect.y <= Player2.rect.y + 100:
                ball.speed_x = ball.speed_x * -1
            else:
                player1_score += 1
                ball.reload()

        if GameManager.play:
            Control.pongui.update_scoreboards(player1_score, player2_score)
            if GameManager.game_mode == "single":
                Computer.play_to_player()
        else:
            Computer.play_to_yourself()

        game_window.draw()

        Control.ui_manager.update(dt_s)
        Control.ui_manager.draw_ui(game_window.surface)
        pygame.display.flip()


if __name__ == "__main__":
    main()
