import pygame
from random import randint
from utils import formatear_vidas_enemigo, mostrar_texto

class EnemigoNormal():
  def __init__(self, config, pantalla: pygame.Surface) -> None:
    # self.image = pygame.image.load(config['IMAGEN_JUGADOR'])
    # self.rect = self.image.get_rect(center=(config['screen_width'] // 2, config['screen_height'] - 50))
    self.pantalla = pantalla
    self.rect = pygame.Rect(randint(0 + config["SMALL_ENEMY_WIDTH"], config["SCREEN_WIDTH"] - config["SMALL_ENEMY_WIDTH"]), - 30 - config["SMALL_ENEMY_HEIGHT"] // 2, config["SMALL_ENEMY_WIDTH"], config["SMALL_ENEMY_HEIGHT"])
    self.velocidad: int = config['SMALL_ENEMY_SPEED']
    self.vida: int = config['SMALL_ENEMY_LIFEPOINTS']
    self.puntos: int = config['SMALL_ENEMY_LIFEPOINTS']
    self.config = config
    self.speed_delay = False

  def actualizar(self):
    if not self.speed_delay: self.rect.y += self.velocidad
    else: self.speed_delay = True
    
  def dibujar(self, pantalla: pygame.Surface):
    # pantalla.blit(self.image, self.rect)
    fuente = pygame.font.Font(None, 40)
    mostrar_texto(self.pantalla, f'{formatear_vidas_enemigo(self.vida)}', fuente, color=self.config["RED"], coordenada=(self.rect.center[0], self.rect.top - 10))
    pygame.draw.rect(pantalla, self.config["YELLOW"], self.rect)

class EnemigoElite():
  def __init__(self, config, pantalla: pygame.Surface) -> None:
    # self.image = pygame.image.load(config['IMAGEN_JUGADOR'])
    # self.rect = self.image.get_rect(center=(config['screen_width'] // 2, config['screen_height'] - 50))
    self.pantalla = pantalla
    self.rect = pygame.Rect(randint(0 + config["BIG_ENEMY_WIDTH"], config["SCREEN_WIDTH"] - config["BIG_ENEMY_WIDTH"]), - 30 - config["BIG_ENEMY_HEIGHT"] // 2, config["BIG_ENEMY_WIDTH"], config["BIG_ENEMY_HEIGHT"])
    self.velocidad: int = config['BIG_ENEMY_SPEED']
    self.vida: int = config['BIG_ENEMY_LIFEPOINTS']
    self.puntos: int = config['BIG_ENEMY_LIFEPOINTS']
    self.config = config
    self.speed_delay = False
  
  def actualizar(self):
    if not self.speed_delay: self.rect.y += self.velocidad
    else: self.speed_delay = True

  def dibujar(self, pantalla: pygame.Surface):
    # pantalla.blit(self.image, self.rect)
    fuente = pygame.font.Font(None, 40)
    mostrar_texto(self.pantalla, f'{formatear_vidas_enemigo(self.vida)}', fuente, color=self.config["RED"], coordenada=(self.rect.center[0], self.rect.top -10))
    pygame.draw.rect(pantalla, self.config["MAGENTA"], self.rect)