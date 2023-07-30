import pygame as pg

SCREEN_WIDTH, SCREEN_HEIGHT = 650, 285

SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pg.display.set_caption("Time Checker")
pg.display.set_icon(pg.image.load("assets/clock.png"))

FPS = 60