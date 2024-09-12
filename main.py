#pgzero

# M6.L1: Actividad #1: "Viaje al espacio"

"""

Kenney assets:

Kodland: https://kenney.nl/assets/space-shooter-extension
Extra: https://kenney.nl/assets/space-shooter-redux
Planetas: https://kenney.nl/assets/planets
UI: https://kenney.nl/assets/ui-pack-sci-fi

"""

WIDTH = 600
HEIGHT = 450

TITLE = "GUERRA GALACTICA"
FPS = 30

# Objetos y Variables
nave = Actor("ship", (300,300))
fondo = Actor("space")

# Funciones PGZERO
def draw():
  fondo.draw()
  nave.draw()
  screen.draw.text(TITLE, center=(300, 100), color="white", background="black")