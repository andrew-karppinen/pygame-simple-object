import pygame

def opposite(number):
    return -1 * number




#otsikkotiedosto

class Objekti:
    def __init__(self,kuva:pygame.Surface,sijainti_x: int = 0, sijainti_y: int = 0,painovoiman_voimakkuus: float = 0.2,hypyn_voimakkuus: float = 20.0,): #konstruktori
        self.sijainti_x_ = sijainti_x
        self.sijainti_y_ = sijainti_y
        self.painovoiman_arvo_ = 0.0 #painovoiman arvo   < 0 = alaspäin > 0 = ylöspäin
        self.hypyn_voimakkuus_ = hypyn_voimakkuus
        self.painovoiman_voimakkuus_ = painovoiman_voimakkuus
        
        self.kuva_ = kuva #pygame kuva olio
        self.kuva_koko_y_ = kuva.get_height() #kuvan mitat
        self.kuva_koko_x_ = kuva.get_width()
        
        self.muut_objektit_ = []


    
    #nämä metodit toteuttavat objektin liikuttamisen
    def LiikuX(self,matka: int):
        for i in range(self.sijainti_x_,self.sijainti_x_+matka):
            self.sijainti_x_ += 1

            if self.TunnistaTormays() == True: #jos tapahtuu törmäys
                self.sijainti_x_ -= 1 #peruu liikkeen
                return None


        self.sijainti_x_ += matka

    
    def LiikuY(self,matka: int):

        for i in range(self.sijainti_y_,self.sijainti_y_+matka):
            self.sijainti_y_ += 1

            if self.TunnistaTormays() == True: #jos tapahtuu törmäys
                self.sijainti_y_ -= 1 #peruu liikkeen
                return None


        self.sijainti_y_ += matka

    
        
    def Painovoima(self): #metodi toteuttaa painovoiman
        #muuttaa y sijaintia
        

        self.LiikuY(opposite(int(self.painovoiman_arvo_))) 

        if self.painovoiman_arvo_ > -5.0:
            self.painovoiman_arvo_ -= self.painovoiman_voimakkuus_  
    

    
    def Hyppy(self): #metodi toteuttaa hypyn
        self.painovoiman_arvo_ = self.hypyn_voimakkuus_
        



    def LisaaTormays(self,obj):
        '''
        Saa parametrina viittauksen toiseen objektiin
        '''
        
        self.muut_objektit_.append(obj) #lisää objektin listaan


    def TunnistaTormays(self):
        #palauttaa True/False jos objekti päällekkäin jonkun muun objektin kanssa

        for i in range(len(self.muut_objektit_)):
            obj = self.muut_objektit_[i]

            if self.sijainti_y_ <= obj.sijainti_y_ + obj.kuva_koko_y_:
                if self.sijainti_y_+ self.kuva_koko_y_>= obj.sijainti_y_:
                    
                    if self.sijainti_x_<= obj.sijainti_x_ + obj.kuva_koko_x_:
                        if self.sijainti_x_ + self.kuva_koko_x_ >= obj.sijainti_x_:
                            return True

        return False



    def TulostaMuut(self):
        for i in range(len(self.muut_objektit_)):
            print(self.muut_objektit_[i])
