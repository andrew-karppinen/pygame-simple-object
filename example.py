import pygame
from pygamesimpleobject import *

pygame.init()
screen = pygame.display.set_mode((850, 700)) #create window
pygame.display.set_caption('tank')
clock = pygame.time.Clock()

tankimage = pygame.image.load("examplemedia/tank.png") #load images
mineimage = pygame.image.load("examplemedia/mine.png")
bulletimage = pygame.image.load("examplemedia/bullet.png")

mineimage.set_colorkey((0,0,0))
tankimage.set_colorkey((0, 0, 0))

tank = NewObject(image=tankimage, position_x=425, position_y=350) #create objects
mine = NewObject(image=mineimage, position_x=100, position_y=320)
mine2 = NewObject(image=mineimage, position_x=400, position_y=600)
bullet = NewObject(image=bulletimage)
map = TileMap("examplemedia/map.txt","examplemedia/tileset.png",tilesize=(32,32)) #create map

objectslist = [mine,mine2,bullet,tank,map]

AddCollision(tank,map)
AddCollision(tank,[mine,mine2])
tank.AddCamera([mine,mine2,map])



left = False
right = False
move = False
move2 = False

shoot = False

while True: #main loop
    #event lopp
    for event in pygame.event.get():
        #keyboards event
        if event.type == pygame.KEYDOWN:
            if event.key  == pygame.K_t:
                shoot = True
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

    if shoot: #shoot
        bullet.PlaceObject(tank.position_x_+tank.object_size_x_//2,tank.position_y_+tank.object_size_y_//2)
        bullet.Rotate(tank.angle_,2)
        shoot = False

    if left:
        tank.Rotate(2)
    if right:
        tank.Rotate(-2)
    if move:
        tank.CameraMove(5)
    if move2:
        tank.CameraMove(-5)

    bullet.Move(15)

    #draw all
    screen.fill((0, 0, 0))
    DrawObjects(screen,objectslist)

    pygame.display.flip() #update screen

    clock.tick(60)  #fps limit
