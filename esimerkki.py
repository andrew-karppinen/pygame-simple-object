import pygame

from object_class import Objekti

pygame.init() #alustetaan pygame moduuli
naytto = pygame.display.set_mode((640, 480)) #luodaan ikkuna
pygame.display.set_caption("pygame") #nimetään ikkuna


robottikuva = pygame.image.load("kuvat/robotti.png") #ladataan kuva robotti
tasokuva = pygame.image.load("kuvat/taso.png")

#luodaan kello jolla rajoitetaan pelin nopeutta
kello = pygame.time.Clock()


robotti = Objekti(robottikuva,sijainti_x=400,sijainti_y=100,painovoiman_voimakkuus=0.5,hypyn_voimakkuus=15)
taso = Objekti(tasokuva,sijainti_x=50,sijainti_y=200)

robotti.LisaaTormays(taso)


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
                ylos = True
            if tapahtuma.key  == pygame.K_DOWN:
                alas = True
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = True
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = True

        if tapahtuma.type == pygame.KEYUP: #ylös
            if tapahtuma.key  == pygame.K_UP:
                ylos = False
            if tapahtuma.key  == pygame.K_DOWN:
                alas = False
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = False
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = False
    


        if tapahtuma.type == pygame.QUIT: #jos ohjelma suljetaan
            exit() 
        

    if oikealle:
        robotti.LiikuX(2)
    if vasemmalle:
        robotti.LiikuX(-2)
    if alas:
        robotti.LiikuY(2)
    if ylos:
        robotti.LiikuY(-2)



    #robotti.Painovoima()
    
    naytto.fill((0,0,0)) #täytetään ruutu mustalla
    naytto.blit(robotti.kuva_,(robotti.sijainti_x_,robotti.sijainti_y_))
    naytto.blit(taso.kuva_,(taso.sijainti_x_,taso.sijainti_y_))

    pygame.display.flip() #päivittää näytön
    
    kello.tick(60) #rajoittaa pelin nopeuden