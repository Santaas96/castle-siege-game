from random import randint
import pygame

class Boost():
  def __init__(self, config, pantalla: pygame.Surface) -> None:
  # self.image = pygame.image.load(config['IMAGEN_JUGADOR'])
  # self.rect = self.image.get_rect(center=(config['screen_width'] // 2, config['screen_height'] - 50))
    self.pantalla = pantalla
    self.rect = pygame.Rect(randint(0 + config["BOOST_WIDTH"], config["SCREEN_WIDTH"] - config["SMALL_ENEMY_WIDTH"]), - 30 - config["BOOST_HEIGHT"] // 2, config["BOOST_WIDTH"], config["BOOST_HEIGHT"])
    self.velocidad: int = config['BOOST_SPEED']
    self.config = config

  def actualizar(self):
    self.rect.y += self.velocidad
    
  def dibujar(self, pantalla: pygame.Surface):
    # pantalla.blit(self.image, self.rect)
    pygame.draw.rect(pantalla, self.config["YELLOW"], self.rect, border_radius=self.config["BOOST_HEIGHT"])