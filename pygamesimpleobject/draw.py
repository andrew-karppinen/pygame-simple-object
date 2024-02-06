import pygame
from copy import  deepcopy

def DrawObjects(surface, objects:list, tracked_object:object=None):


    list1 = [] #draw first
    list2 = []
    list3 = [] #draw last

    screen_sixe_x, screen_sixe_y = surface.get_size() #get surface size

    #order objects
    for i in range(len(objects)):
        if type(objects[i]) == list:
            for j in range(len(objects[i])):#if list
                if objects[i][j].map_object_: #if map object
                    if objects[i][j].map_setup_ == 1 or objects[i][j].map_setup_ == 2: #if map type 1 or 2
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
            surface.blit(i.image_,i.rect_)
        for i in (list2):
            surface.blit(i.image_,i.rect_)
        for i in (list3):
            surface.blit(i.image_, i.rect_)

    else: #camera tracking system:
        #draw objects
        for i in (list1):
            rect_copy = deepcopy(i.rect_)
            rect_copy[0] -= tracked_object.position_x_ - screen_sixe_x // 2
            rect_copy[1] -= tracked_object.position_y_ - screen_sixe_y // 2

            surface.blit(i.image_,rect_copy) #draw object

        for i in (list2):
            rect_copy = deepcopy(i.rect_)
            rect_copy[0] -= tracked_object.position_x_ - screen_sixe_x // 2
            rect_copy[1] -= tracked_object.position_y_ - screen_sixe_y // 2

            surface.blit(i.image_,rect_copy) #draw object

        for i in (list3):
            rect_copy = deepcopy(i.rect_)
            rect_copy[0] -= tracked_object.position_x_ - screen_sixe_x // 2
            rect_copy[1] -= tracked_object.position_y_ - screen_sixe_y // 2

            surface.blit(i.image_, rect_copy) #draw object