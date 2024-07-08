from random import randint
import pygame

class Boost():
  def __init__(self, config, pantalla: pygame.Surface) -> None:
    imagen_cargada = pygame.image.load(config["BOOST_IMAGE"])
    self.imagen = pygame.transform.scale(imagen_cargada, (config["BOOST_WIDTH"], config["BOOST_HEIGHT"]))
    self.pantalla = pantalla
    self.rect = pygame.Rect(randint(0 + config["BOOST_WIDTH"], config["SCREEN_WIDTH"] - config["BOOST_WIDTH"]), - 30 - config["BOOST_HEIGHT"] // 2, config["BOOST_WIDTH"], config["BOOST_HEIGHT"])
    self.velocidad: int = config['BOOST_SPEED']
    self.config = config

  def actualizar(self):
    self.rect.y += self.velocidad
    
  def dibujar(self, pantalla: pygame.Surface):
    pantalla.blit(self.imagen, self.rect)