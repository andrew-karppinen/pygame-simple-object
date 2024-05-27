import pygame
import math

from pygamesimpleobject import *



def Return_x_y(angle, distance)->tuple:
    '''
    calculates the lengths of the legs of a right triangle from the length of the hypotenuse and the angle
    '''


    scaled_distance = distance

    x = math.cos(math.radians(angle)) * scaled_distance

    y = math.sin(math.radians(angle)) * scaled_distance

    return (x,y)




def opposite(number):
    return -1 * number



class NewObject:
    def __init__(self,image = None,position_x: int = 0, position_y: int = 0,object_size_x:int = 1,object_size_y:int = 1): #constructor

        self.image_ = None


        self.position_x_ = position_x #screen position
        self.position_y_ = position_y

        self.collision_objects_ = []
        self.rounded_collision_check_ = False
        self.circle_radius_ = 20

        self.map_object_ = False #Object is not map


        if image != None: #if image given
            self.SetImage(image) #sets object image, object size and create create object
        else: #if image no given
            #set object size:
            self.object_size_x_ = object_size_x
            self.object_size_y_ = object_size_y
            self.rect_ = pygame.Rect((0, 0), (1, 1)) #create rect object

        self.UpdateRect() #update pygame rect object
        self.angle_ = 0


        #Variables that are not visible here:
        #self.object_size_x_
        #self.object_size_y_
        #self.rect_

        #self.__original_image_




    def SetImage(self,image)->None:

        self.image_ = image
        self.image_.set_colorkey((0,0,0)) #the black areas in the image are transparent
        self.__original_image_  = image #used image rotation

        self.object_size_y_ = image.get_height() #set object size to image size
        self.object_size_x_ = image.get_width()
        self.rect_ = self.image_.get_rect(center=(self.image_.get_width(), self.image_.get_height()))  #create rect object

        self.UpdateRect()




    def UpdateRect(self)->None:
        #position --> rect
        self.rect_[0] = self.position_x_
        self.rect_[1] = self.position_y_


    def UpdateRect2(self)->None:
        #rect --> obejct size
        #rect --> position


        self.object_size_x_ = self.rect_[2]
        self.object_size_y_ = self.rect_[3]

        self.position_x_ = self.rect_[0]
        self.position_y_ = self.rect_[1]





    def Rotate(self, angle,option:int = 1)->None:
        """
        Rotate image around center

        option 1 = increases angle value
        option 2 = set angle value
        """
        original_angle = self.angle_

        if option == 1:
            self.angle_ += angle
        elif option == 2:
            self.angle_ = angle

        if self.image_ != None: #only if the image exists
            self.image_ = pygame.transform.rotate(self.__original_image_, self.angle_)  #rotate image
            self.rect_ = self.image_.get_rect(center=self.rect_.center)#update rect_
            self.UpdateRect2() #update object position and size

        if self.__Collision(): #if collision
            self.angle_ = original_angle #cancel rotate
            if self.image_ != None:  #only if the image exists
                self.image_ = pygame.transform.rotate(self.__original_image_, self.angle_)  #cancel image rotate
                self.rect_ = self.image_.get_rect(center=self.rect_.center) #update rect_


        self.UpdateRect2() #update object position and size

        if self.image_ != None: #only if the image exists
            self.image_.set_colorkey((0, 0, 0))  # the black areas in the image are transparent






    def PlaceObject(self,x,y)->None:
        #sets object new position

        self.position_x_ = x
        self.position_y_ = y
        self.UpdateRect()




    def Move(self,distance:int)->None:

        x,y = Return_x_y(opposite(self.angle_),distance)

        y = round(y)
        x = round(x)

        self.MoveX(x)
        self.MoveY(y)



    def MoveX(self,distance: int)->None:
        for i in range(abs(distance)):
            if distance > 0:
                self.position_x_ += 1
            else:
                self.position_x_ += -1

            # Todo update this
            if self.__Collision(): #if collision
                if distance > 0:
                    self.position_x_ += -1 #cancel move
                else:
                    self.position_x_ += 1 #cancel move
                return
        self.UpdateRect()

    
    def MoveY(self,distance: int)->None:

        for i in range(abs(distance)):

            if distance > 0:
                self.position_y_ += 1
            else:
                self.position_y_ += -1


            #Todo update this
            if self.__Collision(): #if collision

                if distance > 0:
                    self.position_y_ += -1 #cancel move

                else:
                    self.position_y_ += 1 #cancel move
                return
        self.UpdateRect()
        


    def __Collision(self,position_x = None,position_y = None)->bool: #private method
        #return True/False
        #if this object collision
        if position_x == None:
            obj1_x = self.position_x_
        else:
            obj1_x = position_x #if location give

        if position_y == None:
            obj1_y = self.position_y_
        else:
            obj1_y = position_y #if location give


        for i in range(len(self.collision_objects_)):
            obj2 = self.collision_objects_[i]

            if CollisionCheck(self,obj2,obj1_x,obj1_y) == True: #if collide
                return  True


        return False




    def GetCollisionObjects(self):
        return self.collision_objects_
