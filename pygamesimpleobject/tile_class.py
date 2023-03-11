import pygame

class Tile:
    def __init__(self, image=None, object_size_x: int = 1, object_size_y: int = 1, position_x: int = 0,position_y: int = 0):  # constructor
        self.position_x_ = position_x #screen position
        self.position_y_ = position_y

        self.coordinate_x_ = 0 #moving coordinate system
        self.coordinate_y_ = 0
        self.collision_objects_ = []
        self.SetImage(image,object_size_x,object_size_y) #sets object image and object size

        self.map_object_ = True # object is map
        self.map_setup_ = None #1 = no collision, 2 = collision,3 = layer 2(draw last, no collision)
        self.UpdateRect()


    def SetImage(self,image = None,object_size_x:int = None,object_size_y:int = None):

        if image != None: #if image given
            self.image_ = image
            self.original_image_  = image #used image rotation


            self.object_size_y_ = image.get_height() #set object size to image size
            self.object_size_x_ = image.get_width()
            self.rect_ = self.image_.get_rect(center=(self.image_.get_width(), self.image_.get_height()))  #create rect object

        else: #if image no given
            self.image_ = None
            self.object_size_y_ = object_size_y
            self.object_size_x_ = object_size_x

            self.rect_ = pygame.Rect((0, 0), (1, 1)) #create rect object


    def UpdateRect(self):
        # position --> rect
        self.rect_[0] = self.position_x_
        self.rect_[1] = self.position_y_


