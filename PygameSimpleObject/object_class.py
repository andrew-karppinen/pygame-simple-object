import pygame

try: from PygameSimpleObject.object_collision import CollisionCheck #import CollisionCheck function other file
except: from object_collision import CollisionCheck


#camera follow object



def opposite(number):
    return -1 * number



class NewObject:
    def __init__(self,image = None,object_size_x:int = None,object_size_y:int = None,position_x: int = 0, position_y: int = 0,gravity_speed: float = 0.0,gravity_strength: float = 6.0,jump_strength: float = 0.0,jump_mode: int = 1,jump_collision_mode = 1): #constructor
        self.position_x_ = position_x #screen position
        self.position_y_ = position_y
        self.gravity_value_ = 0.0
        self.gravity_strength_ = gravity_strength
        self.gravity_speed_ = gravity_speed #gravity  < 0 = downwards > 0 = upwards
        self.jump_strength_ = jump_strength
        self.jump_mode_ = jump_mode
        self.jump_collision_mode_ = jump_collision_mode

        self.collision_objects_ = []
        self.camera_objects_ = []

        self.coordinate_x_ = 0 #moving coordinate system
        self.coordinate_y_ = 0

        self.SetImage(image,object_size_x,object_size_y) #sets object image and object size



    def SetImage(self,image = None,object_size_x:int = None,object_size_y:int = None):

        if image != None: #if image given
            self.image_ = image
            if object_size_y != None and object_size_x != None: #if size given
                self.object_size_y_ = object_size_y
                self.object_size_x_ = object_size_x
            else: #if size no given
                self.object_size_y_ = image.get_height() #set object size to image size
                self.object_size_x_ = image.get_width()

        else: #if image no given
            if object_size_y != None and object_size_x != None: #if size given
                self.object_size_y_ = object_size_y
                self.object_size_x_ = object_size_x
            else:
                self.object_size_y_ = 1
                self.object_size_x_ = 1


    def ReturnCoordinate(self,x,y):
        #moving coordinate system
        #return screen coordinatte

        x = opposite(x)
        y = opposite(y)

        return(opposite(x-self.coordinate_x_), opposite(y - self.coordinate_y_))


    def PlaceObject(self,x,y):
        #sets object new position

        x,y = self.ReturnCoordinate(x,y)

        distance_x = self.position_x_ - x
        distance_y = self.position_y_ - y

        print(distance_x,distance_y)
        self.coordinate_x_ += distance_x
        self.coordinate_y_ += distance_y

        for i in range(len(self.camera_objects_)):
            self.camera_objects_[i].position_x_ += distance_x  #place object new location
            self.camera_objects_[i].position_y_ += distance_y

    def AddCamera(self,objectslist: list):
        self.camera_objects_ = objectslist

    #test moving methods
    #camera follow object
    def CameraMoveX(self,distance: int):
        if distance > 0:
            number = -1
        if distance < 0:
            number = 1

        for i in range(abs(distance)):
            for j in range(len(self.collision_objects_)): #collison check

                if CollisionCheck(self, self.collision_objects_[j], obj2_x =self.camera_objects_[j].position_x_ + number): #if collision
                    return #exit function

            for i in range(len(self.camera_objects_)): #move
                self.camera_objects_[i].position_x_ += number
        for i in range(abs(distance)):
            self.coordinate_x_ += number


    def CameraMoveY(self,distance: int):
        if distance > 0:
            number = -1
        if distance < 0:
            number = 1

        for i in range(abs(distance)):
            for j in range(len(self.collision_objects_)): #collison check

                if CollisionCheck(self, self.collision_objects_[j], obj2_y =self.camera_objects_[j].position_y_ + number): #if collision
                    if self.jump_collision_mode_ == 1:  # stop jump
                        self.gravity_value_ = 0.0
                    return #exit function

            for i in range(len(self.camera_objects_)): #move
                self.camera_objects_[i].position_y_ += number

        for i in range(abs(distance)):
            self.coordinate_y_ += number






            



    def MoveX(self,distance: int):
        for i in range(abs(distance)):

            if distance > 0:
                self.position_x_ += 1
            else:
                self.position_x_ += -1


            if self.__Collision(): #if collision
                if distance > 0:
                    self.position_x_ += -1 #cancel move
                else:
                    self.position_x_ += 1 #cancel move
                return 



    
    def MoveY(self,distance: int):

        for i in range(abs(distance)):

            if distance > 0:
                self.position_y_ += 1
            else:
                self.position_y_ += -1


            
            if self.__Collision(): #if collision 

                if self.jump_collision_mode_ == 1: #stop jump
                    self.gravity_value_= 0.0

                if distance > 0:
                    self.position_y_ += -1 #cancel move

                else:
                    self.position_y_ += 1 #cancel move
                return
    
        
    def Gravity(self,camera = True): #method makes gravity

        if camera:
            self.CameraMoveY(int(self.gravity_value_))
        else:
            self.MoveY(int(self.gravity_value_))
        
        if self.gravity_speed_ > 0:
            if self.gravity_value_ < self.gravity_strength_:
                self.gravity_value_ += self.gravity_speed_
        elif self.gravity_speed_ < 0:
            if self.gravity_value_ > opposite(self.gravity_strength_):
                self.gravity_value_ += self.gravity_speed_

    
    def Jump(self): #method makes jump
        if self.jump_mode_ != 0:
            if self.jump_mode_ == 1: #jumps only if the object is above another object
                if self.gravity_speed_ > 0:
                    self.position_y_ += 1
                    if self.__Collision():
                        self.gravity_value_ = opposite(self.jump_strength_)
                        self.position_y_ -= 1 #cancel move
                        
                if self.gravity_speed_ < 0:
                    self.position_y_ -= 1
                    if self.__Collision():
                        self.gravity_value_ = self.jump_strength_
                        self.position_y_ += 1 #cancel move

            elif self.jump_mode_ == 2: #jump in any case
                if self.gravity_speed_ > 0:
                    self.gravity_value_ = opposite(self.jump_strength_)
                else:
                    self.gravity_value_ = self.jump_strength_
                return



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
