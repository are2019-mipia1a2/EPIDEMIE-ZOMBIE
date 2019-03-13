

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
      
      
      
   
  
  
  

