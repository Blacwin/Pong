import pygame
import pygame_gui


class PonGUI:
    def __init__(self, manager):
        self.manager = manager
        self.start_button = self.get_button((300, 200, 200, 50),"Start")
        self.exit_button = self.get_button((300, 400, 200, 50), "Exit")
        self.one_player_button = self.get_button((300, 200, 200, 50), "One Player")
        self.two_player_button = self.get_button((300, 300, 200, 50), "Two Player")
        self.back_button = self.get_button((300, 400, 200, 50), "Back")
        self.player_one_scoreboard_label = self.get_label((200, 10, 100, 30), "0")
        self.player_two_scoreboard_label = self.get_label((600, 10, 100, 30), "0")
        self.set_main_menu()

    def get_button(self, coord, name):
        button_layout = pygame.Rect(coord)
        return pygame_gui.elements.UIButton(relative_rect=button_layout,
                                            text=name,
                                            manager=self.manager)

    def get_label(self, coord, text):
        label_layout = pygame.Rect(coord)
        return pygame_gui.elements.UILabel(relative_rect=label_layout,
                                           text=text,
                                           manager=self.manager)

    def set_main_menu(self):
        self.one_player_button.hide()
        self.two_player_button.hide()
        self.back_button.hide()
        self.player_one_scoreboard_label.visible = False
        self.player_two_scoreboard_label.visible = False
        self.start_button.visible = True
        self.exit_button.visible = True

    def set_game_type_selector(self):
        self.one_player_button.visible = True
        self.two_player_button.visible = True
        self.back_button.visible = True
        self.player_one_scoreboard_label.visible = False
        self.player_two_scoreboard_label.visible = False
        self.start_button.hide()
        self.exit_button.hide()

    def set_game_ui(self):
        self.one_player_button.hide()
        self.two_player_button.hide()
        self.back_button.hide()
        self.start_button.hide()
        self.exit_button.hide()
        self.player_one_scoreboard_label.visible = True
        self.player_two_scoreboard_label.visible = True

    def update_scoreboards(self, p1, p2):
        self.player_one_scoreboard_label.set_text(str(p1))
        self.player_two_scoreboard_label.set_text(str(p2))