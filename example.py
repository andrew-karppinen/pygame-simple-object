import pygame

from PygameSimpleObject import *



pygame.init()
screen = pygame.display.set_mode((850, 700)) #create window



robottikuva = pygame.image.load("images/robotti.png") #download images
tasokuva = pygame.image.load("images/taso.png")
maalikuva = pygame.image.load("images/maali.png")


clock = pygame.time.Clock()

#create objects
robot = NewObject(image=robottikuva,position_x=425, position_y=350, gravity_speed = 0.2, jump_strength = 10.0)
block = NewObject(tasokuva, position_x=350, position_y=600)
block2 = NewObject(tasokuva, position_x=600, position_y=400)
block3 = NewObject(maalikuva, position_x=700, position_y=335)
block4 = NewObject(tasokuva, position_x=700, position_y=0)


#add collisions
AddCollision(robot, block)
AddCollision(robot, block2)

robot.AddCamera((block, block2, block4,block3))

robot.image_.set_colorkey((0, 0, 0))

block_left = True
robot_left = False
robot_right = False
ylos = False
alas = False

i = 0

#block4.PlaceObject(50,50)

while True: #main loop
    #event lopp
    for event in pygame.event.get():
        
        #keyboards event
        if event.type == pygame.KEYDOWN:
            if event.key  == pygame.K_UP:
                robot.Jump()
            if event.key == pygame.K_LEFT:
                robot_left = True
            if event.key == pygame.K_RIGHT:
                robot_right = True

            if event.key == pygame.K_t:
                robot.Rotate(i)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                robot_left = False
            if event.key == pygame.K_RIGHT:
                robot_right = False

        if event.type == pygame.QUIT:
            exit() 
        


    if robot_right:
        robot.CameraMoveX(4)
    if robot_left:
        robot.CameraMoveX(-4)


    x,y = robot.ReturnCoordinate(0, 0) #coordinate system

    if block.position_x_ == x + 850:
       block_left = True
    if block.position_x_ == x:
        block_left = False
        
    if block_left:
        block.MoveX(-1)
    else:
        block.MoveX(1)
        
    robot.Gravity()

    i += 1

    if CollisionCheck(robot, block3): #if two object collision
        robot.PlaceObject(50,50)

    block4.Rotate(i)





    #draw all
    screen.fill((0, 0, 0))
    screen.blit(robot.image_, robot.rect_)
    screen.blit(block4.image_,block4.rect_)
    screen.blit(block.image_, block.rect_)
    screen.blit(block2.image_, block2.rect_)
    screen.blit(block3.image_, block3.rect_)

    pygame.draw.circle(screen, (50, 50, 50), robot.ReturnCoordinate(800, 40), 50)

    pygame.display.flip() #update screen
    
    clock.tick(60) #fps limit
