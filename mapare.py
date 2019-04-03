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

      









