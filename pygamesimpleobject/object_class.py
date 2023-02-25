import pygame
import math

try: from pygamesimpleobject.object_collision import CollisionCheck #import CollisionCheck function other file
except: from object_collision import CollisionCheck




def Return_x_y(angle, distance):
    '''
    calculates the lengths of the legs of a right triangle from the length of the hypotenuse and the angle
    '''

    x = math.cos(math.radians(angle)) * distance

    y = math.tan(math.radians(angle)) * x

    return (x, y)


def opposite(number):
    return -1 * number



class NewObject:
    def __init__(self,image = None,object_size_x:int = 1,object_size_y:int = 1,position_x: int = 0, position_y: int = 0): #constructor
        self.position_x_ = position_x #screen position
        self.position_y_ = position_y

        self.coordinate_x_ = 0 #moving coordinate system
        self.coordinate_y_ = 0
        self.collision_objects_ = []
        self.camera_objects_ = []

        self.map_object_ = False #if object is map
        self.map_setup_ = None #1 = no collision, 2 = collision,3 = layer 2(draw last, no collision)

        self.tracked_object = False #if the object is followed

        self.SetImage(image,object_size_x,object_size_y) #sets object image and object size

        self.UpdateRect() #update pygame rect object
        self.angle_ = 0


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
        #position --> rect
        self.rect_[0] = self.position_x_
        self.rect_[1] = self.position_y_


    def UpdateRect2(self):
        #rect --> obejct size
        #rect --> position


        self.object_size_x_ = self.rect_[2]
        self.object_size_y_ = self.rect_[3]

        self.position_x_ = self.rect_[0]
        self.position_y_ = self.rect_[1]





    def Rotate(self, angle,option:int = 1):
        """
        Rotate image around center

        option 1 = increases angle value
        option 2 = set angle value
        """
        if option == 1:
            self.angle_ += angle
        elif option == 2:
            self.angle_ = angle

        if self.image_ != None: #only if the image exists
            self.image_ = pygame.transform.rotate(self.original_image_, self.angle_)  #rotate image
            self.rect_ = self.image_.get_rect(center=self.rect_.center)#update rect_
            self.UpdateRect2() #update object position and size

        if self.__Collision(): #if collision
            self.angle_ -= angle #cancel rotate
            self.image_ = pygame.transform.rotate(self.original_image_, self.angle_)  #cancel rotate


            self.rect_ = self.image_.get_rect(center=self.rect_.center) #update rect_

        self.UpdateRect2() #update object position and size



    def ReturnCoordinate(self,x,y):
        #moving coordinate system
        #return screen coordinatte

        x = opposite(x)
        y = opposite(y)

        return(opposite(x-self.coordinate_x_), opposite(y - self.coordinate_y_))


    def PlaceObject(self,x,y):
        #sets object new position

        if self.tracked_object: #if the object is followed
            x,y = self.ReturnCoordinate(x,y)

            distance_x = self.position_x_ - x
            distance_y = self.position_y_ - y


            self.coordinate_x_ += distance_x
            self.coordinate_y_ += distance_y

            for i in range(len(self.camera_objects_)):
                self.camera_objects_[i].position_x_ += distance_x  #place object new location
                self.camera_objects_[i].position_y_ += distance_y
                self.camera_objects_[i].UpdateRect()
        else:
            self.position_x_ = x
            self.position_y_ = y
            self.UpdateRect()

    def AddCamera(self,objectslist: list):
        for i in range(len(objectslist)):
            if type(objectslist[i]) == list: #if index is list
                for j in range(len(objectslist[i])):
                    self.camera_objects_.append(objectslist[i][j])
            else:
                self.camera_objects_.append(objectslist[i])

        self.tracked_object = True

    #test moving methods
    #camera follow object
    def CameraMoveX(self,distance: int):
        if distance > 0:
            number = -1
        if distance < 0:
            number = 1

        for i in range(abs(distance)):
            for j in range(len(self.collision_objects_)): #collision check

                if CollisionCheck(self, self.collision_objects_[j], obj2_x =self.collision_objects_[j].position_x_ + number): #if collision
                    return #exit function

            for k in range(len(self.camera_objects_)): #move
                self.camera_objects_[k].position_x_ += number
                self.camera_objects_[k].UpdateRect()
        for i in range(abs(distance)):
            self.coordinate_x_ += number


    def CameraMoveY(self,distance: int):
        if distance > 0:
            number = -1
        if distance < 0:
            number = 1

        for i in range(abs(distance)):
            for j in range(len(self.collision_objects_)): #collision check

                if CollisionCheck(self, self.collision_objects_[j], obj2_y =self.collision_objects_[j].position_y_ + number): #if collision
                    return #exit function

            for k in range(len(self.camera_objects_)): #move
                self.camera_objects_[k].position_y_ += number
                self.camera_objects_[k].UpdateRect()
        for i in range(abs(distance)):
            self.coordinate_y_ += number


    def Move(self,distance:int):

        x,y = Return_x_y(opposite(self.angle_),distance)

        self.MoveX(int(x))
        self.MoveY(int(y))

    def CameraMove(self,distance:int):

        x, y = Return_x_y(opposite(self.angle_), distance)
        self.CameraMoveX(int(x))
        self.CameraMoveY(int(y))


    def MoveX(self,distance: int):
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

    
    def MoveY(self,distance: int):

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
        


    def __Collision(self,position_x = None,position_y = None): #private method
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


            if obj1_y < obj2.position_y_ + obj2.object_size_y_:
                if obj1_y + self.object_size_y_ > obj2.position_y_:

                    if obj1_x < obj2.position_x_ + obj2.object_size_x_:
                        if obj1_x + self.object_size_x_ > obj2.position_x_:
                            return True
        return False




    def PrintOther(self):
        for i in range(len(self.collision_objects_)):
            print(self.collision_objects_[i])
