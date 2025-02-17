import pygame
from boost import Boost
from colisiones import detectar_colision_rectangulos
from enemigo import EnemigoElite, EnemigoNormal
from jugador import Jugador
from utils import mostrar_texto

class Game:
  def __init__(self, pantalla: pygame.Surface, config) -> None:
    imagen_fondo = pygame.image.load(config["GRASS_IMAGE"])
    self.fondo = pygame.transform.scale(imagen_fondo, config["SIZE_SCREEN"])
    imagen_castillo = pygame.image.load(config["CASTLE_IMAGE"])
    self.castillo = pygame.transform.scale(imagen_castillo, (config["SCREEN_WIDTH"], config["CHARACTER_HEIGHT"]))
    self.pantalla = pantalla
    self.config = config
    self.puntaje: int = 0
    self.vida: int = config["CASTLE_LIFEPOINTS"]
    self.jugador: Jugador = Jugador(config, pantalla)
    self.fuente = pygame.font.Font(None, 40)
    self.enemigos: list[EnemigoElite | EnemigoNormal] = [EnemigoNormal(config, pantalla), EnemigoElite(config, pantalla)]
    self.boosts: list[Boost] = []
    self.REMOVEBOOST = pygame.USEREVENT + 5

  def actualizar(self):
    self.jugador.actualizar()

    for enemigo in self.enemigos:
      enemigo.actualizar()

    for boost in self.boosts:
      boost.actualizar()

    self.verificar_colisiones_flechas_enemigos()
    self.verificar_colisiones_enemigos_castillo()
    self.verificar_vida_castillo()
    self.verificar_colision_jugador_boost()
    self.verificar_colision_boost_fondo()

  def dibujar(self):
    self.pantalla.blit(self.fondo, self.config["ORIGIN"])
    self.pantalla.blit(self.castillo, (0, self.config["SCREEN_HEIGHT"] - self.config["CHARACTER_HEIGHT"]))

    self.jugador.dibujar(self.pantalla)

    for enemigo in self.enemigos:
      enemigo.dibujar(self.pantalla)
    
    for boost in self.boosts:
      boost.dibujar(self.pantalla)

    # Actualizo informacion de la partida
    mostrar_texto(self.pantalla, f'Score: {self.puntaje}', self.fuente, (20, 10), centered=False)
    mostrar_texto(self.pantalla, f'Castillo: {self.vida}%', self.fuente, coordenada=(self.config["SCREEN_WIDTH"] - 110, 20))
  
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
        self.vida -= enemigo.vida * 2
        try:
          self.enemigos.remove(enemigo)
        except ValueError:
          print("El remove no encontro su objetivo en la lista")

  def verificar_vida_castillo(self):
    if self.vida <= 0:
      from game_over_screen import game_over_screen
      game_over_screen(self.pantalla, self.puntaje, self.config)

  def verificar_colision_jugador_boost(self):
    for boost in self.boosts[:]:
      if detectar_colision_rectangulos(boost.rect, self.jugador.rect):
        pygame.time.set_timer(self.REMOVEBOOST, self.config["BOOST_DURATION"], 1)
        self.boosts.remove(boost)
        self.jugador.arrow_boost = True
        self.jugador.color = self.config["YELLOW"]

  def verificar_colision_boost_fondo(self):
    for boost in self.boosts[:]:
      if boost.rect.top >= self.config["SCREEN_HEIGHT"]:
        self.boosts.remove(boost)

