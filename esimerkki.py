import pygame

from PygameSimpleObject import *




pygame.init() #alustetaan pygame moduuli
naytto = pygame.display.set_mode((850, 700)) #luodaan ikkuna



robottikuva = pygame.image.load("images/robotti.png") #ladataan imaget
tasokuva = pygame.image.load("images/taso.png")
maalikuva = pygame.image.load("images/maali.png")

#luodaan kello jolla rajoitetaan pelin nopeutta
kello = pygame.time.Clock()

#luodaan Objektit
robotti = Object(robottikuva,position_x=200,position_y=100)
taso = Object(tasokuva,position_x=100,position_y=600)
taso2 = Object(tasokuva,position_x=600,position_y=400)
maali = Object(maalikuva,position_x=700,position_y=335)

#lisätään törmäykset
robotti.AddCollision(taso)
robotti.AddCollision(taso2)
taso.AddCollision(robotti)




tasovasemmalle = False
vasemmalle = False
oikealle = False
ylos = False
alas = False

while True: #pääsilmukka
    #tapahtuma silmukka
    for tapahtuma in pygame.event.get():
        
        #tutkitaan näppäinpainalluksia
        if tapahtuma.type == pygame.KEYDOWN: #pohjaan
            if tapahtuma.key  == pygame.K_UP:
                robotti.Jump()
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = True
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = True

        if tapahtuma.type == pygame.KEYUP: #ylös
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = False
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = False

        if tapahtuma.type == pygame.QUIT: #jos ohjelma suljetaan
            exit() 
        

    if oikealle:
        robotti.MoveX(4)
    if vasemmalle:
        robotti.MoveX(-4)


    if taso.position_x_ == 500:
       tasovasemmalle = True
    if taso.position_x_ < 0:
        tasovasemmalle = False
        
    if tasovasemmalle:
        taso.MoveX(-1)
    else:
        taso.MoveX(1)
        
    robotti.Gravity()
    
    if CollisionCheck(robotti,maali): #tunnistetaan kahden Objectin törmäys

        robotti.position_x_ = 200
        robotti.position_y_ = 100
    
    naytto.fill((0,0,0)) #täytetään ruutu mustalla
    naytto.blit(robotti.image_,(robotti.position_x_,robotti.position_y_))
    naytto.blit(taso.image_,(taso.position_x_,taso.position_y_))
    naytto.blit(taso2.image_,(taso2.position_x_,taso2.position_y_))
    naytto.blit(maali.image_,(maali.position_x_,maali.position_y_))

    pygame.display.flip() #päivittää näytön
    
    kello.tick(60) #rajoittaa pelin nopeuden
