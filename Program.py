# Importaciones
import pygame
import sys
from Menu import Menu
from Bubble_Sort import Bubble_Sort

class Program:
    def __init__(self):
        "#Inicializa Pygame"; pygame.init()
        "#Crea la ventana del juego"
        self.screen_size = (800, 600)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Sorting Data")

        "#iconos"
        self.icon_exit = pygame.image.load("images\exit.png")
        self.icon_back = pygame.image.load("images\go_back.png")
        
        "#Crea las respectivas Ventanas"
        self.menu = Menu(self.screen, self)
        self.bubble_sort = Bubble_Sort(self.screen, self)

        "#Pantalla por defecto"
        self.current_screen = self.menu

    def set_screen(self, screen):
        "#Cambia de Ventana";self.current_screen = screen

    def run(self):
        # Bucle principal del juego
        while True:
            "#Maneja eventos"
            for event in pygame.event.get():
                self.current_screen.handle_events(event)

            "#Dibuja la pantalla actual"
            self.current_screen.draw()

            "#Actualiza la pantalla"
            pygame.display.update()


    def quit_pygame(self):
        print("Closed Program")
        pygame.quit()
        sys.exit()
