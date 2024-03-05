import pygame



def CollisionCheck(obj1, obj2, obj1_x = None, obj1_y = None, obj2_x = None, obj2_y = None):
    '''
    receive two object 
    return True/False if objects is collision
    '''


    if type(obj1) == list or type(obj2) == list: #if obj1 or obj2 is list
        if type(obj1) == list: #obj1 is list
            for obj in obj1:

                if type(obj2) != list: #obj2 is not list
                    if obj2_x != None and obj2_y != None: #obj2 position is given
                        if CollisionCheck(obj, obj2,obj2_x = obj2_x,obj2_y=obj2_y) == True:
                            return True
                    else: #obj2 position is no given
                        if CollisionCheck(obj, obj2) == True:
                            return True
                else: #obj2 is list
                    if CollisionCheck(obj, obj2) == True:
                        return True


        if type(obj2) == list: #obj2 is list
            for obj in obj2:

                if type(obj1) != list: #obj1 is not list
                    if obj1_x != None and obj1_y != None: #obj1 position is given
                        if CollisionCheck(obj, obj1,obj2_x = obj1_x,obj2_y=obj1_y) == True:
                            return True
                    else: #obj1 position is no given
                        if CollisionCheck(obj, obj1) == True:
                            return True

                if CollisionCheck(obj,obj1) == True:
                    return True

        return False

    if obj1_x == None: #if location no given
        obj1_x = obj1.position_x_
    if obj1_y == None: #if location no given
        obj1_y = obj1.position_y_

    if obj2_x == None: #if location no given
        obj2_x = obj2.position_x_
    if obj2_y == None: #if location no given
        obj2_y = obj2.position_y_


        
    if obj1_y < obj2_y + obj2.object_size_y_:
        if obj1_y + obj1.object_size_y_> obj2_y:

            if obj1_x < obj2_x + obj2.object_size_x_:
                if obj1_x + obj1.object_size_x_ > obj2_x:
                    return True
    return False




def AddCollision(obj1,obj2):
    #Add collision
    #obj1 <-- obj2
    #obj2 <-- obj1

    if type(obj2) == list: #if obj2 is list
        for i in range(len(obj2)):
            if obj2[i].map_object_: #if map object
                if obj2[i].map_setup_ == 2: #if collision tile
                    obj1.collision_objects_.append(obj2[i])
                    obj2[i].collision_objects_.append(obj1)
            else:
                obj1.collision_objects_.append(obj2[i]) #add obejct list
                obj2[i].collision_objects_.append(obj1) #add object list
    else:
        obj1.collision_objects_.append(obj2) #add object list
        obj2.collision_objects_.append(obj1) #add object list

def DelteCollision(obj1,obj2):
    #Delete object in list
    # Todo update this

    #obj1
    for i in range(len(obj1.collision_objects_)):
        if obj2 == obj1.collision_objects_[i]:
            obj1.collision_objects_.pop(i)
            break
    
    #obj2
    for i in range(len(obj2.collision_objects_)):
        if obj1 == obj2.collision_objects_[i]:
            obj2.collision_objects_.pop(i)
            break
