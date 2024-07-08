import pygame
from colisiones import detectar_colision_rectangulos
from enemigo import EnemigoElite, EnemigoNormal
from jugador import Jugador
from utils import mostrar_texto

class Game:
  def __init__(self, pantalla: pygame.Surface, config) -> None:
    self.pantalla = pantalla
    self.config = config
    self.puntaje: int = 0
    self.vida: int = config["CASTLE_LIFEPOINTS"]
    self.jugador: Jugador = Jugador(config, pantalla)
    self.fuente = pygame.font.Font(None, 36)
    self.enemigos: list[EnemigoElite | EnemigoNormal] = [EnemigoNormal(config, pantalla), EnemigoElite(config, pantalla)]

  def actualizar(self):
    self.jugador.actualizar()

    for enemigo in self.enemigos:
      enemigo.actualizar()

    self.verificar_colisiones_flechas_enemigos()
    self.verificar_colisiones_enemigos_castillo()
    self.verificar_vida_castillo()

  def dibujar(self):
    self.pantalla.fill(self.config["BLACK"])

    self.jugador.dibujar(self.pantalla)

    for enemigo in self.enemigos:
      enemigo.dibujar(self.pantalla)

    # Actualizo informacion de la partida
    mostrar_texto(self.pantalla, f'Score: {self.puntaje}', self.fuente, (20, 10), centered=False)
    mostrar_texto(self.pantalla, f'Castillo: {self.vida}%', self.fuente, coordenada=(self.config["SCREEN_WIDTH"] - 100, 20))
  
  def verificar_colisiones_flechas_enemigos(self):
    for flecha in self.jugador.flechas[:]:
      for enemigo in self.enemigos:
        # Chequeamos si alguna flecha toca algun enemigo
        if detectar_colision_rectangulos(flecha.rect, enemigo.rect):
          enemigo.vida -= 1
          try:
            self.jugador.flechas.remove(flecha)
          except ValueError:
            print("El remove no encontro su objetivo en la lista")
          # Si el enemigo no tiene vida lo removemos
          if enemigo.vida == 0:
            self.puntaje += enemigo.puntos
            try:
              self.enemigos.remove(enemigo)
            except ValueError:
              print("El remove no encontro su objetivo en la lista")
  
  def verificar_colisiones_enemigos_castillo(self):
    for enemigo in self.enemigos[:]:
      # Si toca el castillo le restamos la vida actual del enemigo a la vida del castillo
      if enemigo.rect.bottom > self.config["SCREEN_HEIGHT"] - self.config["CHARACTER_HEIGHT"]:
        self.vida -= enemigo.vida
        try:
          self.enemigos.remove(enemigo)
        except ValueError:
          print("El remove no encontro su objetivo en la lista")

  def verificar_vida_castillo(self):
    if self.vida <= 0:
      from game_over_screen import game_over_screen
      game_over_screen(self.pantalla, self.puntaje, self.config)


