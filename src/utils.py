import json
import pygame
import sys
from colisiones import punto_en_rectangulo

def cargar_datos(ruta: str) -> any:
  with open(ruta, 'r') as archivo:
    return json.load(archivo)

def guardar_puntuacion(ruta: str, puntaje: int):
  datos = cargar_datos(ruta)
  datos['scores'].append(puntaje)
  with open(ruta, 'w') as archivo:
    json.dump(datos, archivo, indent=2)

def dibujar_boton(superficie: pygame.Surface, text: str, rect: pygame.Rect, color: tuple[int, int, int], hover_color: tuple[int, int, int], fuente: pygame.font.Font, config, action = None):
  mouse_pos = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()
  hovered = punto_en_rectangulo(mouse_pos, rect)
  
  if hovered:
    pygame.draw.rect(superficie, hover_color, rect)
    if click[0] == 1 and action:
      pygame.time.delay(200)
      action(superficie, config)
  else:
    pygame.draw.rect(superficie, color, rect)
  
  texto_superficie = fuente.render(text, True, config["BLACK"])
  superficie.blit(texto_superficie, (rect.x + (rect.width - texto_superficie.get_width()) // 2, rect.y + (rect.height - texto_superficie.get_height()) // 2))
  
  return hovered

def mostrar_texto(superficie: pygame.Surface, texto: str, fuente:pygame.font.Font, coordenada: tuple[int, int] = (0,0), color: tuple[int, int, int] = (255, 255, 255), background_color: tuple[int, int, int] = None, centered: bool = True) -> None:
  texto_a_renderizar = fuente.render(texto, True, color, background_color)
  rect_texto = texto_a_renderizar.get_rect()
  if centered: rect_texto.center = coordenada
  else: rect_texto.topleft = coordenada
  superficie.blit(texto_a_renderizar, rect_texto)

def esperar_tecla_usuario(tecla: int) -> None:
  flag_start = True
  while flag_start:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == tecla:
          flag_start = False

def map_list(procesadora, lista: list) -> list:
  if not isinstance(lista,list):
    raise TypeError("No es una lista")
  lista_retorno = []
  for element in lista:
    lista_retorno.append(procesadora(element))
  return lista_retorno

def bubble_sort(comparador, lista:list) -> None:
  if not isinstance(lista,list):
    raise TypeError("No es una lista")
  tam = len(lista)
  for i in range(tam - 1):
    for j in range(i + 1, tam):
      if (comparador(lista[i], lista[j])):
        aux = lista[i]
        lista[i] = lista[j]
        lista[j] = aux

def sorted_map(comparador, lista:list) -> list:
  if not isinstance(lista,list):
    raise TypeError("No es una lista")
  copia_lista = map_list(lambda numero: numero, lista)
  bubble_sort(comparador, copia_lista)
  return copia_lista

def formatear_vidas_enemigo(vida: int):
    vidas = ""
    for i in range(vida):
      vidas += "* "
    return vidas.strip()