import pygame


def DrawObjects(surface,objects:list):


    for i in range(len(objects)):
        if type(objects[i]) == list:
            for j in range(len(objects[i])):
                surface.blit(objects[i][j].image_,objects[i][j].rect_)
        else:
            surface.blit(objects[i].image_,objects[i].rect_)
