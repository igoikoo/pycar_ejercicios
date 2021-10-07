# Import a library of functions called 'pygame'
import pygame
from main_functions import *

# Initialize the game engine
pygame.init()

#call main routine

ancho = int(input("Ancho de la ventana:"))
alto = int(input("Alto de la ventana:"))

size[0] = ancho
size[1] = alto
main2(size)