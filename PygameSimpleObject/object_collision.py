import pygame



def CollisionCheck(obj1,obj2):
    '''
    receive two object 
    return True/False if objects is collision
    '''

    if obj1.position_y_ <= obj2.position_y_ + obj2.image_size_y_:
        if obj1.position_y_+ obj1.image_size_y_>= obj2.position_y_:

            if obj1.position_x_<= obj2.position_x_ + obj2.image_size_x_:
                if obj1.position_x_ + obj1.image_size_x_ >= obj2.position_x_:
                    return True

    return False