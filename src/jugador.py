import pygame
from flecha import Flecha

class Jugador:
  def __init__(self, config, pantalla: pygame.Surface):
    imagen_cargada = pygame.image.load(config["CHARACTER_IMAGE"])
    self.imagen = pygame.transform.scale(imagen_cargada, (config["CHARACTER_WIDTH"], config["CHARACTER_HEIGHT"]))
    self.rect = pygame.Rect(config["SCREEN_WIDTH"] // 2 - config["CHARACTER_WIDTH"] // 2, config["SCREEN_HEIGHT"] - config["CHARACTER_HEIGHT"], config["CHARACTER_WIDTH"], config["CHARACTER_HEIGHT"])
    self.pantalla = pantalla
    self.velocidad = config['CHARACTER_INITIAL_SPEED']
    self.config = config
    self.color = config["BLUE"]
    self.flechas: list[Flecha] = []
    self.arrow_boost = False

  def actualizar(self):
    teclas = pygame.key.get_pressed()
    if (teclas[pygame.K_a] or teclas[pygame.K_LEFT]) and self.rect.left > 0:
      self.rect.x -= self.velocidad
      if self.rect.left < 0:
        self.rect.left = 0
    if (teclas[pygame.K_d] or teclas[pygame.K_RIGHT]) and self.rect.right < self.config["SCREEN_WIDTH"]:
      self.rect.x += self.velocidad
      if self.rect.left > self.config["SCREEN_WIDTH"]:
        self.rect.left = self.config["SCREEN_WIDTH"]
    if teclas[pygame.K_SPACE]:
      if self.arrow_boost:
        self.disparar()

    for flecha in self.flechas[:]:
      flecha.actualizar()
      if flecha.rect.bottom < 0:
        try:
          self.flechas.remove(flecha)
        except ValueError:
          print("El remove no encontro su objetivo en la lista")

  def disparar(self):
    self.flechas.append(Flecha(self.config, self.rect.left))

  def dibujar(self, pantalla: pygame.Surface):
    pantalla.blit(self.imagen, self.rect)

    for flecha in self.flechas:
      flecha.dibujar(self.pantalla)