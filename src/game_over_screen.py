import pygame
from quit import quit_game
from utils import dibujar_boton, guardar_puntuacion, mostrar_texto

def game_over_screen(pantalla: pygame.Surface, score: int, config):
  imagen_fondo = pygame.image.load(config["FONDO_GAMEOVER_IMAGE"])
  fondo = pygame.transform.scale(imagen_fondo, config["SIZE_SCREEN"])

  try:
    guardar_puntuacion('src/settings.json', score)
  except FileNotFoundError:
    print("\n\n*****Archivo de configuración no encontrado******\n\n")
    quit_game()
    
  fuente1 = pygame.font.Font(None, 36)
  fuente2 = pygame.font.Font(None, 50)
  while True:
    pantalla.blit(fondo, config["ORIGIN"])

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit_game()

    mostrar_texto(pantalla, f'TU PUNTAJE: {score}', fuente2, coordenada=(400, 200), color= config["GREEN"])

    from game_screen import init_game
    dibujar_boton(pantalla, "JUGAR DE NUEVO", pygame.Rect(200, 300, 400, 50), config["BLUE"], config["YELLOW"], fuente1, config, init_game)
    from puntajes_screen import puntajes_screen
    dibujar_boton(pantalla, "TABLA PUNTOS", pygame.Rect(200, 400, 400, 50), config["BLUE"], config["YELLOW"], fuente1, config, puntajes_screen)

    dibujar_boton(pantalla, "SALIR", pygame.Rect(300, 500, 200, 50), config["RED"], config["YELLOW"], fuente1, config, quit_game)

    pygame.display.flip()