import requests
import pygame as pg
from settings import *
from input_box import *

class Button:
    def __init__(self):
        pg.font.init()
        self.button_img = pg.image.load("assets/get_time_button.png")
        self.rect = self.button_img.get_rect(center = (125, 155))

        self.clicked = False

        self.font = pg.font.Font(None, 32)

        self.error_message = ""
        self.error_message_surf = self.font.render(self.error_message, True, "white")
        self.show_error = False

        self.hour = 0
        self.minute = 0

    def blit_error(self):
        if self.show_error:
            SCREEN.blit(self.error_message_surf, (30,220))

    def return_time(self) -> int:
        return self.hour, self.minute

    def make_request(self):
        timezone = input_box.return_input()
        api_url = f'https://timeapi.io/api/Time/current/zone?timeZone={timezone}'
        response = requests.get(api_url)
        data = response.json()

        if response.status_code == requests.codes.ok and "hour" in data and "minute" in data:
            self.show_error = False
            self.hour, self.minute = int(data["hour"]), int(data["minute"])
        else:
            self.show_error = True
            self.error_message = f"Error: 400. Invalid Timezone."
            self.error_message_surf = self.font.render(self.error_message, True, "white")
            self.hour, self.minute = 0, 0 

    def check_click(self):
        x,y = pg.mouse.get_pos()

        if self.rect.collidepoint(x,y):
            if self.clicked == False and pg.mouse.get_pressed()[0]:
                self.make_request()
                self.clicked = True

        self.reset_click()

    def reset_click(self):
        if pg.mouse.get_pressed()[0] == False:
            self.clicked = False

    def draw(self):
        SCREEN.blit(self.button_img, self.rect)
    
    def update(self):
        self.blit_error()
        self.check_click()
        self.draw()

get_time_button = Button()
get_time_button.update()