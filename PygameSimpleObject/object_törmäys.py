



def TunnistaTormays(obj1,obj2):
    #saa kaksi objektia parametriksi
    #Tunnistaa onko kaksi objektia päällekkäin 
    #palauttaa True/False


    if obj1.sijainti_y_ <= obj2.sijainti_y_ + obj2.kuva_koko_y_:
          if obj1.sijainti_y_+ obj1.kuva_koko_y_>= obj2.sijainti_y_:
              
              if obj1.sijainti_x_<= obj2.sijainti_x_ + obj2.kuva_koko_x_:
                  if obj1.sijainti_x_ + obj1.kuva_koko_x_ >= obj2.sijainti_x_:
                      return True

    return False