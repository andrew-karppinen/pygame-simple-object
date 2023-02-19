import pygame
from PygameSimpleObject import *
from PIL import Image
#tilemap test

def StringToList(string,rowswidth,rowcount):


    '''
    String to 2d list Retrun list
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


        elif string[i] == ",":
            x += 1 #next index

    
    
    return list #return 2d list


def ReadFile(filepath):

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
    rowswidth = int(rowswidth)

    print(rowscount,rowswidth)

    for i in range(1,rowscount +1):
        string += rows[i]
        string += "\n"


    maplist = StringToList(string,rowswidth,rowscount)

    return(maplist,rowswidth,rowscount)


def ReadTileset(tileset_path,tilesize = (32,32)):
    '''
    tilesize = (x,y)

    Read tileset image
    using pillow library

    convert pillow image to pygame surface

    retun images as list
    '''

    image = Image.open(tileset_path) #open imagefile
    tilesetsize = image.size
    imagelist = []

    if tilesetsize[0] % tilesize[0] != 0 or tilesetsize[1] % tilesize[1] != 0: #check is image size correct
        raise Exception("invalid tileset image size")


    mapheight = tilesetsize[1] // tilesize[1] #map height in tiles


    for i in range(mapheight):#crop image to tiles
        for j in range(0,tilesetsize[0],tilesize[0]):

            #Setting the points for cropped image
            left = j
            top = i*tilesize[1]
            right = j+tilesize[0]
            bottom = i*tilesize[1] + tilesize[1]

            croppedimage = image.crop((left, top, right, bottom)) #crop image

            #convert image to pygame surface
            mode = image.mode
            data = croppedimage.tobytes()
            imagelist.append(pygame.image.fromstring(data, tilesize, mode)) #add cropped image to list


    return(imagelist)



def TileMap(mapfile_path:str,tileset_path,tilesize = (32,32)):
    '''
    tilesize = (x,y)

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
    c = layer2
    d = no tile

    a,b = layer 1(draw first)
    c = layer2 (draw last)

    read tileset image from left to right and from top to bottom

    '''

    images = ReadTileset(tileset_path,tilesize) #read tileset
    maplist, rowwidth, rowcout = ReadFile(mapfile_path)  #read txt file

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
                    objectlist.append(NewObject(image = None,position_x=x*tilesize[0],position_y=y*tilesize[1]))
                else:
                    objectlist.append(NewObject(image = images[number-1],position_x=x*tilesize[0],position_y=y*tilesize[1]))

                objectlist[-1].map_object_ = True
                if char == "a": #no collision tile
                    objectlist[-1].map_setup_ = 1
                elif char == "b": #collision tile
                    objectlist[-1].map_setup_ = 2
                elif char == "c": #layer2 (draw last) (no collision)
                    objectlist[-1].map_setup_ = 3




    return(objectlist)




