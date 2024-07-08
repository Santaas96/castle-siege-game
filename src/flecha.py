import pygame

class Flecha():
  def __init__(self, config, jugador_left: int) -> None:
    # self.image = pygame.image.load(config['IMAGEN_JUGADOR'])
    # self.rect = self.image.get_rect(center=(config['screen_width'] // 2, config['screen_height'] - 50))
    self.rect = pygame.Rect(jugador_left + config["CHARACTER_WIDTH"] // 2, config["SCREEN_HEIGHT"] - config["CHARACTER_HEIGHT"], config["ARROW_WIDTH"], config["ARROW_HEIGHT"])
    self.velocidad: int = config['ARROW_SPEED']
    self.config = config

  def actualizar(self):
    self.rect.y -= self.velocidad

    
  def dibujar(self, pantalla: pygame.Surface):
    # pantalla.blit(self.image, self.rect)
    pygame.draw.rect(pantalla, self.config["BLUE"], self.rect)