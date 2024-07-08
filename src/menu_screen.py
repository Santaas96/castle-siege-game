import pygame
from puntajes_screen import puntajes_screen
from quit import quit_game
from game_screen import init_game
from utils import dibujar_boton, mostrar_texto

def main_menu_screen(pantalla: pygame.Surface, config):
  imagen_fondo = pygame.image.load(config["FONDO_MENU_IMAGE"])
  fondo = pygame.transform.scale(imagen_fondo, config["SIZE_SCREEN"])

  fuente = pygame.font.Font(None, 36)
  fuente2 = pygame.font.Font(None, 50)
  while True:
    pantalla.blit(fondo, config["ORIGIN"])

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit_game()

    mostrar_texto(pantalla, f'CASTLE SIEGE', fuente2, coordenada=(config["SCREEN_WIDTH"] // 2, 150), color= config["MAGENTA"])

    dibujar_boton(pantalla, "JUGAR", pygame.Rect(300, 250, 200, 50), config["BLUE"], config["YELLOW"], fuente, config, init_game)

    dibujar_boton(pantalla, "TABLA PUNTOS", pygame.Rect(200, 350, 400, 50), config["BLUE"], config["YELLOW"], fuente, config, puntajes_screen)

    dibujar_boton(pantalla, "SALIR", pygame.Rect(300, 550, 200, 50), config["RED"], config["YELLOW"], fuente, config, quit_game)

    pygame.display.flip()