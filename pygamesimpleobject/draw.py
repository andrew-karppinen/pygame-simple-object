import pygame
from copy import deepcopy




def DrawImage(surface, image,position:tuple,tracked_object:object=None):
    '''
    Draw given pygame image on given pygame surface.
    tracked_object is optionaly
    '''


    if tracked_object == None:
        surface.blit(image, position)

    else: #tracked object is given
        screen_sixe_x, screen_sixe_y = surface.get_size()  # get surface size

        screen_center_x = (tracked_object.position_x_+tracked_object.object_size_x_//2) - screen_sixe_x // 2 #calculate center of screen
        screen_center_y = (tracked_object.position_y_+tracked_object.object_size_y_//2) - screen_sixe_y // 2 #calculate center of screen


        surface.blit(image, (position[0]-screen_center_x, position[1]-screen_center_y))


def DrawObjects(surface, objects:list, tracked_object:object=None):
    '''
    Draw given objects image on given pygame surface.
    tracked_object is optionaly
    '''


    list1 = [] #draw first
    list2 = []
    list3 = [] #draw last

    screen_sixe_x, screen_sixe_y = surface.get_size() #get surface size

    #order objects
    for i in range(len(objects)):
        if type(objects[i]) == list:
            for j in range(len(objects[i])):#if list
                if objects[i][j].map_object_: #if map object
                    if objects[i][j].tile_setup_ == 1 or objects[i][j].tile_setup_ == 2: #if map type 1 or 2
                        list1.append(objects[i][j]) #list1
                    else:#if map type 3
                        list3.append(objects[i][j])  #list3
                else:
                    list2.append(objects[i][j]) #list2
        else:
            list2.append(objects[i]) #list2

    if tracked_object == None: #if tracked object no given
        #draw objects
        for i in (list1):
            if i.image_ != None: #only if the image exists
                surface.blit(i.image_,i.rect_)
        for i in (list2):
            if i.image_ != None: #only if the image exists
                surface.blit(i.image_,i.rect_)
        for i in (list3):
            if i.image_ != None: #only if the image exists
                surface.blit(i.image_, i.rect_)

    else: #camera tracking system:
        #draw objects

        screen_center_x = (tracked_object.position_x_+tracked_object.object_size_x_//2) - screen_sixe_x // 2 #calculate center of screen
        screen_center_y = (tracked_object.position_y_+tracked_object.object_size_y_//2) - screen_sixe_y // 2 #calculate center of screen


        for i in (list1):
            rect_copy = deepcopy(i.rect_)
            rect_copy[0] -= screen_center_x
            rect_copy[1] -= screen_center_y

            if i.image_ != None: #only if the image exists
                surface.blit(i.image_,rect_copy) #draw object

        for i in (list2):
            rect_copy = deepcopy(i.rect_)
            rect_copy[0] -= screen_center_x
            rect_copy[1] -= screen_center_y

            if i.image_ != None: #only if the image exists
                surface.blit(i.image_,rect_copy) #draw object

        for i in (list3):
            rect_copy = deepcopy(i.rect_)
            rect_copy[0] -= screen_center_x
            rect_copy[1] -= screen_center_y
            if i.image_ != None: #only if the image exists
                surface.blit(i.image_, rect_copy) #draw object