import pygame

#TEST
#camera follow object test


def opposite(number):
    return -1 * number




class NewObject:
    def __init__(self,image:pygame.Surface,position_x: int = 0, position_y: int = 0,gravity_speed: float = 0.0,gravity_strength: float = 6.0,jump_strength: float = 0.0,jump_mode: int = 1,jump_collision_mode = 1): #constructor
        self.position_x_ = position_x
        self.position_y_ = position_y
        self.gravity_value_ = 0.0
        self.gravity_strength_ = gravity_strength
        self.gravity_speed_ = gravity_speed #gravity  < 0 = downwards > 0 = upwards
        self.jump_strength_ = jump_strength
        self.jump_mode_ = jump_mode
        self.jump_collision_mode_ = jump_collision_mode
        
        
        self.image_ = image #pygame image object
        self.image_size_y_ = image.get_height()
        self.image_size_x_ = image.get_width()

        self.collision_objects_ = []
        self.other_objects_ = []


    def AddCamera(self,objectslist: list):
        self.other_objects_ = objectslist
            



    #object moving methods camera test
    def CameraMoveX(self,distance: int):

        for i in range(len(self.other_objects_)):
            
            for j in range(abs(distance)):

                if distance > 0:
                    
                    self.other_objects_[i].position_x_ -= 1
                else:
                    self.other_objects_[i].position_x_ += 1


                if self.__Collision(): #if collision
                    if distance > 0:
                        self.other_objects_[i].position_x_ += 1 #cancel move
                    else:
                        self.other_objects_[i].position_x_ -= 1 #cancel move
                    return 



    
    def CameraMoveY(self,distance: int):

        for i in range(len(self.other_objects_)):

            for j in range(abs(distance)):

                if distance > 0:
                    self.other_objects_[i].position_y_ -= 1
                else:
                    self.other_objects_[i].position_y_ += 1


                if self.__Collision(): #if collision
                    if distance > 0:
                        self.other_objects_[i].position_y_ += 1 #cancel move
                    else:
                        self.other_objects_[i].position_y_ -= 1 #cancel move
                    return 

        #object moving methods
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
    
        
    def Gravity(self): #method makes gravity

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

            elif self.jump_mode_ == 2:
                if self.gravity_speed_ > 0:
                    self.gravity_value_ = opposite(self.jump_strength_)
                else:
                    self.gravity_value_ = self.jump_strength_
                return





    def __Collision(self): #private method
        #return True/False
        #if this object collision



        for i in range(len(self.collision_objects_)):
            obj = self.collision_objects_[i]


            if self.position_y_ < obj.position_y_ + obj.image_size_y_:
                if self.position_y_+ self.image_size_y_ > obj.position_y_:
                    
                    if self.position_x_< obj.position_x_ + obj.image_size_x_:
                        if self.position_x_ + self.image_size_x_ > obj.position_x_:
                            return True

        return False

        



    def PrintOther(self):
        for i in range(len(self.collision_objects_)):
            print(self.collision_objects_[i])
