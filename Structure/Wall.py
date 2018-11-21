import pygame as pg
from constante import *
from utile import SpriteSheet

class Wall(pg.sprite.Sprite):
    def __init__(self,game,x,y,id):
        self.game = game
        self.groups = self.game.Sprites,self.game.Walls
        pg.sprite.Sprite.__init__(self,self.groups)
        if id == 1:
            self.image = pg.image.load("res/Wall.png").convert()
        elif id == 4:
            self.sheet = SpriteSheet.SpriteSheet("res/chest.png")
            self.image = self.sheet.get_Image(0,0,33,33,False)
        self.rect = self.image.get_rect()
        self.rect.x = x * 32
        self.rect.y = y * 32
