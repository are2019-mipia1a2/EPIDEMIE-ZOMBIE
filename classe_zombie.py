class Zombie:

    """
 Classe définissant un zombie, qui peux se déplacer et cherche à tuer les humains
 """

    num_zombie=0

    def __init__(self):
        self.nom = Zombie.num_zombie                        # Attribue le nom à chaque zombie
        Zombie.num_zombie += 1
        self.comp=0     #??                      # Compteur pour différencier chaque zombie
    def __str__(self):
        return "Zombie " + str(self.nom)
    def __repr__(self):
        return self.__str__()
    def sentir(self, carte,Liste_humain):

        i_zombie,j_zombie=self.place_MATRICE
        liste_humain = liste_tuples(Liste_humain)          # Arrange cette liste en liste de tuples
        self.place_matrice = i_zombie ,j_zombie
        self.place_MATRICE=self.place_matrice
        dmin = 1000                                     # Distance supposée du plus proche humain
        i_humain_cible = None                               # Coordonnée i de l'humain le plus proche
        j_humain_cible = None                               # Coordonnée j de l'humain le plus proche
        for X in range(len(liste_humain)):
            i_humain, j_humain = liste_humain[X]
            if i_humain in range((i_zombie-Odorat_Z),(i_zombie+Odorat_Z+1)) and j_humain in range((j_zombie-Odorat_Z),(j_zombie+Odorat_Z+1)):
                dz=math.sqrt(((i_humain - i_zombie)**2)+((j_humain - j_zombie)**2))
                if dz<dmin:                        # Compare la distance H-Z avec la plus petite trouvée
                    i_humain_cible = i_humain
                    j_humain_cible = j_humain
                    dmin=dz
        self.coord_humain=(i_humain_cible ,j_humain_cible)


    def move(self, carte,Liste_humain,Liste_zombie,Liste_classe):
        if self.coord_humain==(None,None):
            compteur_boucle = 0
            while compteur_boucle == 0 :
                x = random.randint(-1,1)                        # Tirage du déplacement vertical
                y = random.randint(-1,1)                        # Tirage du déplacement horizontal
                i_zombie, j_zombie = self.place_matrice
                i1 = i_zombie + x
                j1 = j_zombie + y
                if (i1 in range(i)) and (j1 in range(j)):       # Vérifie que le déplacement voulu ne sort pas de la map
                    if isinstance(carte[i1,j1], Vide):
                        carte[i1,j1] = self
                        carte[i_zombie,j_zombie] = Vide()
                        self.place_matrice=i1,j1
                        self.place_MATRICE=self.place_matrice
                        compteur_boucle += 1
        else:
            A1,B1=0,0
            A3,B3=self.coord_humain
            A,B=self.place_matrice
            A1,B1,A2,B2=nouveau_coordonnées(A3,B3,A,B)
            print(carte[A2,B2])
            if isinstance(carte[A2,B2], Vide):
                carte[A2,B2]=self
                carte[A,B]=Vide()
                self.place_matrice=A2,B2
                self.place_MATRICE=self.place_matrice

            if isinstance(carte[A2,B2],Humain):
                x=random.randint(taux_de_réussite_zombies1,taux_de_réussite_zombies2)
                if x==1:

                    Liste_humain.remove(carte[A2,B2])
                    Liste_classe.remove(carte[A2,B2])
                    carte[A2,B2]=self
                    carte[A,B]=Vide()
                    print(Liste_humain)
                    self.place_matrice=A2,B2
                    self.place_MATRICE=self.place_matrice

                else:

                    print(Liste_zombie)
                    Liste_humain.remove(carte[A2,B2])
                    Liste_classe.remove(carte[A2,B2])
                    carte[A2,B2]=self
                    carte[A,B]=Zombie()
                    carte[A,B].place_MATRICE=A,B
                    carte[A,B].place_matrice=carte[A,B].place_MATRICE
                    self.place_matrice=A2,B2
                    self.place_MATRICE=self.place_matrice
                    Liste_zombie+=[carte[A,B]]
                    Liste_classe.append(carte[A,B])
                    print(Liste_zombie)

def nouveau_coordonnées(H1,H2,Z1,Z2):
    if H1<=Z1:
        Z1-=1
    if H1>=Z1:
        Z1+=1
    if H2<=Z2:
        Z2-=1
    if H2>=Z2:
        Z2+=1
    return (H1,H2,Z1,Z2)


########################################################################################################
#VIDE

class Vide:
    def __repr__(self):
        return "Vide"
