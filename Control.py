import pygame
import pygame_gui
import View
from View import *
from pygame.locals import K_ESCAPE, K_w, K_s, K_UP, K_DOWN
from Model.GameManager import Player1, Player2
from Model import GameManager

ui_manager = None
pongui = None


def listen():
    for event in pygame.event.get():
        ui_manager.process_events(event)
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == pongui.start_button:
                    pongui.set_game_type_selector()
                elif event.ui_element == pongui.exit_button:
                    GameManager.is_running = False
                elif event.ui_element == pongui.back_button:
                    pongui.set_main_menu()
                elif event.ui_element == pongui.one_player_button:
                    pongui.set_game_ui()
                    View.screen_mode = "game"
                    GameManager.game_mode = "single"
                    GameManager.play = True
                    GameManager.set_default()
                elif event.ui_element == pongui.two_player_button:
                    pongui.set_game_ui()
                    View.screen_mode = "game"
                    GameManager.game_mode = ""
                    GameManager.play =True
                    GameManager.set_default()

        if event.type == pygame.QUIT:
            GameManager.is_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                View.screen_mode = "menu"
                pongui.set_main_menu()
                GameManager.play = False
            elif event.key == K_w:
                Player1.UP = True
            elif event.key == K_s:
                Player1.DOWN = True
            elif event.key == K_UP:
                Player2.UP = True
            elif event.key == K_DOWN:
                Player2.DOWN = True

        if event.type == pygame.KEYUP:
            if event.key == K_w:
                Player1.UP = False
            elif event.key == K_s:
                Player1.DOWN = False
            elif event.key == K_UP:
                Player2.UP = False
            elif event.key == K_DOWN:
                Player2.DOWN = False
