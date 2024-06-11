# Importaciones
import pygame

import sys, os
# Agregar el directorio raiz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Program:
    def __init__(self):
        #Importaciones locales
        from views.Menu import Menu
        from views.Bubble_Sort import Bubble_Sort

        "#Inicializa Pygame"; pygame.init()
        "#Crea la ventana del juego"
        self.screen_size = (800, 600)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Sorting Data")

        "#iconos"
        self.icon_exit = pygame.image.load("assets\images\exit.png")
        self.icon_back = pygame.image.load("assets\images\go_back.png")
        
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
