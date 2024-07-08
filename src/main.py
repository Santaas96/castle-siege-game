import pygame
from menu_screen import main_menu_screen
from quit import quit_game
from utils import cargar_datos

# INICIALIZO PYGAME
pygame.init()
# CARGO CONFIGURACION DESDE JSON
try:
  datos = cargar_datos('src/settings.json')
except FileNotFoundError:
  print("\n\n*****Archivo de configuración no encontrado******\n\n")
  quit_game()
config = datos["config"]
# CONFIGURO PANTALLA
pantalla_principal = pygame.display.set_mode((config["SCREEN_WIDTH"], config["SCREEN_HEIGHT"]))
pygame.display.set_caption("CASTLE SIEGE")

if __name__ == '__main__':
  main_menu_screen(pantalla_principal, config)

# a.mendiberry@sistemas-utnfra.com.ar