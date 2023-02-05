import pygame

from PygameSimpleObject import *



pygame.init()
screen = pygame.display.set_mode((850, 700)) #create window
clock = pygame.time.Clock()

tankimage = pygame.image.load("examplemedia/tank.png") #load images
mineimage = pygame.image.load("examplemedia/mine.png")

tank = NewObject(image=tankimage, position_x=425, position_y=350)
mine = NewObject(image=mineimage, position_x=100, position_y=320)
mine2 = NewObject(image=mineimage, position_x=400, position_y=300)
TileMap(None,None)

tank.AddCamera([mine,mine2])

left = False
right = False
move = False
tank.image_.set_colorkey((0, 0, 0))

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
        tank.Rotate(3)
    if right:
        tank.Rotate(-3)
    if move:
        tank.CameraMove(5)


    #draw all
    screen.fill((0, 0, 0))
    screen.blit(mine.image_, mine.rect_)
    screen.blit(mine2.image_, mine2.rect_)
    screen.blit(tank.image_, tank.rect_)
    pygame.display.flip()  # update screen

    clock.tick(60)  #fps limit
