import pygame
from quit import quit_game
from utils import cargar_datos, dibujar_boton, mostrar_texto, sorted_map

def puntajes_screen(pantalla: pygame.Surface, config):
  imagen_fondo = pygame.image.load(config["FONDO_LEADERBOARD_IMAGE"])
  fondo = pygame.transform.scale(imagen_fondo, config["SIZE_SCREEN"])

  try:
    datos = cargar_datos('src/settings.json')
  except FileNotFoundError:
    print("\n\n*****Archivo de configuración no encontrado******\n\n")
    quit_game()

  puntajes = datos["scores"]
  scores = sorted_map(lambda a, b: a < b, puntajes)
    
  fuente1 = pygame.font.Font(None, 36)
  fuente2 = pygame.font.Font(None, 50)

  while True:
    pantalla.blit(fondo, config["ORIGIN"])

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit_game()

    mostrar_texto(pantalla, f'TABLA MAYORES 5 PUNTAJES', fuente2, coordenada=(400, 100), color= config["MAGENTA"])

    CANTIDAD_PUNTAJES = 5
    coord_y = 200
    for i in range(CANTIDAD_PUNTAJES):
      try:
        mostrar_texto(pantalla, f'{i + 1})     {scores[i]}', fuente2, coordenada=(400, coord_y), color= config["GREEN"])
      except IndexError:
        mostrar_texto(pantalla, f'{i + 1})     {0}', fuente2, coordenada=(400, coord_y), color= config["GREEN"])
      
      coord_y += 50

    from menu_screen import main_menu_screen
    dibujar_boton(pantalla, "MENU", pygame.Rect(250, 500, 300, 50), config["BLUE"], config["YELLOW"], fuente1, config, main_menu_screen)

    dibujar_boton(pantalla, "SALIR", pygame.Rect(300, 600, 200, 50), config["RED"], config["YELLOW"], fuente1, config, quit_game)

    pygame.display.flip()