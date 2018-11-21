import pygame as pg
from constante import *
from Entity import Player
from Structure import Wall , Ground
from map import *
from camera import *

if __name__ == "__main__":

    class Main:

        def __init__(self):
            pg.init()
            pg.mixer.init()
            self.screen = pg.display.set_mode((WIDTH,HEIGHT))
            pg.display.set_caption(TITLE)
            self.run = True
            self.clock = pg.time.Clock()
            self.Sprites = pg.sprite.Group()
            self.Walls = pg.sprite.Group()
            self.Grounds = pg.sprite.Group()
            self.Mob = pg.sprite.Group()
            pg.key.set_repeat(1,1)
            self.new()
            self.loop()


        def loop(self):
            while self.run:
                self.dt = self.clock.tick(FPS) / 1000
                
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.run = False

                self.Update(event)
                self.draw()
            self.Quit()




        def new(self):
            self.map = Map('map2.txt',self)
            self.camera = Camera(self.map.width ,self.map.height )


        def Update(self,event):

            self.Sprites.update()
            self.Walls.update()
            self.camera.update(self.player)

        def draw(self):
            self.screen.fill(Black)
            self.Grounds.draw(self.screen)
            for g in self.Grounds:
                self.screen.blit(g.image, self.camera.apply(g))

            self.Mob.draw(self.screen)
            for sp in self.Sprites:

                self.screen.blit(sp.image,self.camera.apply(sp))



            pg.display.flip()
         

        def Quit(self):
            pg.quit()
    
    main = Main()                


