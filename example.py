import pygame

from PygameSimpleObject import *




pygame.init()
naytto = pygame.display.set_mode((850, 700)) #create window



robottikuva = pygame.image.load("images/robotti.png") #download images
tasokuva = pygame.image.load("images/taso.png")
maalikuva = pygame.image.load("images/maali.png")


kello = pygame.time.Clock()

#create objects
robotti = NewObject(robottikuva,position_x=200,position_y=100,gravity_speed = 0.2,jump_strength = 10.0)
taso = NewObject(tasokuva,position_x=100,position_y=600)
taso2 = NewObject(tasokuva,position_x=600,position_y=400)
maali = NewObject(maalikuva,position_x=700,position_y=335)

#add collisions
AddCollision(robotti,taso)
AddCollision(robotti,taso2)

lista = [taso,taso2,maali]
robotti.AddCamera(lista)

tasovasemmalle = False
vasemmalle = False
oikealle = False
ylos = False
alas = False

while True: #main loop
    #event lopp
    for tapahtuma in pygame.event.get():
        
        #keyboards event
        if tapahtuma.type == pygame.KEYDOWN: 
            if tapahtuma.key  == pygame.K_UP:
                robotti.Jump()
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = True
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = True

        if tapahtuma.type == pygame.KEYUP: 
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = False
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = False

        if tapahtuma.type == pygame.QUIT: 
            exit() 
        

    if oikealle:
        robotti.CameraMoveX(4)
    if vasemmalle:
        robotti.CameraMoveX(-4)


    if taso.position_x_ == 500:
       tasovasemmalle = True
    if taso.position_x_ < 0:
        tasovasemmalle = False
        
    if tasovasemmalle:
        taso.MoveX(-1)
    else:
        taso.MoveX(1)
        
    robotti.Gravity()
    
    if CollisionCheck(robotti,maali): #if two object collision

        robotti.position_x_ = 200
        robotti.position_y_ = 100
    
    #draw all
    naytto.fill((0,0,0)) #
    naytto.blit(robotti.image_,(robotti.position_x_,robotti.position_y_))
    naytto.blit(taso.image_,(taso.position_x_,taso.position_y_))
    naytto.blit(taso2.image_,(taso2.position_x_,taso2.position_y_))
    naytto.blit(maali.image_,(maali.position_x_,maali.position_y_))

    pygame.display.flip() #update screen
    
    kello.tick(60) #fps limit