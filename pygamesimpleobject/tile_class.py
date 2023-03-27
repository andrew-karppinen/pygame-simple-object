import pygame

class Tile:
    #class variables
    tileset = []

    tilesize = (32,32) #x,y default: 32,32


    def __init__(self, tilenumber, position_x: int = 0,position_y: int = 0):  # constructor
        self.position_x_ = position_x #screen position
        self.position_y_ = position_y

        self.coordinate_x_ = 0 #moving coordinate system
        self.coordinate_y_ = 0
        self.collision_objects_ = []

        self.tilenumber_ = 0

        Tile.tileset.insert(0,pygame.Surface(Tile.tilesize))


        self.SetImage(tilenumber)  # sets object image and object size

        self.map_object_ = True # object is map
        self.map_setup_ = None #1 = no collision, 2 = collision,3 = layer 2(draw last, no collision)
        self.UpdateRect()



    def SetImage(self,tilenumber):

        '''
        Change tileimage
        indexing start from 1
        0 is noneimage
        '''


        if abs(tilenumber) > len(Tile.tileset): #invalid tilenumber
            raise Exception("tilelist index out of range")

        self.tilenumber_ = tilenumber


        self.rect_ = Tile.tileset[self.tilenumber_-1].get_rect(center=(Tile.tilesize[0], Tile.tilesize[1]))  #create rect object


    @property
    def image_(self):


        return Tile.tileset[self.tilenumber_]
    @property
    def object_size_x_(self):
        return Tile.tilesize[0]
    @property
    def object_size_y_(self):
        return Tile.tilesize[1]

    def UpdateRect(self):

        # position --> rect
        self.rect_[0] = self.position_x_
        self.rect_[1] = self.position_y_


