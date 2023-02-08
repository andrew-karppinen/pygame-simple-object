import pygame


def DrawObjects(surface,objects:list):


    list1 = [] #draw first
    list2 = []
    list3 = [] #draw last

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



    #draw objects
    for i in (list1):
        surface.blit(i.image_,i.rect_)
    for i in (list2):
        surface.blit(i.image_,i.rect_)
    for i in (list3):
        surface.blit(i.image_, i.rect_)