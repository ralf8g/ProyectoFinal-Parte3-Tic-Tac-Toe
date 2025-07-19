import pygame
from config import *
import os
from backend.board import board
from frontend.graphics import draw_board

def load_menu_background():
    try:
        image = pygame.image.load(os.path.join('frontend', 'assets', 'background.jpg')).convert()
        return pygame.transform.scale(image, (WIDTH, HEIGHT))
    except pygame.error:
        print("No se pudo cargar la imagen de fondo.")
        return None

def draw_menu(screen, background):
    if background:
        screen.blit(background, (0, 0))
    else:
        screen.fill(BLACK)
    font_title = pygame.font.SysFont('georgia', 30, bold=True)
    font_options = pygame.font.SysFont('georgia', 20)

    title = font_title.render("TIC-TAC-TOE", True, WHITE)
    screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 4)))

    options = ["Jugar con la IA", "2 jugadores", "Salir"]
    button_rects = []
    for i, opt in enumerate(options):
        rect = pygame.Rect(WIDTH // 2 - 125, HEIGHT // 2 + i * 60, 250, 45)
        color = MENU_BUTTON_SELECTED if rect.collidepoint(pygame.mouse.get_pos()) else MENU_BUTTON_DARK
        pygame.draw.rect(screen, color, rect, border_radius=10)
        text = font_options.render(opt, True, WHITE)
        screen.blit(text, text.get_rect(center=rect.center))
        button_rects.append(rect)
    return button_rects

def draw_game_over_screen(screen, winner, game_state):
    screen.fill(BLACK)
    draw_board(screen)

    font = pygame.font.SysFont('georgia', 45)
    msg = "EMPATE!" if winner == 0 else ("AI Gana!" if game_state.vs_ai else f"Jugador {winner} gana!")
    color = GRAY if winner == 0 else (RED if winner == 2 else GREEN)

    msg_surface = font.render(msg, True, color)
    screen.blit(msg_surface, msg_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3)))

    prompt = pygame.font.SysFont('georgia', 30).render("¿Continuar? (S/N)", True, WHITE)
    screen.blit(prompt, prompt.get_rect(center=(WIDTH // 2, HEIGHT // 3 * 2)))
