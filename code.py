# CircuitPlaygroundExpress_NeoPixel

import board
from neopixel import (
    NeoPixel
)
from digitalio import DigitalInOut, Direction
import time

RED = (255, 0, 0)
YELLOW = (200, 150, 25)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
BLACK = (0, 0, 0)

TAMANNO = 10
TREN = 1
TIEMPO_ON = 0.2
TIEMPO_OFF = 0.001
COLOR = RED
pixels = NeoPixel(board.NEOPIXEL, TAMANNO, brightness=0.1)

pixels [0:3] = RED

while True:
    pixels[0:TAMANNO] = [ GREEN ] * TAMANNO

    for i in range(TAMANNO):
        pixels[i] = RED

        pixels.show()
        time.sleep(1)


    for i in range(TAMANNO):
        pixels[i] = BLACK
        pixels.show()
        time.sleep(0.3)
