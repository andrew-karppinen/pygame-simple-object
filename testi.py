import pygame

from object_class import Objekti

robottikuva = pygame.image.load("robotti.png") #ladataan kuva robotti
tasokuva = pygame.image.load("taso.png")

obj1 = Objekti(robottikuva)

obj2 = Objekti(tasokuva)






obj1.TulostaMuut()