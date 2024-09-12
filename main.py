#pgzero
import random

""" > M6.L1 · Actividad #3: "Naves hostiles"

Kenney assets:

Kodland: https://kenney.nl/assets/space-shooter-extension
Extra: https://kenney.nl/assets/space-shooter-redux
Planetas: https://kenney.nl/assets/planets
UI: https://kenney.nl/assets/ui-pack-sci-fi

Objetivo: Agregar lógica de spawn de enemigos
Prox. Actividad: "Reciclar"/Reemplazar naves enemigas que se salgan de la pantalla de juego

Paso Nº 1: importamos la librería random
Paso Nº 2: Definimos la cantidad de enemigos a spawnear (constante CANT_ENEMIGOS)
Paso Nº 3: Creamos nuestra lista_enemigos
Paso Nº 4: Creamos el bucle de spawn
Paso Nº 5: Agregamos la función que maneja el avance de la flota enemiga
Paso Nº 6: Agregamos un bucle for en nuestro draw() que dibuje las naves enemigas
Paso Nº 7: Agregamos nuesto update() que incluirá una llamada a mov_flota_enemiga()
"""

WIDTH = 600
HEIGHT = 450

TITLE = "GUERRA GALÁCTICA"
FPS = 30

# Objetos y Variables
CANT_ENEMIGOS = 5 # Cantidad de enemigos a spawnear

nave = Actor("ship", (300,300))
fondo = Actor("space")

# Listas
lista_enemigos = []

# To-do: Convertir a una función

for e in range(CANT_ENEMIGOS):
  # Setear coordenadas random (importamos la librería)
  x = random.randint(50, WIDTH-50)
  y = random.randint(-200, -50)

  # To-do: permitir que haya más de un tipo de enemigo
  # To-do: chequear que no se superpongan los enemigos entre sí

  # Creamos el nvo_enemigo
  nvo_enemigo = Actor("enemy", (x, y))
  nvo_enemigo.velocidad = random.randint(4, 8)
    
  """ Nota: Si yo quiero que la velocidad de los enemigos sea un factor
            de la dificultad del juego, en lugar de ser random p/cada
            nave, puedo crear una variable global llamada "velocidad_naves_enemigas"
            (o algo así) y actualizarlo cuando lo necesite """
             
  lista_enemigos.append(nvo_enemigo)

# FUNCIONES PROPIAS

def mov_flota_enemiga():
  for nave_enemiga in lista_enemigos:
    nave_enemiga.y += nave_enemiga.velocidad

    """ To-do: evitar que las naves salgan de la pantalla

        OPCION 1: ELIMINARLAS
        OPCION 2: RECICLARLAS """

# Funciones PGZERO

def draw():
  fondo.draw()
  
  for nave_enemiga in lista_enemigos:
    nave_enemiga.draw()
  
  #screen.draw.text(TITLE, center=(300, 100), color="white", background="black")

  texto_temp = "Coord: (x: " + str(int(nave.x)) + ", y: " + str(int(nave.y)) + ")"
  screen.draw.text(texto_temp, midleft=(20, 20), color = "white", fontsize = 24)

  nave.draw()

def on_mouse_move(pos):
  nave.pos = pos

def update(dt):
  mov_flota_enemiga()