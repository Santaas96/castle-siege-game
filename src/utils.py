import json
import pygame
import sys
from colisiones import punto_en_rectangulo

def cargar_datos(ruta: str) -> any:
  '''
    Carga un archivo json tomando una ruta como parametro.

      Parameters:
              ruta (str): Ruta archivo json en formato string.

      Returns:
              Contenido archivo json.
  '''
  with open(ruta, 'r') as archivo:
    return json.load(archivo)

def guardar_puntuacion(ruta: str, puntaje: int) -> None:
  '''
    Guarda en un archivo json el puntaje pasado por parametro.

      Parameters:
              ruta (str): Ruta archivo json en formato string.
              puntaje (int): Puntaje para guardar en json.

  '''
  datos = cargar_datos(ruta)
  datos['scores'].append(puntaje)
  with open(ruta, 'w') as archivo:
    json.dump(datos, archivo, indent=2)

def dibujar_boton(superficie: pygame.Surface, text: str, rect: pygame.Rect, color: tuple[int, int, int], hover_color: tuple[int, int, int], fuente: pygame.font.Font, config, action = None) -> bool:
  '''
    Dibuja un boton en la superficie indicada y devuelve si el mismo esta en estado hover.

      Parameters:
              superficie (Surface): Superficie en donde dibujar el boton.
              text (str): Texto a escribir en el boton.
              rect (Rect): Base del boton.
              color (tuple[int, int, int]): Color del boton.
              hover_color (tuple[int, int, int]): Color del boton en estado hover.
              fuente (font.Font): Configuracion del objeto fuente de pygame.
              config (any): Datos de configuracion del juego.
              action (Function): Funcion a ejecutar cuando se haga click encima del boton.

      Returns:
              Retorna si el boton esta en estado hover.
  '''
  mouse_pos = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()
  hovered = punto_en_rectangulo(mouse_pos, rect)
  
  if hovered:
    pygame.draw.rect(superficie, hover_color, rect)
    if click[0] == 1 and action:
      pygame.time.delay(200)
      try:
        action(superficie, config)
      except TypeError:
        action()
  else:
    pygame.draw.rect(superficie, color, rect)
  
  texto_superficie = fuente.render(text, True, config["BLACK"])
  superficie.blit(texto_superficie, (rect.x + (rect.width - texto_superficie.get_width()) // 2, rect.y + (rect.height - texto_superficie.get_height()) // 2))
  
  return hovered

def mostrar_texto(superficie: pygame.Surface, texto: str, fuente:pygame.font.Font, coordenada: tuple[int, int] = (0,0), color: tuple[int, int, int] = (255, 255, 255), background_color: tuple[int, int, int] = None, centered: bool = True) -> None:
  '''
    Muestra un determinado texto en la superficie indicada.

      Parameters:
              superficie (Surface): Superficie en donde dibujar el boton.
              text (str): Texto a mostrar.
              fuente (font.Font): Configuracion del objeto fuente de pygame.
              coordenada (tuple[int, int]): Destino del texto renderizado.
              color (tuple[int, int, int]): Color del texto.
              background_color (tuple[int, int, int]): Color del fondo del texto.
              centeres (bool): Si queremos que el texto este alineado al centro.

  '''
  texto_a_renderizar = fuente.render(texto, True, color, background_color)
  rect_texto = texto_a_renderizar.get_rect()
  if centered: rect_texto.center = coordenada
  else: rect_texto.topleft = coordenada
  superficie.blit(texto_a_renderizar, rect_texto)

def esperar_tecla_usuario(tecla: int) -> None:
  '''
    Inicia un bucle que se destraba solo presionando la tecla que viene por parametro o saliendo de la ventana del juego.

      Parameters:
              tecla (int): Valor de la tecla para salir del bucle.

  '''
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
  '''
    Retorna una lista despues de haber procesado cada item de la lista pasada por parametro.

      Parameters:
              procesadora (Function): Funcion que obtiene cada uno de los items de la lista original.
              lista (list): Lista para iterar y procesar cada uno de sus items.

      Returns:
              Lista procesada.
  '''
  if not isinstance(lista,list):
    raise TypeError("No es una lista")
  lista_retorno = []
  for element in lista:
    lista_retorno.append(procesadora(element))
  return lista_retorno

def bubble_sort(comparador, lista:list) -> None:
  '''
    Muta una lista pasada por parametro para ordenarla segun este especificado en la funcion comparadora.

      Parameters:
              comparadora (Function): Funcion que compara cada item con el posterior de la lista.
              lista (list): Lista para iterar y comparar cada uno de sus items.

  '''
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
  '''
    Retorna una nueva lista ordenada segun este especificado en la funcion comparadora.

      Parameters:
              comparadora (Function): Funcion que compara cada item con el posterior de la lista.
              lista (list): Lista para iterar y comparar cada uno de sus items.

      Returns:
              Lista ordenada segun este especificado en la funcion comparadora.
  '''
  if not isinstance(lista,list):
    raise TypeError("No es una lista")
  copia_lista = map_list(lambda a: a, lista)
  bubble_sort(comparador, copia_lista)
  return copia_lista

def formatear_vidas_enemigo(vida: int) -> str:
  '''
    Formatea una cadena de caracteres para mostrar un "*" en relacion a la magnitud del parametro ingresado.

      Parameters:
              vida (int): Entero que representa la vida de alguien o algo.

      Returns:
              Cadena formateada para mostrar en pantalla
  '''
  vidas = ""
  for i in range(vida):
    vidas += "* "
  return vidas.strip()