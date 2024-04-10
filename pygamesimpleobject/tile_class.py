import pygame

class Tile:
    #class variables
    map_size = [] #x,y
    tileset = []
    tilesize = (32,32) #x,y default: 32,32


    def __init__(self, tilenumber, position_x: int = 0,position_y: int = 0,data:int=None):  # constructor
        self.position_x_ = position_x #screen position
        self.position_y_ = position_y

        self.coordinate_x_ = 0 #moving coordinate system
        self.coordinate_y_ = 0
        self.collision_objects_ = []

        self.image_number_ = 0

        self.tile_number_ = 0

        self.SetImage(tilenumber)  # sets object image and object size

        self.map_object_ = True # object is map
        self.tile_setup_ = None #1 = no collision, 2 = collision,3 = layer 2(draw last, no collision)

        self.data_ = data #1-500 or None

        self.UpdateRect()




    def SetImage(self, image_number):

        '''
        Change tileimage
        indexing start from 1
        0 is noneimage
        '''


        if abs(image_number) > len(Tile.tileset): #invalid tilenumber
            raise Exception("tilelist index out of range")

        self.image_number_ = image_number


        self.rect_ = Tile.tileset[self.image_number_].get_rect(center=(Tile.tilesize[0], Tile.tilesize[1]))  #create rect object


    @property
    def image_(self):
        return Tile.tileset[self.image_number_]
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


