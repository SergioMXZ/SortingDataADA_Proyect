# Importaciones
from Screen import Screen, pygame
import time

class Bubble_Sort(Screen):
    def __init__(self, screen, program):
        super().__init__(screen, program)
        #titulo_1
        self.lista = []
        self.t1 = self.font_tit.render(
            'Bubble Sort', True, self.colors.SILVER, None)
        t1_w , t1_h = self.t1.get_size(); self.t1_x = (self.s_w-t1_w)//2; self.t1_y=t1_h

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        "#fondo"; self.screen.fill(self.colors.SILVER_DARK)
        "#encabezado"
        "-fondo"; pygame.draw.rect(self.screen, self.colors.DARK_GRAY,rect=(0,0,self.s_w,60))
        "-b_atras"; 
        "-titulo_1"; self.screen.blit(self.t1, (self.t1_x,5))
        "-icono-salida"
        if self.r_icon2.collidepoint(mouse_pos):
            pygame.draw.circle(self.screen, self.colors.GREEN,(self.s_w-104,31),18)
        self.screen.blit(self.program.icon_back, self.r_icon2)
        
        pygame.display.flip()

    def handle_events(self, event):
        if event.type == pygame.QUIT:
            self.program.quit_pygame()
        elif event.type == pygame.KEYDOWN:
            pass
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if self.r_icon2.collidepoint(mouse_pos):
                "menu"; self.program.set_screen(
                    self.program.menu)
            #elif
    class number():
        def __init__(self, number:int, state:str, change:str, color):
            self.number = number
            self.state = state #= selec, no_selec
            self.change = change #= change, no_change
            self.color = color #= [YELLOW=Y, RED=R, WHITE=W, GREEN=G]


    def draw_numbers(self, numbers):
        x, y = (1,1)
        for num in numbers:
            #pygame.draw.circle(self.screen, self.colors.GREEN,(self.s_w-104,31),18)
            #self.screen.blit(self.t1, (self.t1_x,5))
            #self.t1 = self.font_tit.render(
            #    'Bubble Sort', True, self.colors.SILVER, None)
            pygame.draw.circle(self.screen, self.colors.WHITE, )
            pass

    def sorting(self, list):
        # Sorting whith bubble sort
        numbers_list = []
        for num in list:
            numbers_list.append(self.number(num,"no_selec","no_change","B"))
        
        for i in range(len(list)):
            numbers_list[i].self.state = "selec"
            for j in range(0, len(list) - i - 1):
                numbers_list[j].self.change = "change"
                numbers_list[j+1].self.change = "change"

                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
                    interc = True
                #pintamos
                #sleep(1.5)
                numbers_list[j].self.change = "no_change"

            numbers_list[i].self.state = "no_selec"


            


