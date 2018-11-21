from os import path
from Entity import Player , Mob
from Structure import Wall , Ground
class Map:
    def __init__(self,NameFile,game):
        self.data = []
        self.name = NameFile
        self.game = game
        self.GameFolder = path.dirname(__file__)
        self.spawn = (0,0)
        self.open()
        self.width = len(self.data[0]) * 32
        self.height = len(self.data) * 32
        self.Initialise()


    def open(self):
        with open(path.join(self.GameFolder,"src",self.name),'rt') as f:
            for line in f:
                self.data.append(line)

    def Initialise(self):
        for row,tiles in enumerate(self.data):
            for col , tile in enumerate(tiles):
                if tile == '1' or tile == '4':
                    Wall.Wall(self.game,col,row,int(tile))
                if tile == '0' or tile == '3':
                    Ground.Ground(col,row,self.game,int(tile))
                if tile == '6':
                    self.game.player = Player.Player(self.game,col * 32,row * 32)
                if tile == '7':
                    self.game.mob = Mob.Mob(self.game,col,row)
                
        
