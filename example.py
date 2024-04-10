import pygame
from pygamesimpleobject import *


pygame.init()
screen = pygame.display.set_mode((850, 700)) #create window
pygame.display.set_caption('tank')
clock = pygame.time.Clock()


mineimage = pygame.image.load("examplemedia/mine.png") #load images
tankimage = pygame.image.load("examplemedia/soldier.bmp") #load images
bulletimage =  pygame.image.load("examplemedia/bullet.png") #load images

tank = NewObject(image=tankimage, position_x=425, position_y=450) #create objects
mine = NewObject(image=mineimage, position_x=100, position_y=320)
mine2 = NewObject(image=mineimage, position_x=400, position_y=600)

map = TileMap("examplemedia/testikartta/testikartta.txt","examplemedia/testikartta/tileset.png",tilesize=(32,32)) #create map


bullet =  NewObject(bulletimage)

objectslist = [mine,mine2,tank,map]

#AddCollision(tank,map) #add collisions
AddCollision(tank,[mine,mine2])


left = False
right = False
move = False
move2 = False

i = 1



def ObjectCollidesLine(start_pos,end_pos, obj):


    box_x = obj.position_x_
    box_y = obj.position_y_
    box_width = obj.object_size_x_
    box_height =obj.object_size_y_

    start_x = start_pos[0]
    start_y = start_pos[1]
    end_x = end_pos[0]
    end_y = end_pos[1]


    # Tarkistetaan, leikkaako viiva laatikon vasemman reunan
    if start_x < box_x and end_x >= box_x:
        y_intersection = start_y + (box_x - start_x) * (end_y - start_y) / (end_x - start_x)
        if box_y <= y_intersection <= box_y + box_height:
            return True

    # Tarkistetaan, leikkaako viiva laatikon oikean reunan
    if start_x > box_x + box_width and end_x <= box_x + box_width:
        y_intersection = start_y + (box_x + box_width - start_x) * (end_y - start_y) / (end_x - start_x)
        if box_y <= y_intersection <= box_y + box_height:
            return True

    # Tarkistetaan, leikkaako viiva laatikon yläreunan
    if start_y < box_y and end_y >= box_y:
        x_intersection = start_x + (box_y - start_y) * (end_x - start_x) / (end_y - start_y)
        if box_x <= x_intersection <= box_x + box_width:
            return True

    # Tarkistetaan, leikkaako viiva laatikon alareunan
    if start_y > box_y + box_height and end_y <= box_y + box_height:
        x_intersection = start_x + (box_y + box_height - start_y) * (end_x - start_x) / (end_y - start_y)
        if box_x <= x_intersection <= box_x + box_width:
            return True

    # Jos mikään ylläolevista ei toteudu, viiva ei osu laatikkoon
    return False


while True: #main loop
    #event lopp
    for event in pygame.event.get():
        #keyboards event
        if event.type == pygame.KEYDOWN:

            if event.key  == pygame.K_UP:
                move = True
            if event.key == pygame.K_DOWN:
                move2 = True
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_UP:
                move = False
            if event.key == pygame.K_DOWN:
                move2 = False

        if event.type == pygame.QUIT:
            exit()


    if left:
        tank.Rotate(2)
    if right:
        tank.Rotate(-2)
    if move:
        tank.Move(5)
    if move2:
        tank.Move(-5)



    #print(CollisionCheck(tank,map,check_all_tiles=False))
    #print(ReturnTilesHitByObject(map,tank))
    #print(ReturnTileFrom(map,33,31))

    #draw all
    screen.fill((0, 0, 0))
    DrawObjects(screen,objectslist,tank)


    pygame.display.flip() #update screen

    clock.tick(50)  #fps limit

