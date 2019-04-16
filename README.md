# Ropport final

## I. Résumé

Notre objectif était de modéliser une attaque de Zombies dans une ville remplie d’humains. Mais une ville réaliste avec des bâtiments : des habitations, des hôpitaux, des armureries et des magasins. Les humains peuvent donc récupérer les ressources dont ils ont besoins dans les bâtiments. Plus précisément, notre objectif est d’étudier l’évolution des Zombies par rapport à celle des humains.  Les humains peuvent tuer les zombies et les zombies peuvent transformer les humains, ce qui participe à l’évolution de la population humaine. Pour réaliser ce projet nous avons codé une map sur laquelle nous avons placé nos bâtiments, nos humains et nos zombies, interagissant entre eux grâce à de nombreuses fonctions. Le type Classe de Python nous a été très utile pour coder les humains et les zombies ainsi que d’autres fonctions plus connues. 

## II. Introduction

Nous avons voulu, pour notre projet, nous rapprocher le plus de la réalité en représentant les humains et les zombies. Même si les Zombies n'existe pas, nous nous sommes inspiré des films, séries... pour les créer et les mettre en confrontation avec les humains. Nous avons dû faire face à un problème avec les humains. Que se passe-t-il s’il meurt de faim, s’ils n’ont plus de point de vie, s’ils n’ont plus d’armes ou de munitions ? On a décidé de mettre un ordre des priorités et nous avons envisagé de nombreuses possibilités, parce que si l’humain est déjà en train de mourir de faim, est-ce qu’il doit fuir ou tuer le Zombie ? Nous avons donc essayé de nous rapprocher le plus possible de la réalité. 
 
Nous sommes quatre à avoir travaillé sur le projet, Alexandre Djenane, Valentin Flageul, Martin Verrier et Astrid Ricard. Nous nous sommes réparties les tâches afin d’être plus efficace dans notre travail. 

## III. Présentation de la thématique

L’ensemble de notre projet repose sur des notions fondamentales  
Tout d’abord, nous avons eu besoin des bases de python que nous avons vu au premier semestre pour la réalisation de notre projet : 
Expressions et Fonctions : la définition d’une fonction, la sémantique, les types d’expression (simples : entiers, réels, booléens, chaînes ; et composées), les opérateurs informatiques... 
Fonctions et alternatives : if/else 
Répétitions et Boucles : while, for, simulation de boucle, print... 
Chaînes de caractères : intervalles, itération... 
Listes : définitions, transformation de listes, opérations diverses... 
Ensembles et Dictionnaires : opérations de base, Itération sur les ensembles et les dictionnaires, ils nous ont surtout été utile lors de la création de nos classes. 
 
Cependant, nous avons dû pousser un peu nos connaissances afin de créer une classe, c’est-à-dire un nouveau type d’objet. Nous en avons créé deux, la classe zombies et la classe humain, qui définissent le comportement et les attributs associés aux zombies et aux humains. Dans le cadre de ses classes nous avons dû apprendre à maîtriser la variable “self” ou autrement dit le “sois même” qui nous a permis de coder des classes capables de créer des objets différents en boucle. Ensuite nous avons dû créer une map, dans ce but nous avons dû apprendre à construire des matrices avec python.  Donc pour notre map nous avons créé une matrice et nous y avons implanté nos agents, pour cela nous avons su maîtriser les “import”. Pour mieux comprendre ces fonctions nous avons fait appel à l’aide d’amis qui sont en 4A à Polytech.

De plus, hors contexte scientifique, il fallait également que chaque personne du groupe soit coordonnée avec les autres afin d’optimiser au mieux notre efficacité. En effet, parfois en mettant les programmes en commun ils ne marchaient plus car les structures des algorithmes n’étaient pas adaptés pour pouvoir fonctionner entre eux. Cela représente une autre notion fondamentale de notre travail qui a été d’avoir une bonne coordination en parlant beaucoup entre nous pour savoir exactement ce que faisait chaque membre du groupe afin d’avoir une vision globale de ce nous faisions tous et d’avoir un aperçu de notre rendu final pour éviter tout dérapage ou une mauvaise compréhension de ce que nous recherchions.

Finalement, une dernière notion importante sur laquelle reposait notre travail était celle d’espacer au mieux notre travail et de ne pas travailler “en bloc” (en plusieurs heures d’affilé mais rarement). En effet, espacer notre travail (en travaillant chez nous également) nous permettait de prendre plusieurs fois du recul et remettre à chaque fois en question ce que nous faisons (de bien/mal). De plus, lorsque que la source d’un bug nous échappe pendant 2h, il est nécessaire de revenir plus tard avec un regard nouveau.

## IV. Contibutions

### A/ Les agents

#### 1. Les zombies

#### 2. Les humains

### B/ Environnement

### C/ Dynamique

#### 1. Structure

#### 2. Affichage

## V. Conclusion




















# Cahier des charges: EPIDEMIE DE ZOMBIES

Verrier Martin Ricard Astrid Flageul Valentin Djenane Alexandre

## I. Thème

Epidémie de Zombies dans une ville

## II. Nos objectifs:

- Étudier la propagation du virus à l’échelle d'une ville.
- Au bout de combien de générations l’humanité a t-elle disparu, ou non ?
- Les humains ont-ils réussi à éradiquer le virus?
- La rapidité du développement du virus en fonction du foyer de départ


## III. Nos hypothèses:

- Les humains cherchent à annihiler les zombies
- Les zombies cherchent à tuer les humains

## IV. Paramètres 

### Les paramètres fixes:

- la taille de la ville
- disposition de la ville

### Nos variables:

- population mondiale initiale
- le patient 0
- les probabilités que l'infection soit transmise
- proba de prendre un transport
- proba de mort
- proba des naissances

## V. Caractéristiques

### Les zombies

- l’agressivité
- Moyens de contaminations
- Espérance de vie des zombies

### Les humains

- Capacité à résister aux zombie
- Capacité à développer un remède
- Immunisation au virus

### Les facteurs environnementaux

- Influence du climat sur le virus
- Proximité des transports
- Foyer de départ du virus

### Les facteurs démographiques

- Densité de population
- Natalité / mortalité
- Migrations

# COMPTE RENDU FIN DE SÉANCES

## 13/03/19
Aujourd'hui Une partie du groupe s'est chargée de faire des recheches pour savoir comment coder une map et faire se déplacer les humains et zombie sur Python.
L'autre partie du groupe quand à elle s'est chargé de commencer à définir les classes dont on allait avoir besoin pour le reste de notre code.
Ils ont alors codé la fonction _init_(self) qui renferme toutes les caratéristiques des humains ainsi que les paramètres que nous utiliseront par la suite du programme.

## 20/03/19
Nous avons definie nos paramètre généraux (modifiable) ainsi que fini de définir a classe Humain.
Nous avons commencer à creer notre classe Zombie.

## 27/03/19
Aujourd'hui nous avons défini notre classe Zombie. Pour coder les classes nous nous sommes aidés de plusieurs sites comme: https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/232721-apprehendez-les-classes?fbclid=IwAR0tlbxvmCCcZDxL5yMi-RJvmxID0JaxM4WikrRzws-XkD5qRQ3xB_fbg-s  .

## 03/04/19
Aujourd'hui nous avons fini de coder la classe Zombie, coder la map sous forme de matrice.
Nous avons également fixé les objectifs de notre visualisation (placement aléatoire des batiments, batiments en couleur, courbes de visualisations).

## 10/04/19
Aujourd'hui nous avons finalisé le code de notre projet, nous avons réussi à visualiser notre animation qu'il reste à étudier. Nous avons déjà procédé à quelques simulations afin d'étudier les comportements de nos agents(zombies et humains) en fonction de nos paramètres modifables. Nous avons aussi bien avancé le compte rendu. 

