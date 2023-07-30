import pygame as pg
from settings import *

class InputBox:
    def __init__(self):
        pg.font.init()

        self.rect = pg.Rect(30, 50, 175, 40)

        self.text = ""
        self.active = False

        self.font = pg.font.Font(None, 32)

        self.info_text = "Type timezone in:"
        self.info_surf = self.font.render(self.info_text, True, "white")

        self.show_error = False

    def get_input(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == True and self.rect.collidepoint(event.pos):
                self.active = True
            else: 
                self.active = False
        elif event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    return self.text
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
    
    def show_error_message(self):
        if self.show_error:
            SCREEN.blit(self.font.render("Timezone must be a string.", True, "white"), (0,0))

    def return_input(self) -> str:
        if self.text.isalpha:
            return self.text
        else:
            self.show_error = True
        
    def draw_self(self):
        rect_color = (255,255,255) if self.active else (222,222,222)
        pg.draw.rect(SCREEN, rect_color, self.rect, 3)

        text_surf = self.font.render(self.text, True, "white")
        self.rect.w = max(100, text_surf.get_width() + 20)
        SCREEN.blit(text_surf, (self.rect.x + 10, self.rect.y + 10))
        SCREEN.blit(self.info_surf, (30, 20))

    def draw_right_rect(self):
        pg.draw.rect(SCREEN, "white", self.right_rect, 3)

    def update(self):
        self.show_error_message()
        self.draw_self()

input_box = InputBox()

input_box.update()