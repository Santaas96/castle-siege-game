import pygame
from puntajes_screen import puntajes_screen
from quit import quit_game
from game_screen import init_game
from utils import dibujar_boton

def main_menu_screen(pantalla: pygame.Surface, config):
  fuente = pygame.font.Font(None, 36)
  while True:
    pantalla.fill(config["BLACK"])

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit_game()

    dibujar_boton(pantalla, "JUGAR", pygame.Rect(300, 200, 200, 50), config["BLUE"], config["YELLOW"], fuente, config, init_game)

    dibujar_boton(pantalla, "TABLA PUNTOS", pygame.Rect(200, 300, 400, 50), config["BLUE"], config["YELLOW"], fuente, config, puntajes_screen)

    dibujar_boton(pantalla, "SALIR", pygame.Rect(300, 500, 200, 50), config["RED"], config["YELLOW"], fuente, config, quit_game)

    pygame.display.flip()