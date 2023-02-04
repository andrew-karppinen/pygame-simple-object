import pygame

from PygameSimpleObject import *



pygame.init()
screen = pygame.display.set_mode((850, 700)) #create window
clock = pygame.time.Clock()

tankimage = pygame.image.load("images/tank.png") #load images

tank = NewObject(image=tankimage, position_x=425, position_y=350)


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
        tank.Move(5)


    #draw all
    screen.fill((0, 0, 0))
    screen.blit(tank.image_, tank.rect_)
    pygame.display.flip()  # update screen

    clock.tick(60)  # fps limit
