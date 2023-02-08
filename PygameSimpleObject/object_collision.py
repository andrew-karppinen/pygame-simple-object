import pygame



def CollisionCheck(obj1, obj2, obj1_x = None, obj1_y = None, obj2_x = None, obj2_y = None):
    '''
    receive two object 
    return True/False if objects is collision
    '''


    
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

    if type(obj2) == list: #if obj2 is list
        for i in range(len(obj2)):
            if obj2[i].map_object_: #if map object
                if obj2[i].map_setup_ == 2: #if collision tile
                    obj1.collision_objects_.append(obj2[i])
                    obj2[i].collision_objects_.append(obj1)



            else:
                obj1.collision_objects_.append(obj2[i])
                obj2[i].collision_objects_.append(obj1)
    else:
        obj1.collision_objects_.append(obj2) #add object list
        obj2.collision_objects_.append(obj1) #add object list

def DelteCollision(obj1,obj2):
    #Delete object in list


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
