#pgzero
import random

""" > M6.L2 · Actividad #5: "Colisiones de proyectiles"

Kenney assets:

Kodland: https://kenney.nl/assets/space-shooter-extension
Extra: https://kenney.nl/assets/space-shooter-redux
Planetas: https://kenney.nl/assets/planets
UI: https://kenney.nl/assets/ui-pack-sci-fi

Objetivo: Agregar colisiones a los proyectiles
Prox. Actividad: (Adicionales): Puntuación y Reiniciar partida

Paso Nº 1) Modificar la función colisiones para que, en caso de un proyectil impactar una nave enemiga o un meteorito, lo destruya
Paso Nº 2) Agregamos un bucle for que compruebe la colisión entre naves enemigas y proyectiles
           > en caso de colisión, spawnearemos un nuevo enemigo 
Paso Nº 3) Agregamos un bucle for que compruebe la colisión entre meteoritos y proyectiles
           > en caso de colisión, spawnearemos un nuevo meteorito

           
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
CANT_METEOROS = 4 # Cantidad de meteoros a spawnear
modo_actual = "menu" # Valores posibles: "juego" / "game_over" / "menu"

nave = Actor("ship", (300,300))
fondo = Actor("space")

# Modelos Naves
tipo1 = Actor("ship1", (100, 225))
tipo2 = Actor("ship2", (300, 225))
tipo3 = Actor("ship3", (500, 225))

# Listas
lista_enemigos = []
lista_planetas = []
lista_meteoritos = []
lista_proyectiles = []

""" ****************************** [ PLANETAS ] ****************************** """

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

def mov_planetas(delta_y):
  for planeta_actual in lista_planetas:
      planeta_actual.y += delta_y

      # Si se sale de la pantalla de juego, lo reciclamos
      if (planeta_actual.y > (HEIGHT + planeta_actual.height)):
          planeta_actual.x = random.randint(0, WIDTH)
          planeta_actual.y = random.randint(-1200, -850)
          planeta_actual.angle = random.randint(0,359)

""" ****************************** [ ENEMIGOS ] ****************************** """

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

      for meteorito in lista_meteoritos:
          # recorro la lista de meteoritos y chequeo las colisiones
          if  nvo_enemigo.colliderect(meteorito):
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

""" ****************************** [ METEORITOS ] ****************************** """

def spawn_nvo_meteorito(tipo=""):

  # Determinar tipo de meteorito a añadir:
  if tipo == "":
      tipo = "meteor"
  
  # To-do: permitir que haya más de un tipo de meteorito
  pos_valida = False

  while (not pos_valida):
      # Setear coordenadas random (importamos la librería)
      x = random.randint(50, WIDTH-50)
      y = random.randint(-200, -50)
      
      # Crear nvo_enemigo según el tipo:
      nvo_meteorito = Actor(tipo, (x, y))

      # Verificamos que nuestro nvo_meteorito NO se superponga con otro
      
      #Nota: más adelante veremos collidelist que sería una mejor solución a este caso
      pos_valida = True # Defino como "válida" la posición, hasta que encuentre lo contrario

      for nave_enemiga in lista_enemigos:
          # recorro la lista de enemigos y chequeo las colisiones
          if  nvo_meteorito.colliderect(nave_enemiga):
              pos_valida = False
      
      for meteorito in lista_meteoritos:
          # recorro la lista de meteoritos y chequeo las colisiones
          if  nvo_meteorito.colliderect(meteorito):
              pos_valida = False

  # Cuando ya validé la posición de mi nvo_metorito, configuro lo demás
  """ Nota: ver nota en spawn_nvo_enemigo  """

  nvo_meteorito.velocidad = random.randint(5, 10) # o variable global
  # Cuando mi nuevo meteorito está listo, lo agrego a la lista:
  lista_meteoritos.append(nvo_meteorito)
  ##########################################
    
def mov_meteoritos():
    
  for meteorito in lista_meteoritos:
      if (meteorito.y > (HEIGHT + meteorito.height)): # Si se salió de la pantalla
            # Lo reciclamos:
            meteorito.y = random.randint(-200, -50)
            meteorito.x = random.randint(50, WIDTH - 50)
            # Nota: si cambiamos la velocidad según la dificultad, modificar ésto:
            meteorito.velocidad = random.randint(5, 10) # o variable global
    
      else:
            meteorito.y += meteorito.velocidad

""" ****************************** [ PROYECTILES ] ****************************** """
def mov_proyectiles():
    for p in lista_proyectiles:
        if (p.y < -p.height): # Si se salió de la pantalla
            lista_proyectiles.remove(p)
        else:
            # Nota: si cambiamos la velocidad de los proyectiles según power-ups, modificar aquí:
            p.y -= 10 # velocidad de proyectiles

""" ****************************** [ COLISIONES ] ****************************** """

def comprobar_colisiones():
    global modo_actual
    # Comprobar colisiones con enemigos
    for nave_enemiga in lista_enemigos:
        if nave.colliderect(nave_enemiga):
            modo_actual = "game_over" # Terminamos el juego

        for p in lista_proyectiles:
            if p.colliderect(nave_enemiga):
                # To-do: aumentar puntuación (eliminé enemigo)
                # To-do: agregar explosión
                lista_enemigos.remove(nave_enemiga)
                lista_proyectiles.remove(p)
                spawn_nvo_enemigo() 

    for meteorito in lista_meteoritos:
        if nave.colliderect(meteorito):
            modo_actual = "game_over" # Terminamos el juego

        for p in lista_proyectiles:
            if p.colliderect(meteorito):
                # To-do: aumentar puntuación (eliminé meteorito)
                # To-do: agregar explosión
                lista_meteoritos.remove(meteorito)
                lista_proyectiles.remove(p)
                spawn_nvo_meteorito()

""" #####################
   # FUNCIONES PG ZERO #
  ##################### """

def draw():
  if (modo_actual == "juego"):
      fondo.draw()

      for planeta in lista_planetas:
          planeta.draw()

      for meteorito in lista_meteoritos:
          meteorito.draw()

      for proyectil in lista_proyectiles:
          proyectil.draw()
      
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

  elif (modo_actual == "menu"):
      fondo.draw()
    
      screen.draw.text("ELIGE TU NAVE", center=(int(WIDTH/2), int(HEIGHT/4)), color = "white", background="black", fontsize = 36)

      tipo1.draw()
      tipo2.draw()
      tipo3.draw()
    
def on_mouse_move(pos):
  if (modo_actual == "juego"):
    nave.pos = pos

def on_mouse_down(button, pos):
    global modo_actual

    if ((modo_actual == "menu") and (tipo1.collidepoint(pos))):
        nave.image = "ship1"
        modo_actual = "juego"
        
    elif ((modo_actual == "menu") and (tipo2.collidepoint(pos))):
        nave.image = "ship2"
        modo_actual = "juego"
    
    elif ((modo_actual == "menu") and (tipo3.collidepoint(pos))):
        nave.image = "ship3"
        modo_actual = "juego"

    ########################

    if ((modo_actual == "juego") and (button == mouse.LEFT)):
        nvo_proyectil = Actor("missiles", nave.pos)
        # NOTA: si quiero tener distintos tipos de proyectiles con distintas velocidades debería agregar un atributo al Actor
        #       según el tipo de proyectil será su velocidad y daño pero
        # NOTA 2: Puedo agregar un timer que controle el cooldown/recarga entre disparos
        lista_proyectiles.append(nvo_proyectil)

"""  #####################
    # INICIALIZAR JUEGO #
   #####################  """

# To-do: convertir a FN p/ iniciar/reiniciar el juego
for e in range(CANT_ENEMIGOS):
  spawn_nvo_enemigo()

for m in range(CANT_METEOROS):
  spawn_nvo_meteorito()

##################
# BUCLE DE JUEGO #
##################

def update(dt):
  global modo_actual
  
  if (modo_actual == "juego"):
    mov_planetas(1) # Nota: si modifico el juego para que tenga velocidad variable, asegurarme de actualizar el delta_y
    mov_meteoritos()
    mov_flota_enemiga()
    mov_proyectiles()
    comprobar_colisiones()
  
  elif (modo_actual == "game_over"):
    if keyboard.enter:
      modo_actual = "juego"
      # To-Do: agregar función reset_game()