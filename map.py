def CreationMatriceZero(x, y):
    """
   int*int -> list[list[int]]
   Crée une map de 0 de hauteur x et de largeur y
   """
   
    return [[0 for j in range(y)] for i in range(x)]

def set_map(carte):
   """
   list[list[int*Object]] -> liste[list[Object]]
   Remplace les zéros de la matrice initiale par la classe Vide
   """
   for ligne in range (i):
       for colonne in range(j):
           if carte[ligne][colonne] == 0:
               carte[ligne][colonne] = Vide()
   return carte

      









