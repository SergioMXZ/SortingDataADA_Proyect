# Importaciones
#from src.Program import pygame
import pygame
import assets.styles.colors as colors

# clase padre de pantallas
class Screen:
    def __init__(self, screen, program):
        self.screen = screen
        self.program = program
        self.colors = colors
        self.s_w,self.s_h = self.program.screen_size

        i_w, i_h = program.icon_exit.get_size()
        self.r_icon1 = pygame.Rect(self.s_w-50,15, i_w,i_h)
        i_w, i_h = program.icon_back.get_size()
        self.r_icon2 = pygame.Rect(self.s_w-120,15, i_w,i_h)

        self.font_tit = pygame.font.SysFont('Time New Romans', 70)
        self.font_bot1 = pygame.font.SysFont('Time New Romans', 45)

        


    def draw(self):
        "#dibujar la pantalla"
        pass

    def handle_events(self, event):
        "#manejar eventos"
        pass

    def sorting(self, lista):
        "#ordenar datos"
        pass