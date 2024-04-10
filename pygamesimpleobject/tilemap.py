import pygame
from pygamesimpleobject import *
from PIL import Image







def ReturnTilesWithData(tilemap:list, data_number:int):

    tile_list = []

    for i in tilemap: #iterate map
        if i.data_ != None: #if data tile
            if i.data_ == data_number: #check data number
                tile_list.append(i.tile_number_)
    return(tile_list)

def ReturnTilesHitByObject(map:list,object):
    '''
    Return the tiles that the object hits
    '''
    tiles = []
    counter = 0

    for i in range(len(map)):
        if CollisionCheck(map[i],object,check_all_tiles=True):
            tiles.append(counter)

        counter += 1

    return tiles

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



def TileMap(mapfile_path:str,tileset_path:str,tilesize = (32,32)):
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
    0 = no image (image is only black)

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

    Tile.tileset = images #set tileset to Tile class
    Tile.tilesize = tilesize #set tilesize to Tile class
    Tile.tileset.insert(0, pygame.Surface(Tile.tilesize))

    #make tiles objects

    counter = 1
    for y in range(rowcout):
        for x in range(rowwidth):
            image_number = ""


            data = None

            is_data = False
            data_index = maplist[y][x].find("e")

            if data_index != -1: #if data tile
                is_data = True
                data = int(maplist[y][x][data_index+1:])


            for i in range(len(maplist[y][x])):

                if is_data == True and i == data_index:
                    break

                if maplist[y][x][i].isnumeric():
                    image_number += maplist[y][x][i]
                else:
                    char = maplist[y][x][i]


            image_number = int(image_number)

            if char != "d": #create objects
                if image_number == 0: #if no image
                    objectlist.append(Tile(0,position_x=x*tilesize[0],position_y=y*tilesize[1],data=data))
                else:
                    objectlist.append(Tile(image_number,position_x=x*tilesize[0],position_y=y*tilesize[1],data=data))

                objectlist[-1].tile_number_ = counter

                if char == "a": #no collision tile
                    objectlist[-1].map_setup_ = 1
                elif char == "b": #collision tile
                    objectlist[-1].map_setup_ = 2
                elif char == "c": #layer2 (draw last) (no collision)
                    objectlist[-1].map_setup_ = 3


            counter += 1

    return(objectlist)




