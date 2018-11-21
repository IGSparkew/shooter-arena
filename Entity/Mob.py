import pygame as pg
from utile import SpriteSheet

class Mob(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game = game
        self.groups = self.game.Mob,self.game.Sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.sheet = SpriteSheet.SpriteSheet("res/mob.png")
        self.image = self.sheet.get_Image(0,0,32,30,True)

        self.rect = self.image.get_rect()
        self.rect.x = x*32
        self.rect.y = y*32
