import pygame

from PygameSimpleObject import *




pygame.init()
naytto = pygame.display.set_mode((850, 700)) #create window



robottikuva = pygame.image.load("images/robotti.png") #download images
tasokuva = pygame.image.load("images/taso.png")
maalikuva = pygame.image.load("images/maali.png")


klock = pygame.time.Clock()

#create objects
robot = NewObject(robottikuva, position_x=425, position_y=350, gravity_speed = 0.2, jump_strength = 10.0)
block = NewObject(tasokuva, position_x=350, position_y=600)
block2 = NewObject(tasokuva, position_x=600, position_y=400)
block3 = NewObject(maalikuva, position_x=700, position_y=335)

#add collisions
AddCollision(robot, block)
AddCollision(robot, block2)

lista = [block, block2, block3]
robot.AddCamera(lista)

block_left = True
robot_left = False
robot_right = False
ylos = False
alas = False


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




    if CollisionCheck(robot, block3): #if two object collision

        robot.position_x_,robot.position_y_ = 100,100


    #draw all
    naytto.fill((0,0,0))
    naytto.blit(robot.image_, (robot.position_x_, robot.position_y_))
    naytto.blit(block.image_, (block.position_x_, block.position_y_))
    naytto.blit(block2.image_, (block2.position_x_, block2.position_y_))
    naytto.blit(block3.image_, (block3.position_x_, block3.position_y_))
    pygame.draw.circle(naytto, (50,50,50), robot.ReturnCoordinate(50, 50), 50)

    pygame.display.flip() #update screen
    
    klock.tick(60) #fps limit
