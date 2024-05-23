# Importaciones
from Screen import Screen, pygame

class Menu(Screen):
    def __init__(self, screen, program):
        super().__init__(screen, program)
        self.program = program
        #titulo_1
        self.t1 = self.font_tit.render(
            'Sorting Data', True, self.colors.SILVER, None)
        t1_w , t1_h = self.t1.get_size(); self.t1_x = (self.s_w-t1_w)//2; self.t1_y=t1_h
        #botones
        buttons_inf = [ ('  Bubble Sort  ', self.colors.GREEN),
                        ('  Selection Sort  ', self.colors.GREEN),
                        ('  Merge Sort  ', self.colors.GREEN),
                        ('  Insertion Sort  ', self.colors.GREEN),
                        ('  Quick Sort  ', self.colors.GREEN),
                        ('  Heap Sort  ', self.colors.GREEN),
                        (' Counting Sort  ', self.colors.GREEN),
                        ('  Radix Sort  ', self.colors.GREEN),
                        ('  Bucket Sort  ', self.colors.GREEN) ]
        self.buttons = []
        ant_y = self.t1_y
        for b_inf in buttons_inf:
            bt, br, ant_y = self.r_button(*b_inf, ant_y)
            self.buttons.append((bt, br))


    def r_button(self, text, color, ant_y):
        text_obj = self.font_bot1.render(text, True, color,None)
        w, h = text_obj.get_size()
        x = (self.s_w - w) // 2
        y = (h + ant_y) + 20
        button_rect = pygame.Rect(x, y, w, h)
        return text_obj, button_rect, y

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        "#fondo"; self.screen.fill(self.colors.DARK_GRAY)
        "#encabezado"
        "-titulo_1"; self.screen.blit(self.t1, (self.t1_x,5))
        "-icono-salida"
        if self.r_icon1.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, self.colors.RED, self.r_icon1)
        self.screen.blit(self.program.icon_exit, self.r_icon1)

        "#botones"
        for text, rect in self.buttons:
            if rect.collidepoint(mouse_pos):
                pygame.draw.rect(
                self.screen, self.colors.SILVER_DARK_D, rect, border_radius=8)
            self.screen.blit(text, rect)

        pygame.display.flip()


    def handle_events(self, event):
        if event.type == pygame.QUIT:
            self.program.quit_pygame()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                "#bubble"; self.program.set_screen(
                    self.program.bubble_sort)
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if self.buttons[0][1].collidepoint(mouse_pos):
                "#bubble"; self.program.set_screen(
                    self.program.bubble_sort)
            if self.r_icon1.collidepoint(mouse_pos):
                self.program.quit_pygame()


    def sorting(self, lista):
        pass
