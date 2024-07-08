import pygame

class Flecha():
  def __init__(self, config, jugador_left: int) -> None:
    imagen_cargada = pygame.image.load(config["ARROW_IMAGE"])
    self.imagen = pygame.transform.scale(imagen_cargada, (config["ARROW_WIDTH"], config["ARROW_HEIGHT"]))
    self.rect = pygame.Rect(jugador_left + config["CHARACTER_WIDTH"] // 2 - config["ARROW_WIDTH"] // 2, config["SCREEN_HEIGHT"] - config["CHARACTER_HEIGHT"], config["ARROW_WIDTH"], config["ARROW_HEIGHT"])
    self.velocidad: int = config['ARROW_SPEED']
    self.config = config

  def actualizar(self):
    self.rect.y -= self.velocidad

    
  def dibujar(self, pantalla: pygame.Surface):
    pantalla.blit(self.imagen, self.rect)