import pygame
from pygamesimpleobject import *


pygame.init()
screen = pygame.display.set_mode((850, 700)) #create window
pygame.display.set_caption('tank')
clock = pygame.time.Clock()


mineimage = pygame.image.load("examplemedia/mine.png") #load images
tankimage = pygame.image.load("examplemedia/tank.png") #load images


tank = NewObject(image=tankimage, position_x=425, position_y=300) #create objects
mine = NewObject(image=mineimage, position_x=100, position_y=320)
mine2 = NewObject(image=mineimage, position_x=400, position_y=600)

map = TileMap("examplemedia/map.txt","examplemedia/tileset.png",tilesize=(32,32)) #create map


objectslist = [mine,mine2,tank,map]

AddCollision(tank,map) #add collisions
AddCollision(tank,[mine,mine2])


left = False
right = False
move = False
move2 = False


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



    #draw all
    screen.fill((0, 0, 0))
    DrawObjects(screen,objectslist,tank)

    pygame.display.flip() #update screen

    clock.tick(50)  #fps limit
