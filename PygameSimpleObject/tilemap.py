import pygame
from PygameSimpleObject import *


#tilemap test

def StringToList(string,rowswidth,rowcount):


    '''
    String to 2d list
    characters are separated comma
    '''



    list = [['' for i in range(rowswidth)] for j in range(rowcount)]  #create 2d list

    x = 0 
    y = 0 

    
    for i in range(len(string)): 
        if string[i] == "\n":  #if newline
            y += 1 #nextline
            x = 0 

        elif string[i] != ",": #if not ","

            list[y][x] += string[i] #add character to list


        elif string[i] == ",": #jos pilkku lisää uuden alkion
            x += 1 #next index

    
    
    return list #return 2d list


def ReadMap(filepath):

    
    '''
    read txt file to 2d list

    using StringToList function
    retrun list,rows width, rows count
    '''

    file = open(filepath, "r")

    rows = file.read().splitlines()

    file.close()

    rowscount = ""
    rowswidth = ""
    i = 0
    string = ""


    while i < len(rows[0]): #read first line
        if rows[0][i] == ",":
            i += 1
            break
        rowscount += rows[0][i]
        i += 1

    while i < len(rows[0]): #read first line
        if rows[0][i] == ";":
            break
        rowswidth += rows[0][i]
        i += 1


    rowscount = int(rowscount)
    rowswidth= int(rowswidth)


    for i in range(1,rowscount +1):
        string += rows[i]
        string += "\n"


    maplist = StringToList(string,rowswidth,rowscount)

    return(maplist,rowswidth,rowscount)


def TileMap(mapfile_path:str,tileimage_path):
    '''
    Makes tilemap  from txt file
    tiles is objects

    Example file:
    8,8;
    1b,1b,1,1,2,1,1,1,1,1
    1,2,1,1,1,1,1,1,1,1
    1,2,1,1,1b,2,1,1,1,1
    1,2,1,1,1,1,1,2,1,1
    1,2,1,1,1,2,1,1,1,1
    1,2,1,1,1,2,1,0c,0c,0c
    
    number = tile image
    
    char:
    a = no collision
    b = collision
    c = baground tile
    d = no tile
    '''


    tile1 = pygame.image.load("examplemedia/tile1.png")  # load images
    tile2 = pygame.image.load("examplemedia/tile2.png")

    images = [tile1, tile2]

    maplist, rowwidth, rowcout = ReadMap(mapfile_path)  # read txt file

    objectlist = []


    #make tiles objects
    for y in range(rowcout):
        for x in range(rowwidth):
            number = ""
            for i in range(len(maplist[y][x])):
                if maplist[y][x][i].isnumeric():
                    number += maplist[y][x][i]
                else:
                    char = maplist[y][x][i]



            number = int(number)

            if char != "d":
                if number == 0: #if no image
                    objectlist.append(NewObject(image = None,position_x=x*32,position_y=y*32))
                else:
                    objectlist.append(NewObject(image = images[number-1],position_x=x*32,position_y=y*32))

                objectlist[-1].map_object_ = True
                if char == "a": #no collision tile
                    objectlist[-1].map_setup_ = 1
                elif char == "b": #collision tile
                    print(objectlist[-1].position_y_)
                    objectlist[-1].map_setup_ = 2
                elif char == "c": #baground tile(no collision)
                    objectlist[-1].map_setup_ = 3




    return(objectlist)




