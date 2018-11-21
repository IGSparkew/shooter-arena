import pygame as pg
from constante import *

class SpriteSheet:
    def __init__(self,filename):
        self.sheet = pg.image.load(filename).convert()

    def get_Image(self,x,y,sizew,sizeh,iscolored):

        image = pg.Surface((sizew,sizeh))

        image.blit(self.sheet,(0,0),(x * sizew,y * sizeh,sizew,sizeh))
        if iscolored:
            image.set_colorkey(Black)
        return image

