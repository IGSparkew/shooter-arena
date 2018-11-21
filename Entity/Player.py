import pygame as pg
from constante import *
from utile import SpriteSheet
from math import *
from Entity import Bullet

class Player(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game = game
        self.groups = self.game.Sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.sheet = SpriteSheet.SpriteSheet("res/hero.png")
        self.framex = 0
        self.speedA = 0.5
        self.max = 7
        self.image = self.sheet.get_Image(0,0,32,32,True)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.angle = 0
        self.timer = 20

    def update(self):

        self.image = self.sheet.get_Image(floor(self.framex),0,32,32,True)
        self.image = pg.transform.rotate(self.image, self.angle)

        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            self.move(0, -self.speed)
            self.animation()
            self.angle = 0
        if keys[pg.K_a]:
            self.move(-self.speed, 0)
            self.animation()
            self.angle = 90
        if keys[pg.K_s]:
            self.move(0, self.speed)
            self.animation()
            self.angle = 360
        if keys[pg.K_d]:
            self.move(self.speed, 0)
            self.animation()
            self.angle = - 90
        if keys[pg.K_f] and self.timer == 20:
            self.timer = 0
            Bullet.Bullet(self.game,self.rect.x,self.rect.y,self.angle)

        if self.timer < 20:
            self.timer +=1


    def animation(self):
        self.framex += self.speedA
        if floor(self.framex) > self.max:
            self.framex = 0


    def move(self,dx = 0,dy = 0):
        if dx != 0:
            self.Move_Axis(dx,0)
        if dy != 0:
            self.Move_Axis(0,dy)

    def Move_Axis(self,dx = 0,dy = 0):
        self.rect.x += dx
        self.rect.y += dy

        if enumerate(self.game.Walls) != 0:
            for wall in self.game.Walls:

                if dx > 0 and self.rect.colliderect(wall.rect):
                    self.rect.right = wall.rect.left
                if dx < 0 and self.rect.colliderect(wall.rect):
                    self.rect.left = wall.rect.right
                if dy > 0 and self.rect.colliderect(wall.rect):
                    self.rect.bottom = wall.rect.top
                if dy < 0 and self.rect.colliderect(wall.rect):
                    self.rect.top = wall.rect.bottom
