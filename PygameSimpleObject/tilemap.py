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

    using map function
    
    retrun list,rows width, rows count
    '''

    file = open(filepath, "r")

    rows = file.read().splitlines()

    file.close()

    rowscount = ""
    rowswidth = ""
    i = 0
    string = ""


    while i < len(rows[0]):
        if rows[0][i] == ",":
            i += 1
            break
        rowscount += rows[0][i]
        i += 1

    while i < len(rows[0]):
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




def TileMap(mapfile_path,tileimage_path):


    tile1 = pygame.image.load("examplemedia/tile1.png") #loadimage
    tile2 = pygame.image.load("examplemedia/tile2.png")


    maplist,rowwidth,rowcout = ReadMap(mapfile_path)

    
    objectlist = []



            

    #make tiles objects
    for y in range(rowcout):
        for x in range(rowwidth):
            if maplist[y][x] == "1":
                objectlist.append(NewObject(image = tile1,position_x=x*32,position_y=y*32))
                
            elif maplist[y][x] == "2":
                objectlist.append(NewObject(image = tile2,position_x=x*32,position_y=y*32))



    return(objectlist)




