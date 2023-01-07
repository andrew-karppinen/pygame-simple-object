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




        
    if obj1_y <= obj2_y + obj2.image_size_y_:
        if obj1_y + obj1.image_size_y_>= obj2_y:

            if obj1_x <= obj2_x + obj2.image_size_x_:
                if obj1_x + obj1.image_size_x_ >= obj2_x:
                    return True



    return False