

import math
import random
import numpy as np
from Parametres import *

##### HUMAIN

def liste_tuple(liste):
  return [(k.place_MATRICE) for k in liste]

class Humain: 
  ''' classe définissant un humain pouvant se déplacer et fuir les zomnies'''
  
  num_humain=0
  
  def __init__(self):
        self.nom = Humain.num_humain                           #que veux dire ce self qui est partout ?

import math
import random
import numpy as np                                           #Que veulent dire ces import ( numpy parametres )
from Parametres import *

##### HUMAIN

def liste_tuple(liste):
  return [(k.place_MATRICE) for k in liste]

class Humain:
  ''' classe définissant un humain pouvant se déplacer et fuir les zomnies'''
  
  num_humain=0
  
  def __init__(self):
        self.nom = Humain.num_humain                       #le . correspond a quoi ?
        Humain.num_humain += 1
        self.compteur_temps=0
        self.pdv=random.randint(40,100)
        self.compteur_faim=0
        self.sac={"Munitions":munition_début,"Médicaments":médicaments_début,} #Max 10 munitions
      
      
      
     def __str__(self):
        return "Humain " + str(self.nom)                     # self ?????
       
    def __repr__(self):
        return self.__str__()
       
   
    def sentir_zombie(self,carte,Liste_zombie):          # c est quoi carte ????
        i_humain,j_humain=self.place_MATRICE
        self.place_matrice=self.place_MATRICE
        liste_zombie = liste_tuples(Liste_zombie)
        dmin = 10000000                                  # Distance supposée du zombie le plus proche     #unite ????
        i_zombie = None
        j_zombie = None
        self.Zombie_le_plus_proche = (i_zombie, j_zombie)
        self.liste_zombie_proche = []
        for e in range(len(liste_zombie)):
            i_zombieTempo, j_zombieTempo = liste_zombie[e]
            if i_zombieTempo in range((i_humain-Odorat_H),(i_humain+Odorat_H+1))\          # humain-Odorat_H ????????
            and j_zombieTempo in range((j_humain-Odorat_H),(j_humain+Odorat_H+1)):         # L'humain est dans un voisinage +/- 10 du zombie
                 self.liste_zombie_proche +=[(i_zombieTempo,j_zombieTempo)]                #zombieTempo ???????????
                 dz=math.sqrt((i_zombieTempo - i_humain)**2+(j_zombieTempo - j_humain)**2)
                 if (dz<dmin):                        # Compare la distance H-Z la plus petite trouvée
                    i_zombie = i_zombieTempo                                          # Garde en mémoire les coordonnées du zombie le plus proche
                    j_zombie = j_zombieTempo                                          
                    dmin=dz
                    self.Zombie_le_plus_proche = (i_zombieTempo,j_zombieTempo)
                    self.Zombie_le_plus_proche2= Liste_zombie[e]
                    
                    
     def Pdv(self,carte,Liste_humain,Liste_classe):
        """Etat de la vie de l'humain """
        i_humain, j_humain = self.place_MATRICE
        if self.faim == 0:
            if self.compteur_temps < temps_perdre_pdv:
                self.compteur_temps += 1
            else:
                self.pdv -= 1
                self.compteur_temps = 0
                
        if self.pdv<=80 and self.sac["Médicaments"]>1:              #ce n'est pas un >= plutot ?
            self.sac["Médicaments"]-=1
            self.pdv+=pdv_rendus
        if self.pdv==0:
            carte[i_humain,j_humain]=Zombie()                       #encore une fois qu'est ce que carte ????
            carte[i_humain,j_humain].place_MATRICE=i_humain,j_humain
            Liste_humain.remove(self)
            Liste_classe.remove(self)
            Liste_zombie+=carte[i_humain,j_humain]
            Liste_classe+=carte[i_humain,j_humain] 
            
            
     def shoot(self,carte,Liste_zombie,Liste_classe):
        if len(self.liste_zombie_proche)<=2 and len(self.liste_zombie_proche)>0 :    #
            if self.sac["Munitions"]>=1:
                x=random.randint(taux_réussite_tir1,taux_réussite_tir2)
                print(x)
                if x==1 and self.Zombie_le_plus_proche2 != None:
                    Liste_classe.remove(self.Zombie_le_plus_proche2)
                    Liste_zombie.remove(self.Zombie_le_plus_proche2)
                    carte[self.Zombie_le_plus_proche]=Vide()
                    self.sac["Munitions"]=self.sac["Munitions"]-1
                    print(self.sac)
                    print(carte[self.Zombie_le_plus_proche])
                    print("Un zombie s'est fait tué")
                else:
                    self.sac["Munitions"]=self.sac["Munitions"]-1
                    print("RATE")
                    print(self.sac)   
  
  
  
  

