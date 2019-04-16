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
 
Cependant, nous avons dû pousser un peu nos connaissances afin de créer une classe, c’est-à-dire un nouveau type d’objet. Nous en avons créé deux, la classe zombies et la classe humain, qui définissent le comportement et les attributs associés aux zombies et aux humains. Dans le cadre de ses classes nous avons dû apprendre à maîtriser la variable “self” ou autrement dit le “sois même” qui nous a permis de coder des classes capables de créer des objets différents en boucle. Ensuite nous avons dû créer une map, dans ce but nous avons dû apprendre à construire des matrices avec python.  Donc pour notre map nous avons créé une matrice et nous y avons implanté nos agents, pour cela nous avons su maîtriser les “import”.

De plus, hors contexte scientifique, il fallait également que chaque personne du groupe soit coordonnée avec les autres afin d’optimiser au mieux notre efficacité. En effet, parfois en mettant les programmes en commun ils ne marchaient plus car les structures des algorithmes n’étaient pas adaptés pour pouvoir fonctionner entre eux. Cela représente une autre notion fondamentale de notre travail qui a été d’avoir une bonne coordination en parlant beaucoup entre nous pour savoir exactement ce que faisait chaque membre du groupe afin d’avoir une vision globale de ce nous faisions tous et d’avoir un aperçu de notre rendu final pour éviter tout dérapage ou une mauvaise compréhension de ce que nous recherchions.

Finalement, une dernière notion importante sur laquelle reposait notre travail était celle d’espacer au mieux notre travail et de ne pas travailler “en bloc”. En effet, espacer notre travail, à la fac comme chez nous, nous permettait de prendre plusieurs fois du recul et remettre à chaque fois en question ce que nous faisons. De plus, lorsque que la source d’un bug nous échappe pendant 2h, il est nécessaire de revenir plus tard avec un regard nouveau.

## IV. Contibutions

Nous avons décidé pour l’écriture du code de diviser l’algorithme en 2 grandes parties : L’environnement et les agents.

L’environnement est une petite ville comprenant plusieurs types de bâtiments : les maisons (pour se réfugier), les hôpitaux (pour se soigner), les armureries (pour avoir des munitions et tuer les zombies), les magasins (pour la nourriture).

Les agents sont les zombies et les humains ayant plusieurs caractéristiques, plusieurs comportements et ils ont été créés via les classes, nouveauté que nous avons du nous approprier pour coder tout ce que l’on voulait réaliser.

Pour cela, nous avons divisé notre groupe de 4 en 2 groupes de 2 : Martin avec Alexandre et Valentin avec Astrid. Martin et Alexandre se sont occupés de la création des classes et du comportement des agents, ce qui était une des parties les plus longues du programme, notamment parce-qu’on a décidé de réaliser des agents plutôt complets.

Valentin et Astrid se sont, eux, occupés de l’environnement, de la dynamique et du rendu visuel ainsi que la création des courbes en faisant varier les paramètres.

Une fois après avoir fini la réunion des codes et la fusion, nous avons pu commencer nos tests en réglant les derniers problèmes de code et de stabilité.


Contribution lors de la rédaction du rapport :

Astrid : Dynamique, Interprétation des résultats.

Valentin: Résumés, Environnement, Contributions.

Martin : Introduction, Liste des paramètres, Agents.

Alexandre : Agents, Environnement, Liste des paramètres.

### A/ Les agents

#### 1. Les humains

La classe humain contient beaucoup de caractéristiques et de comportements afin de rapprocher leur fonctionnement du notre. Les humains peuvent donc se déplacer, sentir la présence des zombies, tuer les zombies, ils ont aussi des points de vie et une barre de faim, ils ont besoin de se ravitailler (nourritures, munitions, médicaments), et ils peuvent se déplacer selon leur caractéristiques actuelles (s’il y a un zombie à proximité, s’il a besoin de se ravitailler, il se déplace vers une porte, …)
A l’initialisation, l’humain possède un compteur de “faim” qui prend une valeur défini dans les paramètre généraux, des PDV (Points DE Vie) prenant une valeur entre 40 et 100 choisie aléatoirement, on suppose qu’ils n’ont pas encore faim et que dans leur sac ils ne possèdent que 3 munitions maximum.

	def __init__(self):
	   self.nom = Humain.num_humain
		   Humain.num_humain += 1
		   self.compteur_temps=0
		   self.pdv=random.randint(40,100)
		   self.faim=faim_humain
		   self.compteur_faim=0
	   self.sac={"Munitions":4,"Médicaments":0,"Nourriture":0}

Le compteur de temps va servir à compter le temps qu’il passe en état “a faim”


On crée différentes fonctions pour définir leur comportements et leur caractéristiques: 


Tout d’abord, on a créé une fonction pour que les humains sentent la présence des zombies dans un rayon de 10, en rendant les coordonnées du zombie le plus proche grâce à la formule mathématique donnant la distance entre deux points.

math.sqrt((i_zombieTempo - i_humain)**2+(j_zombieTempo - j_humain)**2)
Avec  i_zombieTempo,j_zombieTempo  les coordonnées d’un zombie et i_humain,j_humain  les coordonnées d’un humain.

Ensuite on a codé une fonction Pdv : ses points de vie diminuent au fur et à mesure qu’il marche en ayant faim. S’il possède des médicaments, il les prend pour récupérer de la vie.
 

	def Pdv(self, carte) :
      	Si son compteur faim =0 :
                	Si le compteur temps < 50 :
                          	Compteur temps = Compteur temps +1
                	Sinon :
                          	Il perd 1 pdv
                          	On réinitialise le compteur temps à 0
                          	On réinitialise le compteur faim à 0
      	Si ses pdv<=80 et il a des médicaments :
                	Son sac perd 1 de médicament
                	Ses pdv augmentent de 20
      	Si ses pdv==0 :
                	L’humain se transforme en zombie
 	
Puis une fonction shoot qui lui permet de tuer des zombies (ici très simplifiée)
 
	def shoot(self, carte) :
	Si l’humain possède au moins une munition :
		Une chance sur 2 de tuer le zombie et l’humain perd une munition
 
Nous avons aussi créé les fonctions « ravitaillement »  et « run » qui prennent en compte de nombreux paramètres comme ce que l’humain avait dans son sac, ce qui lui manquait, s’il devait se diriger vers un type de bâtiment en priorité (pour ses points de vie par exemple), etc. En version très simplifiée :
 
	def ravitaillement(self,carte) :
	 L’humain regarde autour de lui s’il y a des portes:
	 Si son stock de médicament n’est pas plein et pas de zombie autour :
		  Se dirige vers une porte d’hôpital et remplit son sac
	 Si son stock d’arme n’est pas plein et pas de zombie autour:
		   Se dirige vers une armurerie et remplit son sac
	 Si son stock de nourriture n’est pas plein et pas de zombie autour:
		   Se dirige vers un magasin et remplit son sac 


#### 2. Les zombies

Les zombies peuvent sentir les humains autour d’eux, se déplacer vers celui le plus proche s’il y en a un a proximité et, soit le tuer, soit le transformer en zombie. Sinon ils se déplacent aléatoirement.

A l’initialisation, on donne un numéro à chaque zombie pour pouvoir les différencier :



def __init__(self):

self.nom = Zombie.num_zombie                        

Zombie.num_zombie += 1    

   

Puis, on crée une classe « sentir » servant à trouver les coordonnées de l’humain le plus proche en utilisant la formule mathématique de la distance entre deux points :


min(math.sqrt((i_humain - i_zombie)**2+(j_humain - j_zombie)**2)


Une fonction « move » pour faire bouger les zombies tout en faisant attention à ce que les zombies ne sortent pas de la map et ne rentrent pas dans les bâtiments.


def move(self, carte) :

         Si pas d’humain à proximité :

                   Se déplacer aléatoirement d’une case autour de sa position

                   Si la position reste dans la matrice et est vide :

                             Changer la classe zombie par vide et vide par zombie

        

Sinon :

                   Faire déplacer le zombie vers l’humain

                   Si il est à côté de lui :

                             Une chance sur deux de le tuer

                             Une chance sur deux de le transformer en zombie

### B/ Environnement


La représentation de l’épidémie de Zombie se fait sur une carte, dont l'affichage repose sur le parcour de la carte, de l'interprétation de chaque case puis du envoie des donnée, etc.

Nous avons utilisé un mode de programmation, appelé “par valeur”, qui consiste à créer des listes qui contiennent les agents et d’appliquer les fonctions à partir de ces listes.

Pour cela nous avons dû d’abord créer un support pour nos agents, qui soit facile à manipuler. Nous avons donc fait une carte sous forme de tableau dans laquelle on stocke nos différents objets. 

Nous l’avons initialisé par une liste de liste avec que des zéros dont les dimensions sont mis dans les paramètres généraux :

return [[0 for j in range(y)] for i in range(x)]

Cette liste n’est créée qu’une fois, ce qui nous permet de ne pas prendre trop de mémoire, et donc sans risque de faire planter l’ordinateur.

Ensuite, on implante ensuite un nombre définit de bâtiments. Pour cela, on parcourt la carte et on les insère aléatoirement avec chacun un type spécifique: hôpital, magasin, maison ou armurerie. Chaque fois qu’ils sont insérés on leur donne une “place_matrice” et on les ajoute à la liste des bâtiments. Ils ont tous la même structure: c’est un amas d’objet de classe “Bâtiment” ayant une méthode définissant leur type, et sont dotés d’une unique porte. Cette porte sert d’interface entre les agents de type “Humain” et les bâtiments. Elle contient à elle seule toutes les informations sur l’état de l’infrastructure, c’est-à-dire ses ressources disponibles que les humains convoitent, comme la nourriture, les munitions ou les médicaments.
	
Pour finir, on ajoute les deux types d’agents, qui sont les objets de classe “Humain” et “Zombie”. Cette implémentation se fait également de manière aléatoire, avec néanmoins un contrôle sur le nombre d’agents à implanter. Ce nombre est défini dans les paramètres généraux. Chaque fois qu’un agent est créé, nous lui donnons une “place_matrice” et l’ajoutons à la liste correspondant à sa classe.

Pour faciliter la manipulation et la lisibilité de cette liste de liste par la suite, on la transforme en un tableau de type array grâce à la fonction array() du module scipy.



### C/ Dynamique

#### 1. Structure

#### 2. Affichage

## V. Conclusion


## VI. résumé en anglais





















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

