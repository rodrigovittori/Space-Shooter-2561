#pgzero
import random

""" > M6.L1 · Actividad #8: "Planetas (Asignación extra)"

Kenney assets:

Kodland: https://kenney.nl/assets/space-shooter-extension
Extra: https://kenney.nl/assets/space-shooter-redux
Planetas: https://kenney.nl/assets/planets
UI: https://kenney.nl/assets/ui-pack-sci-fi

Objetivo: Agregar planetas como elemento decorativo
Prox. Actividad: Meteoritos (Homework)

Paso Nº 1: Crear una lista donde almacenar los planetas
Paso Nº 2: Crear los actores con las imágenes de los planetas y agregarlos a su lista
Paso Nº 3: Crear una función que se encargue de actualizar su posición y reciclarlos una vez hayan salido de la ventana de juego
Paso Nº 4: Actualizar nuestro draw() para que muestre los planetas en pantalla
Paso Nº 5: Actualizar nuestro update() para que llame a mov_planetas()

    ##################
   # VENTANA PGZERO #
  ################## """

WIDTH = 600
HEIGHT = 450

TITLE = "GUERRA GALÁCTICA"
FPS = 30

""" ***************************************************************** """

# Objetos y Variables
CANT_ENEMIGOS = 5 # Cantidad de enemigos a spawnear
modo_actual = "juego" # Valores posibles: "juego" / "game_over"


nave = Actor("ship", (300,300))
fondo = Actor("space")

# Listas
lista_enemigos = []
lista_planetas = []

# Creamos los planetas
planeta_1 = Actor("plan1", (random.randint(0, WIDTH), random.randint(-400, -50)))
planeta_1.angle = random.randint(0,359)
lista_planetas.append(planeta_1)

planeta_2 = Actor("plan2", (random.randint(0, WIDTH), random.randint(-800, -450)))
planeta_2.angle = random.randint(0,359)
lista_planetas.append(planeta_2)

planeta_3 = Actor("plan3", (random.randint(0, WIDTH), random.randint(-1200, -850)))
planeta_3.angle = random.randint(0,359)
lista_planetas.append(planeta_3)


""" ***************************************************************** """

def spawn_nvo_enemigo(tipo=""):

  # Determinar tipo de enemigo a añadir:
  if tipo == "":
      tipo = "enemy"
  
  # To-do: permitir que haya más de un tipo de enemigo
  pos_valida = False

  while (not pos_valida):
      # Setear coordenadas random (importamos la librería)
      x = random.randint(50, WIDTH-50)
      y = random.randint(-200, -50)
      
      # Crear nvo_enemigo según el tipo:
      nvo_enemigo = Actor(tipo, (x, y))

      # Verificamos que nuestro nvo_enemigo NO se superponga con otro
      
      #Nota: más adelante veremos collidelist que sería una mejor solución a este caso
      pos_valida = True # Defino como "válida" la posición, hasta que encuentre lo contrario
      
      for nave_enemiga in lista_enemigos:
          # recorro la lista de enemigos y chequeo las colisiones
          if  nvo_enemigo.colliderect(nave_enemiga):
              pos_valida = False
        

  # Cuando ya validé la posición de mi nvo_enemigo, configuro lo demás
  """ Nota: Si yo quiero que la velocidad de los enemigos sea un factor
          de la dificultad del juego, en lugar de ser random p/cada
          nave, puedo crear una variable global llamada "velocidad_naves_enemigas"
          (o algo así) y actualizarlo cuando lo necesite
              
          # Si mis enemigos tienen cambios según su tipo:
    
        if tipo == "enemy":
          *modificamos lo que tengamos que modificar: velocidad, salud, bonus que dropea, etc*
  """

  nvo_enemigo.velocidad = random.randint(4, 8) # o variable global
  # Cuando mi nuevo enemigo está listo, lo agrego a la lista:
  lista_enemigos.append(nvo_enemigo)
  ##########################################

def mov_flota_enemiga():
    
  for nave_enemiga in lista_enemigos:
      if (nave_enemiga.y > (HEIGHT + nave_enemiga.height)): # Si se salió de la pantalla
            # La reciclamos:
            nave_enemiga.y = random.randint(-200, -50)
            nave_enemiga.x = random.randint(50, WIDTH - 50)
            # Nota: si cambiamos la velocidad según la dificultad, modificar ésto:
            nave_enemiga.velocidad = random.randint(4, 8) # o variable global
    
      else:
            nave_enemiga.y += nave_enemiga.velocidad

def comprobar_colisiones():
    global modo_actual
    # Comprobar colisiones con enemigos
    for nave_enemiga in lista_enemigos:
        if nave.colliderect(nave_enemiga):
            modo_actual = "game_over" # Terminamos el juego

def mov_planetas(delta_y):
  for planeta_actual in lista_planetas:
      planeta_actual.y += delta_y

      # Si se sale de la pantalla de juego, lo reciclamos
      if (planeta_actual.y > (HEIGHT + planeta_actual.height)):
          planeta_actual.x = random.randint(0, WIDTH)
          planeta_actual.y = random.randint(-1200, -850)
          planeta_actual.angle = random.randint(0,359)

""" #####################
   # FUNCIONES PG ZERO #
  ##################### """

def draw():
  if (modo_actual == "juego"):
      fondo.draw()

      for planeta in lista_planetas:
          planeta.draw()
      
      for nave_enemiga in lista_enemigos:
        nave_enemiga.draw()
      
      #screen.draw.text(TITLE, center=(300, 100), color="white", background="black")
    
      texto_temp = "Coord: (x: " + str(int(nave.x)) + ", y: " + str(int(nave.y)) + ")"
      screen.draw.text(texto_temp, midleft=(20, 20), color = "white", fontsize = 24)
    
      nave.draw()

  elif (modo_actual == "game_over"):
      fondo.draw()

      for planeta in lista_planetas:
          planeta.draw()

      screen.draw.text("¡TE ESTRELLASTE!", center=(int(WIDTH/2), int(HEIGHT/2)), color = "red", background = "black", fontsize = 48)

      # To-do: agregar mostrar puntuación final
      # To-do: Mostrar cartel "Presione [Enter] para reiniciar"
      #        -> To-Do: agregar función reset_game()

def on_mouse_move(pos):
  if (modo_actual == "juego"):
    nave.pos = pos

"""  #####################
    # INICIALIZAR JUEGO #
   #####################  """

# To-do: convertir a FN p/ iniciar/reiniciar el juego
for e in range(CANT_ENEMIGOS):
  spawn_nvo_enemigo()

##################
# BUCLE DE JUEGO #
##################

def update(dt):
  global modo_actual
  
  if (modo_actual == "juego"):
    mov_planetas(1) # Nota: si modifico el juego para que tenga velocidad variable, asegurarme de actualizar el delta_y
    mov_flota_enemiga()
    comprobar_colisiones()
  
  elif (modo_actual == "game_over"):
    if keyboard.enter:
      modo_actual = "juego"
      # To-Do: agregar función reset_game()