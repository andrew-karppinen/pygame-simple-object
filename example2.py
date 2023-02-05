import pygame

from PygameSimpleObject import *



pygame.init()
screen = pygame.display.set_mode((850, 700)) #create window
clock = pygame.time.Clock()

tankimage = pygame.image.load("examplemedia/tank.png") #load images
mineimage = pygame.image.load("examplemedia/mine.png")
mineimage.set_colorkey((0,0,0))
tankimage.set_colorkey((0, 0, 0))

tank = NewObject(image=tankimage, position_x=425, position_y=350)
mine = NewObject(image=mineimage, position_x=100, position_y=320)
mine2 = NewObject(image=mineimage, position_x=400, position_y=300)

map =TileMap("examplemedia/map.txt",None)#create map

objectslist = [mine,mine2,map]

tank.AddCamera([mine,mine2,map])

left = False
right = False
move = False


while True: #main loop
    #event lopp
    for event in pygame.event.get():
        #keyboards event
        if event.type == pygame.KEYDOWN:
            if event.key  == pygame.K_UP:
                move = True
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

        if event.type == pygame.QUIT:
            exit()


    if left:
        tank.Rotate(2)
    if right:
        tank.Rotate(-2)
    if move:
        tank.CameraMove(5)


    #draw all
    screen.fill((0, 0, 0))
    DrawObjects(screen,[map,mine,mine2,tank])

    pygame.display.flip()  # update screen

    clock.tick(60)  #fps limit
