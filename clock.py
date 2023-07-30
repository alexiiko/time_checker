import pygame as pg
from settings import *
from button import * 

class Clock:
    def __init__(self):
        pg.font.init()

        self.clock = pg.transform.scale(pg.image.load("assets/clock.png"), (250,250))
        self.hour_arrow = pg.image.load("assets/hour_arrow.png")
        self.minute_arrow = pg.image.load("assets/minute_arrow.png")

        self.font = pg.font.Font(None, 50)

        self.digital_clock_text = "00:00"
        self.digital_clock_surf = self.font.render(self.digital_clock_text, True, "white")

        self.hour = 0
        self.minute = 0
    
    def draw_clock(self):
        SCREEN.blit(self.clock, (350, 30))

    def draw_digital_clock(self):
        hour, minute = get_time_button.return_time()
        if self.minute == 0:
            self.digital_clock_text = f"{hour}:{minute}0"
        elif self.minute < 10:
            self.digital_clock_text = f"{hour}:0{minute}"
        else:
            self.digital_clock_text = f"{hour}:{minute}"
        self.digital_clock_surf = self.font.render(self.digital_clock_text, True, "white")
        SCREEN.blit(self.digital_clock_surf, (550, 15))

    def set_arrows(self, hour: int, minute: int):
        if hour == 0:
            hour_arrow_angle = 0
        else:
            hour_arrow_angle = 360 - (((hour  + 12)* 30) + ((minute/10) * 5))
        
        if minute == 0:
            minute_arrow_angle = 0
        else:
            minute_arrow_angle = 360 - (minute * 6)

        hour_arrow_copy = pg.transform.rotate(self.hour_arrow, hour_arrow_angle)
        minute_arrow_copy = pg.transform.rotate(self.minute_arrow, minute_arrow_angle)

        SCREEN.blit(hour_arrow_copy, (475 - int(hour_arrow_copy.get_width()) / 2, 155 - int(hour_arrow_copy.get_height()) / 2))
        SCREEN.blit(minute_arrow_copy, (475 - int(minute_arrow_copy.get_width()) / 2, 155 - int(minute_arrow_copy.get_height()) / 2))

    def get_hour_and_minute(self):
        self.hour, self.minute = get_time_button.return_time()

    def update(self):
        self.get_hour_and_minute()
        self.draw_clock()
        self.set_arrows(self.hour, self.minute)
        self.draw_digital_clock()

clock = Clock()
clock.update()