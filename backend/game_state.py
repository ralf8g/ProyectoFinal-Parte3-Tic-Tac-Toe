class GameState:
    MENU = 0
    AI_VS_PLAYER = 1
    PLAYER_VS_PLAYER = 2
    GAME_OVER_SCREEN = 3

    def __init__(self):
        self.state = self.MENU
        self.vs_ai = False
        self.current_player = 1
        self.game_over = False
        self.winner = 0

    def start_game(self, vs_ai=False):
        self.vs_ai = vs_ai
        self.state = self.AI_VS_PLAYER if vs_ai else self.PLAYER_VS_PLAYER
        self.current_player = 1
        self.game_over = False
        self.winner = 0

    def switch_player(self):
        self.current_player = 2 if self.current_player == 1 else 1

    def end_game(self, winner):
        self.game_over = True
        self.winner = winner
        self.state = self.GAME_OVER_SCREEN

    def back_to_menu(self):
        self.state = self.MENU
        self.current_player = 1
        self.game_over = False
        self.winner = 0
