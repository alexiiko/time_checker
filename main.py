import pygame as pg
from sys import exit
from settings import *
from button import *
from clock import *
from input_box import *

class App:
    def __init__(self):
        self.clock = pg.time.Clock()

    def draw_window(self):
        SCREEN.fill("#7fa480")
        get_time_button.update()
        clock.update()
        input_box.update()

    def update(self):
        self.clock.tick(FPS)
        pg.display.update()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.QUIT
                exit()
            else:
                input_box.get_input(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw_window()

if __name__ == "__main__":
    app = App()
    app.run()