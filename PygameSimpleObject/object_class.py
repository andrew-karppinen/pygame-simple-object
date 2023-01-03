import pygame

def opposite(number):
    return -1 * number




class Object:
    def __init__(self,image:pygame.Surface,position_x: int = 0, position_y: int = 0,gravity_strength: float = 0.2,jump_strength: float = 20.0): #constructor
        self.position_x_ = position_x
        self.position_y_ = position_y
        self.gravity_value = 0.0 #gravity value   < 0 = downwards > 0 = upwards
        self.jump_strength_ = jump_strength
        self.gravity_strength_ = gravity_strength
        
        self.image_ = image #pygame image object
        self.image_size_y_ = image.get_height()
        self.image_size_x_ = image.get_width()

        self.other_object_ = []


    
    #object moving methods
    def MoveX(self,distance: int):
        for i in range(abs(distance)):

            if distance > 0:
                self.position_x_ += 1
            else:
                self.position_x_ += -1


            if self.Collision(): #if collision
                if distance > 0:
                    self.position_x_ += -1 #retract move
                else:
                    self.position_x_ += 1 #retract move
                return None



    
    def MoveY(self,distance: int):

        for i in range(abs(distance)):

            if distance > 0:
                self.position_y_ += 1
            else:
                self.position_y_ += -1

            
            if self.Collision(): #if collision

                if distance > 0:
                    self.position_y_ += -1 #retract move
                else:
                    self.position_y_ += 1 #retract move
                return None


    
        
    def Gravity(self): #method makes gravity
        

        self.MoveY(opposite(int(self.gravity_value))) 

        if self.gravity_value > -5.0:
            self.gravity_value -= self.gravity_strength_ 
    

    
    def Jump(self): #method makes jump

        #jump only if object is on other object
        self.position_y_ += 1


        if self.Collision():
            self.gravity_value = self.jump_strength_
        



    def AddCollision(self,obj):
        '''
        parameter is reference other object 
        add collision on this
        '''

        
        self.other_object_.append(obj) #add object list


    def DeleteCollision(self,obj):
        '''
        Delete object in list
        '''

        
        for i in range(len(self.other_object_)):
            if obj == self.other_object_[i]:
                self.other_object_.pop(i)
                break


    def Collision(self):
        #return True/False
        #if two object collision



        for i in range(len(self.other_object_)):
            obj = self.other_object_[i]


            if self.position_y_ <= obj.position_y_ + obj.image_size_y_:
                if self.position_y_+ self.image_size_y_ >= obj.position_y_:
                    
                    if self.position_x_<= obj.position_x_ + obj.image_size_x_:
                        if self.position_x_ + self.image_size_x_ >= obj.position_x_:
                            return True

        return False

        



    def PrintOther(self):
        for i in range(len(self.other_object_)):
            print(self.other_object_[i])
