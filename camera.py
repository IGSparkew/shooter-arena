import pygame as pg
from constante import *


class Camera:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.cam = pg.Rect(0,0,self.width,self.height)

    def apply(self,entity):
        return entity.rect.move(self.cam.topleft)

    def update(self,target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)
        x = min(0 , x)
        y = min(0 , y)
        x = max(-(self.width - WIDTH) + 32, x)
        y = max(-(self.height - HEIGHT)  , y)
        self.cam = pg.Rect(x,y,self.width,self.height)

