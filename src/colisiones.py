import pygame

def detectar_colision_rectangulos(rect_1: pygame.Rect, rect_2: pygame.Rect) -> bool:
  rect_1_en_rect_2 = punto_en_rectangulo(rect_1.bottomleft, rect_2) or punto_en_rectangulo(rect_1.bottomright, rect_2) or punto_en_rectangulo(rect_1.topleft, rect_2) or punto_en_rectangulo(rect_1.topright, rect_2)

  rect_2_en_rect_1 = punto_en_rectangulo(rect_2.bottomleft, rect_1) or punto_en_rectangulo(rect_2.bottomright, rect_1) or punto_en_rectangulo(rect_2.topleft, rect_1) or punto_en_rectangulo(rect_2.topright, rect_1)

  return rect_1_en_rect_2 or rect_2_en_rect_1

def punto_en_rectangulo(punto: tuple[int, int], rect: pygame.Rect) -> bool:
  coord_x, coord_y = punto
  return (coord_x >= rect.left and coord_x <= rect.right) and (coord_y >= rect.top and coord_y <= rect.bottom)

def distancia_entre_puntos(punto_1: tuple[int, int], punto_2: tuple[int, int]) -> float:
  return ((punto_1[0] - punto_2[0]) ** 2 + (punto_1[1] - punto_2[1]) ** 2) ** 0.5

def calcular_radio(rect: pygame.Rect) -> float:
  return rect.width / 2

def detectar_colision_circulos(rect_1: pygame.Rect, rect_2: pygame.Rect) -> bool:
  radio_1 = calcular_radio(rect_1)
  radio_2 = calcular_radio(rect_2)
  distancia = distancia_entre_puntos(rect_1.center, rect_2.center)
  return distancia <= radio_1 + radio_2