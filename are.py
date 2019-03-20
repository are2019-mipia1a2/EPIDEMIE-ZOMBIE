import math
import random
import numpy as np
 

#PARAMETRES GENERAUX
 
i = 150  
j = 150
Munitions_max = 20      # Quantité maximale que peut avoir un humain dans son sac
Médicaments_max = 10    # Quantité maximale que peut avoir un humain dans son sac      
Nourriture_max = 20     # Quantité maximale que peut avoir un humain dans son sac
Odorat_Z = 10           # Zone d'odorat des zombies
Odorat_H = 10           # Zone d'alerte des humains
faim_humain= 40
 

#HUMAIN  
def liste_tuples(liste):
    return [(k.place_MATRICE) for k in liste]
 
 
 
 
 
 
class Humain:
 
    """
Classe définissant un humain, qui peux se déplacer, fuir les zombies
"""
   
    num_humain=0
   
    def __init__(self):
        self.nom = Humain.num_humain
        Humain.num_humain += 1                   #??????
        self.compteur_temps=0
        self.pdv=random.randint(40,100)
        self.faim=faim_humain
        self.compteur_faim=0
        self.sac={"Munitions":4,"Médicaments":0,"Nourriture":0}  # Mun max : 30
       
   
    def __str__(self):
        return "Humain " + str(self.nom)      #????????
       
    def __repr__(self):                       #?????????
        return self.__str__()
       
   
    def sentir_zombie(self,carte,Liste_zombie):
        i_humain,j_humain=self.place_MATRICE
        self.place_matrice=self.place_MATRICE
        liste_zombie = liste_tuples(Liste_zombie)
        dmin = 10000000                                  # Distance supposée du zombie le plus proche
        i_zombie = None
        j_zombie = None
        self.Zombie_le_plus_proche = (i_zombie, j_zombie)
        self.liste_zombie_proche = []
        for e in range(len(liste_zombie)):
            i_zombieTempo, j_zombieTempo = liste_zombie[e]                           #Tempo = temporaire
            if i_zombieTempo in range((i_humain-Odorat_H),(i_humain+Odorat_H+1))\
            and j_zombieTempo in range((j_humain-Odorat_H),(j_humain+Odorat_H+1)):         # L'humain est dans un voisinage +/- 10 du zombie
                 self.liste_zombie_proche +=[(i_zombieTempo,j_zombieTempo)]
                 dz=math.sqrt((i_zombieTempo - i_humain)**2+(j_zombieTempo - j_humain)**2) #distance de l'huùmain et du zombie
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
            if self.compteur_temps < 20:
                self.compteur_temps += 1
            else:
                self.pdv -= 1                                                   # si le compteur faim arrive à 20 perd un pdv
                self.compteur_temps = 0
                self.faim=0
        if self.pdv<=80 and self.sac["Médicaments"]>1:
            self.sac["Médicaments"]-=1
            self.pdv+=20
        if self.pdv==0:
            carte[i_humain,j_humain]=Zombie()                                   #l'humain meurt et devient un zombie
            carte[i_humain,j_humain].place_MATRICE=i_humain,j_humain
            Liste_humain.remove(self)
            Liste_classe.remove(self)
            Liste_zombie+=carte[i_humain,j_humain]
            Liste_classe+=carte[i_humain,j_humain]
           
    def Faim(self):
        if self.sac["Nourriture"]>=1 and self.faim<=0:                    # si il a faim et il a de la nourriture il mange
               
                self.sac["Nourriture"]-=1
                self.faim+=20
               
        if self.compteur_faim < 2:
            self.compteur_faim += 1
        elif self.faim>0:
            self.faim -=1                                               #sinon il perd des points de faim
            self.compteur_faim=0
           
    def shoot(self,carte,Liste_zombie,Liste_classe):
        if len(self.liste_zombie_proche)<=2 and len(self.liste_zombie_proche)>0 : #la porté d'un humain est de 2
            if self.sac["Munitions"]>=1:                                          # utilise une munition pour son tire
                x=random.randint(0,1)
                print(x)
                if x==1 and self.Zombie_le_plus_proche2 != None:                 # une chance sur 2 de toucher lors du tire
                    Liste_classe.remove(self.Zombie_le_plus_proche2)
                    Liste_zombie.remove(self.Zombie_le_plus_proche2)
                    carte[self.Zombie_le_plus_proche]=Vide()
                    self.sac["Munitions"]=self.sac["Munitions"]-1
                    print(self.sac)
                    print(carte[self.Zombie_le_plus_proche])
                    print("Un zombie s'est fait tué")                             #si touché zombie meurt
                else:
                    self.sac["Munitions"]=self.sac["Munitions"]-1
                    print("RATE")
                    print(self.sac)                                                #sinon zombie reste en vie
                   
    def prendre_nourr(self,carte):
        i_humain, j_humain = self.place_MATRICE
        for x in range(-1,2):
            for y in range (-1,2):#Vérifie qu'il y a une porte autour de l'humain
                           
                if (i_humain + x in range(i)) and (j_humain + y in range(j)):
                    if not isinstance(carte[i_humain+x,j_humain+y], Zombie) and not isinstance(carte[i_humain+x,j_humain+y], Vide) and not isinstance(carte[i_humain+x,j_humain+y], Humain) and carte[i_humain+x, j_humain+y].type == "Porte":
                        posx_porte = i_humain+x
                        posy_porte = j_humain+y
                        print("_________________________________________________________________________________")
                        print("ravitaillement en cours")
                        if not carte[posx_porte,posy_porte].stock_medicaments == 0 :    # Si le stock n'est pas vide
                            print(self.sac)
                            if not self.sac["Médicaments"]== Médicaments_max :          # Si le sac n'est pas plein
                                if carte[posx_porte,posy_porte].stock_medicaments >= (Médicaments_max - self.sac["Médicaments"]) : # Si stock >= Place dans le sac
                                    carte[posx_porte,posy_porte].stock_medicaments -= (Médicaments_max - self.sac["Médicaments"])  # Vide le stock de la quantité à remplir dans le sac
                                    self.sac["Médicaments"] = Médicaments_max                                                      # Rempli au max le sac
                                if carte[posx_porte,posy_porte].stock_medicaments < (Médicaments_max - self.sac["Médicaments"]) :  # Si stock < Place dans le sac
                                    self.sac["Médicaments"] += carte[posx_porte,posy_porte].stock_medicaments                      # Rempli le sac avec la taille du stock
                                    carte[posx_porte,posy_porte].stock_medicaments -= 0 #Médicaments_max-self.sac["Médicaments"]  # Vide entièrement le stock
                            print(self.sac)
                        if not carte[posx_porte,posy_porte].stock_munitions == 0 :  # Même chose mais avec une autre ressource
                            print(self.sac)
                            if not self.sac["Munitions"]== Munitions_max :
                                if carte[posx_porte,posy_porte].stock_munitions >= (Munitions_max - self.sac["Munitions"]) :
                                    carte[posx_porte,posy_porte].stock_munitions -= (Munitions_max - self.sac["Munitions"])
                                    self.sac["Munitions"] = Munitions_max
                                if carte[posx_porte,posy_porte].stock_munitions < (Munitions_max - self.sac["Munitions"]) :
                                    self.sac["Munitions"] += carte[posx_porte,posy_porte].stock_munitions
                                    carte[posx_porte,posy_porte].stock_munitions = 0     #Probleme: tu remet à 0 le nombres de munitions....
                            print(self.sac)
                        if not carte[posx_porte,posy_porte].stock_nourriture == 0 :  # Même chose mais avec une autre ressource
                            print(self.sac)
                            if not self.sac["Nourriture"]== Nourriture_max :
                                if carte[posx_porte,posy_porte].stock_nourriture >= (Nourriture_max - self.sac["Nourriture"]) :
                                    carte[posx_porte,posy_porte].stock_nourriture -= (Nourriture_max - self.sac["Nourriture"])
                                    self.sac["Nourriture"] = Nourriture_max
                                if carte[posx_porte,posy_porte].stock_nourriture < (Nourriture_max - self.sac["Nourriture"]) :
                                    self.sac["Nourriture"] += carte[posx_porte,posy_porte].stock_nourriture
                                    carte[posx_porte,posy_porte].stock_nourriture = 0
                            print(self.sac)
   
 
   
    def move(self,carte,i_destination, j_destination):
       
        i_humain, j_humain = self.place_matrice        
        i_prox, j_prox = i_humain, j_humain
        i_boussole = 0                                  # Coordonnées de la direction
        j_boussole = 0
        if i_humain < i_destination :                   # Analyse du chemin idéal
            i_prox += 1
            i_boussole = 1
           
        elif i_humain > i_destination :
            i_prox -= 1
            i_boussole = -1
           
        if j_humain < j_destination :
            j_prox += 1
            j_boussole = 1
           
        elif j_humain > j_destination :
            j_prox -= 1
            j_boussole = -1
        if isinstance((carte[i_prox,j_prox]),Vide):                   # Déplacement prévu
            carte[i_prox,j_prox] = self
            self.place_matrice=i_prox,j_prox
            self.place_MATRICE=self.place_matrice
            carte[i_humain,j_humain] = Vide()
        elif isinstance(carte[i_prox - i_boussole ,j_prox],Vide):   # Alternative si chemin obstrué
            carte[i_prox - i_boussole ,j_prox] = self
            self.place_matrice=i_prox - i_boussole ,j_prox
            self.place_MATRICE=self.place_matrice
            carte[i_humain,j_humain] = Vide()
        elif isinstance(carte[i_prox,j_prox - j_boussole],Vide):
            carte[i_prox ,j_prox - j_boussole] = self
            self.place_matrice=i_prox ,j_prox - j_boussole
            self.place_MATRICE=self.place_matrice
            carte[i_humain,j_humain] = Vide()
       
        elif not isinstance(carte[i_prox,j_prox], Zombie) and not isinstance(carte[i_prox,j_prox], Vide) and not isinstance(carte[i_prox,j_prox], Humain) and (carte[i_prox,j_prox].type=='Porte'):
            print ("je suis sur la porte")
            self.prendre_nourr(carte)
       
        else:
                compteur_boucle = 0                                 # Compteur de sortie de boucle
                while compteur_boucle == 0 :
                   
                    x = random.randint(-1,1)                        # Tirage du déplacement vertical
                    y = random.randint(-1,1)                        # Tirage du déplacement horizontal
                    #i_humain, j_humain = self.place_matrice
                    i1 = i_humain + x
                    j1 = j_humain + y
                    if (i1 in range(i)) and (j1 in range(j)):       # Vérifie que le déplacement voulu ne sort pas de la map
                        if isinstance(carte[i1,j1], Vide):                      
                            carte[i1,j1] = self
                            carte[i_humain,j_humain] = Vide()
                            self.place_matrice=i1,j1
                            self.place_MATRICE=self.place_matrice
                            compteur_boucle += 1
               
       
   
    """def move(self,carte,i_destination, j_destination):
       A3,B3=i_destination, j_destination
       A,B=self.place_matrice
       A1,B1=0,0
       compteur_boucle=0
       A1,B1,A2,B2=nouveau_coordonnées(A3,B3,A,B)
       while compteur_boucle == 0 :
           x = random.randint(-1,1)                      
           y = random.randint(-1,1)                      
           i1 = A2 + x
           j1 = B2 + y
           if (i1 in range(i)) and (j1 in range(j))and isinstance(carte[i1,j1], Vide):
               carte[i1,j1] = self
               carte[A2,B2] = Vide()
               self.place_matrice=i1,j1
               self.place_MATRICE=self.place_matrice
               compteur_boucle += 1
           if not isinstance(carte[i1,j1], Zombie) and not isinstance(carte[i1,j1], Vide) and not isinstance(carte[i1,j1], Humain):
               if (carte[i1,j1].type=='Porte'):
                   self.prendre_nourr(carte)"""
       
 
    def run(self,carte,Liste_porte):
        """
    Lance la capacité de l'humain à se déplacer
    """
        i_humain, j_humain = self.place_matrice
        L_P=liste_tuples(Liste_porte)
        for x in range(len(self.liste_zombie_proche)):
                if len(self.liste_zombie_proche) <=x and self.sac["Munitions"] < x:
                    i_porte, j_porte = trouve_batiment("Maison",i_humain,j_humain,carte,Liste_porte)
                    self.move(carte,i_porte, j_porte)
                   
               
        if len(self.liste_zombie_proche) == 0:                         # Si il n'y a pas de zombie à l'horizon
            if self.sac["Munitions"] < 1:                        # Déplacement vers une porte quelconque
                i_porte, j_porte = trouve_batiment("Armurerie",i_humain,j_humain,carte,Liste_porte)
               
                self.move(carte, i_porte, j_porte)
               
           
            elif self.faim < 20 and self.sac["Nourriture"] == 0 : # Déplacement vers n'importe quelle porte
               
                dmin=1000000
                for e in range(0,len(L_P)):
                    i_portetempo, j_portetempo = (L_P)[e] # L'humain est dans un voisinage +/- 10 du zombie
                    dz=math.sqrt((i_portetempo - i_humain)**2+(j_portetempo - j_humain)**2)
                    if (dz<dmin) and Liste_porte[e].stock_nourriture>0:                        # Compare la distance H-Z la plus petite trouvée
                        i_porte = i_portetempo                                          # Garde en mémoire les coordonnées du zombie le plus proche
                        j_porte = j_portetempo                                          
                        dmin=dz
                        self.Porte_la_plus_proche = (i_porte,j_porte)  # Fonction qui rend toute les portes
                self.move(carte, i_porte, j_porte)
           
            elif self.pdv < 30 and self.sac["Médicaments"]==0:
                i_porte, j_porte = trouve_batiment("Hôpital",i_humain,j_humain,carte,Liste_porte)
                self.move(carte,i_porte, j_porte)
               
               
            else:
                compteur_boucle = 0                                 # Compteur de sortie de boucle
                while compteur_boucle == 0 :
                   
                    x = random.randint(-1,1)                        # Tirage du déplacement vertical
                    y = random.randint(-1,1)                        # Tirage du déplacement horizontal
                    #i_humain, j_humain = self.place_matrice
                    i1 = i_humain + x
                    j1 = j_humain + y
                    if (i1 in range(i)) and (j1 in range(j)):       # Vérifie que le déplacement voulu ne sort pas de la map
                        if isinstance(carte[i1,j1], Vide):                      
                            carte[i1,j1] = self
                            carte[i_humain,j_humain] = Vide()
                            self.place_matrice=i1,j1
                            self.place_MATRICE=self.place_matrice
                            compteur_boucle += 1






