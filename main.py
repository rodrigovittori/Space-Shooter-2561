#pgzero

""" > M6.L1 · Actividad #2: "Función on_mouse_move"

Kenney assets:

Kodland: https://kenney.nl/assets/space-shooter-extension
Extra: https://kenney.nl/assets/space-shooter-redux
Planetas: https://kenney.nl/assets/planets
UI: https://kenney.nl/assets/ui-pack-sci-fi
"""

WIDTH = 600
HEIGHT = 450

TITLE = "GUERRA GALÁCTICA"
FPS = 30

# Objetos y Variables
nave = Actor("ship", (300,300))
fondo = Actor("space")

# Funciones PGZERO
def draw():
  fondo.draw()
  texto_temp = "Coord: (x: " + str(int(nave.x)) + ", y: " + str(int(nave.y)) + ")"
  screen.draw.text(texto_temp, midleft=(20, 20), color = "white", fontsize = 24)

  screen.draw.text(TITLE, center=(300, 100), color="white", background="black")
  nave.draw()
    
def on_mouse_move(pos):
  nave.pos = pos