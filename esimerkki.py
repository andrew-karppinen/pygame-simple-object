import pygame

from PygameSimpleObject import *

pygame.init() #alustetaan pygame moduuli
naytto = pygame.display.set_mode((850, 700)) #luodaan ikkuna
pygame.display.set_caption("pygame") #nimetään ikkuna


robottikuva = pygame.image.load("kuvat/robotti.png") #ladataan kuva robotti
tasokuva = pygame.image.load("kuvat/taso.png")
maalikuva = pygame.image.load("kuvat/maali.png")

#luodaan kello jolla rajoitetaan pelin nopeutta
kello = pygame.time.Clock()

#luodaan objektit
robotti = Objekti(robottikuva,sijainti_x=200,sijainti_y=100,painovoiman_voimakkuus=0.5,hypyn_voimakkuus=15)
taso = Objekti(tasokuva,sijainti_x=100,sijainti_y=600)
taso2 = Objekti(tasokuva,sijainti_x=600,sijainti_y=400)
maali = Objekti(maalikuva,sijainti_x=700,sijainti_y=335)

#lisätään törmäykset
robotti.LisaaTormays(taso)
robotti.LisaaTormays(taso2)
taso.LisaaTormays(robotti)



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
                robotti.Hyppy()
            if tapahtuma.key  == pygame.K_DOWN:
                alas = True
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = True
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = True

        if tapahtuma.type == pygame.KEYUP: #ylös

                
            if tapahtuma.key  == pygame.K_DOWN:
                alas = False
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = False
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = False

        if tapahtuma.type == pygame.QUIT: #jos ohjelma suljetaan
            exit() 
        

    if oikealle:
        robotti.LiikuX(4)
    if vasemmalle:
        robotti.LiikuX(-4)
    if alas:
        robotti.LiikuY(4)


    if taso.sijainti_x_ == 500:
       tasovasemmalle = True
    if taso.sijainti_x_ < 0:
        tasovasemmalle = False
        
    if tasovasemmalle:
        taso.LiikuX(-1)
    else:
        taso.LiikuX(1)
        
    robotti.Painovoima()
    
    if TunnistaTormays(robotti,maali): #tunnistetaan kahden objektin törmäys
        robotti.sijainti_x_ = 200
        robotti.sijainti_y_ = 100
    
    naytto.fill((0,0,0)) #täytetään ruutu mustalla
    naytto.blit(robotti.kuva_,(robotti.sijainti_x_,robotti.sijainti_y_))
    naytto.blit(taso.kuva_,(taso.sijainti_x_,taso.sijainti_y_))
    naytto.blit(taso2.kuva_,(taso2.sijainti_x_,taso2.sijainti_y_))
    naytto.blit(maali.kuva_,(maali.sijainti_x_,maali.sijainti_y_))

    pygame.display.flip() #päivittää näytön
    
    kello.tick(60) #rajoittaa pelin nopeuden
