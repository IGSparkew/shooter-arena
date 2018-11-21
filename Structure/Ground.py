import pygame as pg
from constante import *

class Ground(pg.sprite.Sprite):
    def __init__(self,x,y,game,id):
        self.game = game
        self.group =  self.game.Grounds
        pg.sprite.Sprite.__init__(self,self.group)
        if id == 0:
            self.image = pg.image.load("res/Lunar.png").convert()
        elif id == 3:
            self.image = pg.image.load("res/wood.png").convert()
        else:
            self.image = pg.image.load("res/Lunar.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x * 32
        self.rect.y = y * 32
