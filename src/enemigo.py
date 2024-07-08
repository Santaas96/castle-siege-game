import pygame
from random import randint
from utils import formatear_vidas_enemigo, mostrar_texto

class EnemigoNormal():
  def __init__(self, config, pantalla: pygame.Surface) -> None:
    imagen_cargada = pygame.image.load(config["SMALL_ENEMY_IMAGE"])
    self.imagen = pygame.transform.scale(imagen_cargada, (config["SMALL_ENEMY_WIDTH"], config["SMALL_ENEMY_HEIGHT"]))
    self.rect = pygame.Rect(randint(0 + config["SMALL_ENEMY_WIDTH"], config["SCREEN_WIDTH"] - config["SMALL_ENEMY_WIDTH"]), - 30 - config["SMALL_ENEMY_HEIGHT"] // 2, config["SMALL_ENEMY_WIDTH"], config["SMALL_ENEMY_HEIGHT"])
    self.pantalla = pantalla
    self.velocidad: int = config['SMALL_ENEMY_SPEED']
    self.vida: int = config['SMALL_ENEMY_LIFEPOINTS']
    self.puntos: int = config['SMALL_ENEMY_LIFEPOINTS']
    self.config = config
    self.speed_delay = False

  def actualizar(self):
    if not self.speed_delay: self.rect.y += self.velocidad
    else: self.speed_delay = True
    
  def dibujar(self, pantalla: pygame.Surface):
    fuente = pygame.font.Font(None, 40)
    mostrar_texto(self.pantalla, f'{formatear_vidas_enemigo(self.vida)}', fuente, color=self.config["RED"], coordenada=(self.rect.center[0], self.rect.top - 10))
    self.pantalla.blit(self.imagen, self.rect)

class EnemigoElite():
  def __init__(self, config, pantalla: pygame.Surface) -> None:
    imagen_cargada = pygame.image.load(config["BIG_ENEMY_IMAGE"])
    self.imagen = pygame.transform.scale(imagen_cargada, (config["BIG_ENEMY_WIDTH"], config["BIG_ENEMY_HEIGHT"]))
    self.rect = pygame.Rect(randint(0 + config["BIG_ENEMY_WIDTH"], config["SCREEN_WIDTH"] - config["BIG_ENEMY_WIDTH"]), - 30 - config["BIG_ENEMY_HEIGHT"] // 2, config["BIG_ENEMY_WIDTH"], config["BIG_ENEMY_HEIGHT"])
    self.pantalla = pantalla
    self.velocidad: int = config['BIG_ENEMY_SPEED']
    self.vida: int = config['BIG_ENEMY_LIFEPOINTS']
    self.puntos: int = config['BIG_ENEMY_LIFEPOINTS']
    self.config = config
    self.speed_delay = False
  
  def actualizar(self):
    if not self.speed_delay: self.rect.y += self.velocidad
    else: self.speed_delay = True

  def dibujar(self, pantalla: pygame.Surface):
    fuente = pygame.font.Font(None, 40)
    mostrar_texto(self.pantalla, f'{formatear_vidas_enemigo(self.vida)}', fuente, color=self.config["RED"], coordenada=(self.rect.center[0], self.rect.top -10))
    self.pantalla.blit(self.imagen, self.rect)