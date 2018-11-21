import pygame as pg
from Entity import Player
from utile import SpriteSheet
from constante import *
from math import *
class Bullet(pg.sprite.Sprite):
    def __init__(self,game,x,y,angle):
        self.game = game
        self.groups = self.game.Sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.sheet = SpriteSheet.SpriteSheet("res/Bullet.png")
        self.angle = angle
        self.image = self.sheet.get_Image(0,0,17,65,True)
        self.image = pg.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedA = 0.1
        self.framex = 0
        self.max = 2
        self.speed = 5

    def update(self):
        self.image = self.sheet.get_Image(floor(self.framex),0,17,65,True)
        self.image = pg.transform.rotate(self.image, self.angle)
        self.animation()
        if self.angle == 90:
            self.rect.x -= self.speed
        elif self.angle == -90:
            self.rect.x += self.speed
        elif self.angle == 0:
            self.rect.y -= self.speed
        elif self.angle == 360:
            self.rect.y += self.speed
        for wall in self.game.Walls:
            if self.rect.colliderect(wall.rect):
                self.kill()


    def animation(self):
        self.framex += self.speedA
        if floor(self.framex)  > self.max:
            self.framex = 0