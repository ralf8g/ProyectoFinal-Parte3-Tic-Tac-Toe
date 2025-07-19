import sys
import pygame
from config import WIDTH, HEIGHT, SQUARE_SIZE
from backend.board import *
from backend.minimax import best_move_for_ai
from backend.game_state import GameState
from frontend.graphics import draw_board
from frontend.menu import draw_menu, draw_game_over_screen, load_menu_background

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Estados iniciales
game_state = GameState()
background_image = load_menu_background()

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if game_state.state == game_state.MENU:
            if event.type == pygame.MOUSEBUTTONDOWN:
                draw_menu(screen, background_image)  # Se dibuja para obtener rectángulos
                ai_btn, pvp_btn, exit_btn = draw_menu(screen, background_image)
                if ai_btn.collidepoint(event.pos):
                    game_state.start_game(vs_ai=True)
                    reset_board()
                elif pvp_btn.collidepoint(event.pos):
                    game_state.start_game(vs_ai=False)
                    reset_board()
                elif exit_btn.collidepoint(event.pos):
                    sys.exit()

        elif game_state.state in [game_state.AI_VS_PLAYER, game_state.PLAYER_VS_PLAYER]:
            if event.type == pygame.MOUSEBUTTONDOWN and not game_state.game_over:
                col = event.pos[0] // SQUARE_SIZE
                row = event.pos[1] // SQUARE_SIZE
                if is_empty(row, col):
                    mark_square(row, col, game_state.current_player)
                    if check_win(game_state.current_player):
                        game_state.end_game(winner=game_state.current_player)
                    elif is_full():
                        game_state.end_game(winner=0)
                    else:
                        game_state.switch_player()

                    if game_state.vs_ai and game_state.current_player == 2 and not game_state.game_over:
                        pygame.time.wait(300)
                        if best_move_for_ai():
                            if check_win(2):
                                game_state.end_game(winner=2)
                            elif is_full():
                                game_state.end_game(winner=0)
                            else:
                                game_state.switch_player()

        elif game_state.state == game_state.GAME_OVER_SCREEN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    game_state.back_to_menu()
                elif event.key == pygame.K_n:
                    sys.exit()

    # Render según estado
    if game_state.state == game_state.MENU:
        draw_menu(screen, background_image)
    elif game_state.state in [game_state.AI_VS_PLAYER, game_state.PLAYER_VS_PLAYER]:
        draw_board(screen)
    elif game_state.state == game_state.GAME_OVER_SCREEN:
        draw_game_over_screen(screen, game_state.winner, game_state)

    pygame.display.update()
