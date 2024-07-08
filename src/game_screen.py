import pygame
from boost import Boost
from enemigo import EnemigoElite, EnemigoNormal
from quit import quit_game
from game import Game
from utils import esperar_tecla_usuario, mostrar_texto

def init_game(pantalla: pygame.Surface, config):
  pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
  clock = pygame.time.Clock()
  running = True
  game_instance = Game(pantalla, config)

  # Evento para sumar un punto despues de 1 segundo
  NEWSCOREPOINT = pygame.USEREVENT + 1
  pygame.time.set_timer(NEWSCOREPOINT, 1000)
  # Evento para agregar enemigo normal
  ADDNORMALENEMY = pygame.USEREVENT + 2
  pygame.time.set_timer(ADDNORMALENEMY, 1550)
  # Evento para agregar enemigo elite
  ADDELITEENEMY = pygame.USEREVENT + 3
  pygame.time.set_timer(ADDELITEENEMY, 2870)
  # Evento para agregar un elemento Boost
  ADDBOOST = pygame.USEREVENT + 4
  pygame.time.set_timer(ADDBOOST, 12000)
  # Evento para sacarle el boost al jugador
  REMOVEBOOST = pygame.USEREVENT + 5

  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit_game()
      if event.type == NEWSCOREPOINT:
        game_instance.puntaje = game_instance.puntaje + 1
      if event.type == ADDNORMALENEMY:
        game_instance.enemigos.append(EnemigoNormal(game_instance.config, pantalla))
      if event.type == ADDELITEENEMY:
        game_instance.enemigos.append(EnemigoElite(game_instance.config, pantalla))
      if event.type == ADDBOOST:
        game_instance.boosts.append(Boost(game_instance.config, pantalla))
      if event.type == REMOVEBOOST:
        game_instance.jugador.arrow_boost = False
        game_instance.jugador.color = config["BLUE"]
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
          font = pygame.font.Font(None, 56)
          mostrar_texto(pantalla,"PAUSE", font, config["CENTER_SCREEN"], config["GREEN"])
          pygame.display.flip()
          esperar_tecla_usuario(pygame.K_p)
        if event.key == pygame.K_SPACE:
          if not game_instance.jugador.arrow_boost:
            game_instance.jugador.disparar()
          
    # Actualizo pantalla
    game_instance.actualizar()

    # Dibujo pantalla
    game_instance.dibujar()

    pygame.display.flip()
    clock.tick(config["FPS"])