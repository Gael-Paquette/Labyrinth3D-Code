# Importations des bibliothèques nécessaire pour utiliser le programme
from fltk import*
from time import sleep
import sys

#Dimensions du jeu
taille_case = 15 
largeur_plateau = 40 # en nombre de cases
hauteur_plateau = 30 # en nombre de cases

ACCUEIL = True # Variable ACCUEIL qui permet de faire marcher le programme tant que ACCUEIL == True, SI ACCUEIL vaut False alors le programme s'éteint

def chargement_labyrinthe(fichier):
    """
    Fonction qui prend en paramètre une liste 'lst' et un fichier texte.
    A partir du fichier, la fonction charge une liste de liste qui possède le plan du labyrinthe.

    :param fichier:
    :param lst:
    :return lst

    >>> chargement_labyrinthe(fichier, lst)
    ['******************x******', '******************.******', '*......*....******.******', '****.****.*....*.......**',
    '*.**.****.****.*.*****.**', '*.**.****....*.*.***.*.**', '*.**.**.*.**.*.*.*.....**', '*.........**.*.***.******',
    '*.*******.*..*......*****', '*.*.**..*.**.*.**.*.....*', '*...**....**.*.**.*****.*', '*.*.********.*....*****.*',
    '*.*......***.****.......*', '*.******.......**.*****.*', '*....*.***.*.*......***.*', '*.**.*.***.*.******.*...*',
    '*.*..*.....*......*.***.*', '*.********.******.*...***', '*........*.******.***.***', '*.******.*.***.........**',
    '*.*.*.**.*...*.******.*.*', '*.*.*.**.*.***.*........*', '*.*.*.**.*.***.*.******.*', '*.*.*.**.*.***.*........*',
    '*...*...........*********', '*****@*******************']
    """
    lst = [] # on crée localement une liste lst
    fiche = open(fichier, 'r') # On ouvre le fichier schéma dans la variable fiche
    for ligne in fiche: # on parcours les lignes de fiche
        lst.append(ligne.strip()) # on ajoute la ligne du fichier dans la liste lst en supprimant les '\n'
    return lst # on renvoie la liste lst

def emplacement_libre(lst):
    """
    Fonction qui prend en compte chaque point présent dans la liste lst,
    et renvoie une liste nommer case_libre qui contient les coordonées de chaque point présent dans le labyrinthe.
    Les points schématisent les cases libres.

    :param lst:
    :return case_libre:

    >>> emplacement_libre(lst)
    [(1, 18), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 8), (2, 9), (2, 10), (2, 11), (2, 18), (3, 4), (3, 9), (3, 11),
    (3, 12), (3, 13), (3, 14), (3, 16), (3, 17), (3, 18), (3, 19), (3, 20), (3, 21), (3, 22), (4, 1), (4, 4), (4, 9), (4, 14), (4, 16),
    (4, 22), (5, 1), (5, 4), (5, 9), (5, 10), (5, 11), (5, 12), (5, 14), (5, 16), (5, 20), (5, 22), (6, 1), (6, 4), (6, 7), (6, 9),
    (6, 12), (6, 14), (6, 16), (6, 18), (6, 19), (6, 20), (6, 21), (6, 22), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7),
    (7, 8), (7, 9), (7, 12), (7, 14), (7, 18), (8, 1), (8, 9), (8, 11), (8, 12), (8, 14), (8, 15), (8, 16), (8, 17), (8, 18), (8, 19),
    (9, 1), (9, 3), (9, 6), (9, 7), (9, 9), (9, 12), (9, 14), (9, 17), (9, 19), (9, 20), (9, 21), (9, 22), (9, 23), (10, 1), (10, 2),
    (10, 3), (10, 6), (10, 7), (10, 8), (10, 9), (10, 12), (10, 14), (10, 17), (10, 23), (11, 1), (11, 3), (11, 12), (11, 14), (11, 15),
    (11, 16), (11, 17), (11, 23), (12, 1), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 12), (12, 17), (12, 18), (12, 19),
    (12, 20), (12, 21), (12, 22), (12, 23), (13, 1), (13, 8), (13, 9), (13, 10), (13, 11), (13, 12), (13, 13), (13, 14), (13, 17),
    (13, 23), (14, 1), (14, 2), (14, 3), (14, 4), (14, 6), (14, 10), (14, 12), (14, 14), (14, 15), (14, 16), (14, 17), (14, 18), (14, 19),
    (14, 23), (15, 1), (15, 4), (15, 6), (15, 10), (15, 12), (15, 19), (15, 21), (15, 22), (15, 23), (16, 1), (16, 3), (16, 4), (16, 6),
    (16, 7), (16, 8), (16, 9), (16, 10), (16, 12), (16, 13), (16, 14), (16, 15), (16, 16), (16, 17), (16, 19), (16, 23), (17, 1), (17, 10),
    (17, 17), (17, 19), (17, 20), (17, 21), (18, 1), (18, 2), (18, 3), (18, 4), (18, 5), (18, 6), (18, 7), (18, 8), (18, 10), (18, 17),
    (18, 21), (19, 1), (19, 8), (19, 10), (19, 14), (19, 15), (19, 16), (19, 17), (19, 18), (19, 19), (19, 20), (19, 21), (19, 22),
    (20, 1), (20, 3), (20, 5), (20, 8), (20, 10), (20, 11), (20, 12), (20, 14), (20, 21), (20, 23), (21, 1), (21, 3), (21, 5), (21, 8),
    (21, 10), (21, 14), (21, 16), (21, 17), (21, 18), (21, 19), (21, 20), (21, 21), (21, 22), (21, 23), (22, 1), (22, 3), (22, 5),
    (22, 8), (22, 10), (22, 14), (22, 16), (22, 23), (23, 1), (23, 3), (23, 5), (23, 8), (23, 10), (23, 14), (23, 16), (23, 17),
    (23, 18), (23, 19), (23, 20), (23, 21), (23, 22), (23, 23), (24, 1), (24, 2), (24, 3), (24, 5), (24, 6), (24, 7), (24, 8),
    (24, 9), (24, 10), (24, 11), (24, 12), (24, 13), (24, 14), (24, 15)]
    """
    case_libre = [] # on crée une liste local case_libre
    for y in range(26): # on parcours y de 0 à 25
        for x in range(25): # on parcours x de 0 à 24
            if (lst[y][x] == '.') or (lst[y][x] == 'x'): # on teste si l'élément qui à pour coordonnée (y,x) est égale ou on à '.' ou 'x' 
                case_libre.append((y,x)) # Si c'est le cas alors on ajoute à case_libre l'élément(y,x)
    return case_libre # on renvoie la variacle case_libre

def emplacement_départ(lst):
    """
    Fonction qui prend en compte le point de départ présent dans la liste lst,
    et renvoie les coordonnées de départ du personnage dans le labyrinthe.
    L'arobase shématise le point de départ.

    :param lst:
    :return emplacement_perso:

    >>> emlacement_départ(lst)
    (25, 5)
    """
    emplacement_perso = (0, 0) # on crée une variable local emplacement_sortie sous la forme(0, 0)
    for y in range(26): # on parcours y de 0 à 25
        for x in range(25): # on parcours x de 0 à 24
            if lst[y][x] == '@': # on teste si l'élément qui à pour coordonnée (y,x) est égale ou non à '@' 
                emplacement_perso = (y,x) # Si c'est le cas alors on remplace emplacement_perso par l'élément (y,x)
    return emplacement_perso # on renvoie la variable emplacement_perso

def emplacement_sortie(lst):
    """
    Fonction qui prend en compte le point d'arriver présent dans la liste lst,
    et renvoie les coordonnées d'arriver du labyrinthe.
    Le x schématisse le point d'arriver.

    :param lst:
    :return case_sortie:

    >>> emplacement_sortie(lst)
    (0, 18)
    """
    case_sortie = (0, 0) # On crée une variable local case_sortie sous la forme (0, 0)
    for y in range(26): # On parcours y de 0 à 25
        for x in range(25): # on parcours x de 0 à 24
            if lst[y][x] == 'x': # on teste si l'élément qui à pour coordonnée (y, x) est égale ou non à 'x'.
                case_sortie = (y,x) # Si c'est le cas alors on remplace case_sortie par l'élément (y, x)
    return case_sortie # on renvoie la variable case_sortie

def affichage_ecran(lst, emplacement_perso, choix_de_direction, n):
    """
    Fonction qui prend en compte les éléments présent autour du personnage, à partir de la liste lst.
    Et renvoie un n(variable qui associe une situation afficher à l'écran à l'environnement présent autour du personnage)
    qui correspond au schéma dans le quelle on se trouve.

    :param lst:
    :param emplacement_perso:
    :param choixd_de_direction:
    :param n:

    >>> affichage_ecran(['******************x******', '******************.******', '*......*....******.******', '****.****.*....*.......**', \
    '*.**.****.****.*.*****.**', '*.**.****....*.*.***.*.**', '*.**.**.*.**.*.*.*.....**', '*.........**.*.***.******', \
    '*.*******.*..*......*****', '*.*.**..*.**.*.**.*.....*', '*...**....**.*.**.*****.*', '*.*.********.*....*****.*', \
    '*.*......***.****.......*', '*.******.......**.*****.*', '*....*.***.*.*......***.*', '*.**.*.***.*.******.*...*', \
    '*.*..*.....*......*.***.*', '*.********.******.*...***', '*........*.******.***.***', '*.******.*.***.........**', \
    '*.*.*.**.*...*.******.*.*', '*.*.*.**.*.***.*........*', '*.*.*.**.*.***.*.******.*', '*.*.*.**.*.***.*........*', \
    '*...*...........*********', '*****@*******************'], (25, 5), (0, -1), 0)
    5
    """

    # Liste de chaque paterne que l'on peut rencontrer dans le labyrinthe.
    Paterne_n1 = ['*','*','*','*','.','.','*','.','*']#Ce cas correspond à une situation ou l'on peut tourner à droite
    Paterne_n2 = ['*','*','*','.','.','*','*','.','*']#Ce cas correspond à une situation ou l'on peut tourner à gauche
    Paterne_n3 = ['*','.','*','*','.','*','*','.','*']#Ce cas correspond à une situation ou l'on peut avancer tout droit
    Paterne_n4 = ['*','.','*','.','.','*','*','.','*']#Ce cas correspond à une situation ou l'on peut tourner à gauche et avancer tout droit
    Paterne_n5 = ['*','.','*','*','.','.','*','.','*']#Ce cas correspond à une situation ou l'on peut tourner à droite et avancer tout droit
    Paterne_n6 = ['*','.','*','.','.','.','*','.','*']#Ce cas correspond à une situation ou l'on peut tourner à gauche, avancer tout droit et tourner à droite
    Paterne_n7 = ['*','*','*','.','.','.','*','.','*']#Ce cas correspond à une situation ou l'on peut tourner à gauche et tourner à droite
    Paterne_n8 = ['*','*','*','*','.','*','*','.','*']#Ce cas correspond à une situation sans issue
    #Ce cas correspond à une situation ou l'on peut avancer tout droit
    Paterne_n9 = ['*','.','.','*','.','*','*','.','*']
    Paterne_n10 = ['.','.','*','*','.','*','*','.','*']
    Paterne_n11 = ['.','.','.','*','.','*','*','.','*']
    #Ce cas correspond à une situation ou l'on peut tourner à gauche et tourner à droite
    Paterne_n12 = ['.','*','*','*','*','*','.','.','.']
    Paterne_n13 = ['*','*','.','*','*','*','.','.','.']
    Paterne_n14 = ['.','*','.','*','*','*','.','.','.']
    Paterne_n15 = ['*','*','*','*','*','*','.','.','.']
    Paterne_n16 = ['*','.','*','*','*','*','.','.','.']
    Paterne_n17 = ['.','.','.','*','*','*','.','.','.']
    Paterne_n18 = ['*','.','.','*','*','*','.','.','.']
    Paterne_n19 = ['.','.','*','*','*','*','.','.','.']
    #Ce cas correspond à une situation ou l'on peut tourner à droite
    Paterne_n20 = ['*','*','*','*','*','*','*','.','.']
    Paterne_n21 = ['*','*','.','*','*','*','*','.','.']
    Paterne_n22 = ['*','.','.','*','*','*','*','.','.']
    Paterne_n23 = ['.','.','.','*','*','*','*','.','.']
    Paterne_n24 = ['*','.','*','*','*','*','*','.','.']
    Paterne_n25 = ['.','*','.','*','*','*','*','.','.']
    Paterne_n26 = ['.','*','*','*','*','*','*','.','.']
    Paterne_n27 = ['.','.','*','*','*','*','*','.','.']
    #Ce cas correspond à une situation ou l'on peut tourner à gauche
    Paterne_n28 = ['*','*','*','*','*','*','.','.','*']
    Paterne_n29 = ['*','*','.','*','*','*','.','.','*']
    Paterne_n30 = ['*','.','.','*','*','*','.','.','*']
    Paterne_n31 = ['.','.','.','*','*','*','.','.','*']
    Paterne_n32 = ['*','.','*','*','*','*','.','.','*']
    Paterne_n33 = ['.','*','.','*','*','*','.','.','*']
    Paterne_n34 = ['.','*','*','*','*','*','.','.','*']
    Paterne_n35 = ['.','.','*','*','*','*','.','.','*']
    #Ce cas correspond à une situation ou l'on peut tourner à droite et avancer tout droit
    Paterne_n36 = ['*','*','*','*','.','*','*','.','.']
    Paterne_n37 = ['*','*','.','*','.','*','*','.','.']
    Paterne_n38 = ['*','.','.','*','.','*','*','.','.']
    Paterne_n39 = ['.','.','.','*','.','*','*','.','.']
    Paterne_n40 = ['*','.','*','*','.','*','*','.','.']
    Paterne_n41 = ['.','*','.','*','.','*','*','.','.']
    Paterne_n42 = ['.','*','*','*','.','*','*','.','.']
    Paterne_n43 = ['.','.','*','*','.','*','*','.','.']
    #Ce cas correspond à une situation ou l'on peut tourner à gauche et avancer tout droit
    Paterne_n44 = ['*','*','*','*','.','*','.','.','*']
    Paterne_n45 = ['*','*','.','*','.','*','.','.','*']
    Paterne_n46 = ['*','.','.','*','.','*','.','.','*']
    Paterne_n47 = ['.','.','.','*','.','*','.','.','*']
    Paterne_n48 = ['*','.','*','*','.','*','.','.','*']
    Paterne_n49 = ['.','*','.','*','.','*','.','.','*']
    Paterne_n50 = ['.','*','*','*','.','*','.','.','*']
    Paterne_n51 = ['.','.','*','*','.','*','.','.','*']
    #Ce cas correspond à une situation ou l'on peut tourner à gauche, avancer tout droit et tourner à droite
    Paterne_n52 = ['*','*','*','*','.','*','.','.','.']
    Paterne_n53 = ['*','*','.','*','.','*','.','.','.']
    Paterne_n54 = ['*','.','.','*','.','*','.','.','.']
    Paterne_n55 = ['.','.','.','*','.','*','.','.','.']
    Paterne_n56 = ['*','.','*','*','.','*','.','.','.']
    Paterne_n57 = ['.','*','.','*','.','*','.','.','.']
    Paterne_n58 = ['.','*','*','*','.','*','.','.','.']
    Paterne_n59 = ['.','.','*','*','.','*','.','.','.']
    #Ce cas correspond à une situation sans issue
    Paterne_n60 = ['*','*','*','*','*','*','*','.','*']
    Paterne_n61 = ['*','*','.','*','*','*','*','.','*']
    Paterne_n62 = ['*','.','.','*','*','*','*','.','*']
    Paterne_n63 = ['.','.','.','*','*','*','*','.','*']
    Paterne_n64 = ['*','.','*','*','*','*','*','.','*']
    Paterne_n65 = ['.','*','.','*','*','*','*','.','*']
    Paterne_n66 = ['.','*','*','*','*','*','*','.','*']
    Paterne_n67 = ['.','.','*','*','*','*','*','.','*']
    
    #Paterne qui permettent de controler l'affichage lorsque la sortie du labyrinthe se présente
    Paterne_n68 = ['*','x','*','*','.','*','*','.','*']
    Paterne_n69 = ['*','*','*','*','x','*','*','.','*']
    Paterne_n70 = ['*','*','*','*','*','*','*','.','*']

    #Paterne qui permmettent de contrôler l'affichage du jeu lorsque le personnage se trouve à l'entrée du jeu
    Paterne_n71 = ['*','.','*','*','.','*','.','.','@']
    Paterne_n72 = ['*','.','.','*','*','*','@','.','.']
    Paterne_n73 = ['*','*','*','*','@','*','.','.','*']

    cas = [] # Création d'une liste cas qui permet de mettre les éléments présent autour du personnage dans une liste de liste.
    if choix_de_direction == (0, -1): # on test le choix_de_direction pour pouvoir remplir la liste cas en fonction de notre orientation dans le labyrinthe
        y, x = emplacement_perso 
        y = int(y) #on convertit la valeur de y en entier pour éviter d'obtenir une string
        x = int(x) #on convertit la valeur de x en entier pour éviter d'obtenir une string
        if y == 1:
            #on remplit la liste cas pour chaque élément
            cas.append('*')
            cas.append('*')
            cas.append('*')
            cas.append('*')
            cas.append('*')
            cas.append('*')
            cas.append(lst[y][x-1])
            cas.append('.')
            cas.append(lst[y][x+1])
        elif y == 1:
            #on remplit la liste cas pour chaque élément
            cas.append('*')
            cas.append('*')
            cas.append('*')
            cas.append(lst[y-1][x-1])
            cas.append(lst[y-1][x])
            cas.append(lst[y-1][x+1])
            cas.append(lst[y][x-1])
            cas.append('.')
            cas.append(lst[y][x+1])
        else:
            #on remplit la liste cas pour chaque élément
            cas.append(lst[y-2][x-1]) 
            cas.append(lst[y-2][x]) 
            cas.append(lst[y-2][x+1])
            cas.append(lst[y-1][x-1])
            cas.append(lst[y-1][x])
            cas.append(lst[y-1][x+1]) 
            cas.append(lst[y][x-1])
            cas.append('.')
            cas.append(lst[y][x+1])
        #Ensuite on test si la liste cas rempli correspond ou non au paterne en question. Si oui on renvoie le n corespondant.
        if cas == Paterne_n1:
            n = 1 #couloir qui part à droite avec une profondeur de 3 rangs
        elif cas == Paterne_n2: 
            n = 3 #couloir qui part à gauche avec une profondeur de 3 rangs
        elif (cas == Paterne_n3) or (cas == Paterne_n68) or (cas == Paterne_n69) or (cas == Paterne_n70):
            n = 5 #couloir qui va tout droit avec une profondeur de 3 rangs
        elif cas == Paterne_n4:
            n = 7 #2 couloirs avec une profondeur de 3 rangs, un couloir part à gauche et un couloir part tout droit
        elif cas == Paterne_n5:
            n = 9 #2 couloirs avec une profondeur de 3 rangs, un couloir part à droite et un couloir part tout droit
        elif cas == Paterne_n6:
            n = 11 #3 couloirs avec une profondeur de 3 rangs, un couloir part à gauche, un couloir part tout droit, un couloir part à droite
        elif cas == Paterne_n7:
            n = 13 #2 couloirs avec une profondeur de 3 rangs, un couloir part à gauche et un couloir part à droite
        elif cas == Paterne_n8:
            n = 15 #voie sans issue avec une profondeur de 3 rangs
        elif (cas == Paterne_n9) or (cas == Paterne_n10) or (cas == Paterne_n11):
            n = 6 #couloir qui va tout droit avec une profondeur de 2 rangs
        elif (cas == Paterne_n12) or (cas == Paterne_n13) or (cas == Paterne_n14) \
              or (cas == Paterne_n15) or (cas == Paterne_n16) or (cas == Paterne_n17) \
              or (cas == Paterne_n18) or (cas == Paterne_n19):
            n = 14 #2 couloirs avec une profondeur de 2 rangs, un couloir part à gauche et un couloir part à droite
        elif (cas == Paterne_n20) or (cas == Paterne_n21) or (cas == Paterne_n22) \
              or (cas == Paterne_n23) or (cas == Paterne_n24) or (cas == Paterne_n25) \
              or (cas == Paterne_n26) or (cas == Paterne_n27):
            n = 2 #couloir qui part à droite avec une profondeur de 2 rangs
        elif (cas == Paterne_n28) or (cas == Paterne_n29) or (cas == Paterne_n30) \
              or (cas == Paterne_n31) or (cas == Paterne_n32) or (cas == Paterne_n33) \
              or (cas == Paterne_n34) or (cas == Paterne_n35):
            n = 4 #couloir qui part à gauche avec une profondeur de 2 rangs
        elif (cas == Paterne_n36) or (cas == Paterne_n37) or (cas == Paterne_n38) \
              or (cas == Paterne_n39) or (cas == Paterne_n40) or (cas == Paterne_n41) \
              or (cas == Paterne_n42) or (cas == Paterne_n43):
            n = 10 #2 couloirs avec une profondeur de 2 rangs, un couloir part à droite et un couloir part tout droit
        elif (cas == Paterne_n44) or (cas == Paterne_n45) or (cas == Paterne_n46) \
              or (cas == Paterne_n47) or (cas == Paterne_n48) or (cas == Paterne_n49) \
              or (cas == Paterne_n50) or (cas == Paterne_n51):
            n = 8 #2 couloirs avec une profondeur de 2 rangs, un couloir part à gauche et un couloir part tout droit
        elif (cas == Paterne_n52) or (cas == Paterne_n53) or (cas == Paterne_n54) \
              or (cas == Paterne_n55) or (cas == Paterne_n56) or (cas == Paterne_n57) \
              or (cas == Paterne_n58) or (cas == Paterne_n59):
            n = 12 #3 couloirs avec une profondeur de 2 rangs, un couloir part à gauche, un couloir part tout droit, un couloir part à droite
        elif (cas == Paterne_n60) or (cas == Paterne_n61) or (cas == Paterne_n62) \
              or (cas == Paterne_n63) or (cas == Paterne_n64) or (cas == Paterne_n65) \
              or (cas == Paterne_n66) or (cas == Paterne_n67):
            n = 16 #voie sans issue avec une profondeur de 2 rangs
        else:
            n = 17 #mur en face de nous
            
    if choix_de_direction == (-1, 0): # on test le choix_de_direction pour pouvoir remplir la liste cas en fonction de notre orientation dans le labyrinthe
        y, x = emplacement_perso
        y = int(y) #on convertit la valeur de y en entier pour éviter d'obtenir une string
        x = int(x) #on convertit la valeur de x en entier pour éviter d'obtenir une string
        if (y == 25) and (x == 5):
            #on remplit la liste cas pour chaque élément
            cas.append('*')
            cas.append(lst[y][x-2])
            cas.append(lst[y-1][x-2])
            cas.append('*')
            cas.append(lst[y][x-1])
            cas.append(lst[y-1][x-1])
            cas.append('*')
            cas.append('.')
            cas.append(lst[y-1][x])
        elif x == 1:
            #on remplit la liste cas pour chaque élément
            cas.append('*')
            cas.append('*')
            cas.append('*')
            cas.append(lst[y+1][x-1])
            cas.append(lst[y][x-1])
            cas.append(lst[y-1][x-1])
            cas.append(lst[y+1][x])
            cas.append('.')
            cas.append(lst[y-1][x])
        else:
            #on remplit la liste cas pour chaque élément
            cas.append(lst[y+1][x-2])
            cas.append(lst[y][x-2])
            cas.append(lst[y-1][x-2])
            cas.append(lst[y+1][x-1])
            cas.append(lst[y][x-1])
            cas.append(lst[y-1][x-1])
            cas.append(lst[y+1][x])
            cas.append('.')
            cas.append(lst[y-1][x])
        #Ensuite on test si la liste cas rempli correspond ou non au paterne en question. Si oui on renvoie le n corespondant.
        if cas == Paterne_n1:
            n = 1 #couloir qui part à droite avec une profondeur de 3 rangs
        elif cas == Paterne_n2:
            n = 3 #couloir qui part à gauche avec une profondeur de 3 rangs
        elif cas == Paterne_n3:
            n = 5 #couloir qui va tout droit avec une profondeur de 3 rangs
        elif cas == Paterne_n4:
            n = 7 #2 couloirs avec une profondeur de 3 rangs, un couloir part à gauche et un couloir part tout droit
        elif cas == Paterne_n5:
            n = 9 #2 couloirs avec une profondeur de 3 rangs, un couloir part à droite et un couloir part tout droit
        elif cas == Paterne_n6:
            n = 11 #3 couloirs avec une profondeur de 3 rangs, un couloir part à gauche, un couloir part tout droit, un couloir part à droite
        elif cas == Paterne_n7:
            n = 13 #2 couloirs avec une profondeur de 3 rangs, un couloir part à gauche et un couloir part à droite
        elif cas == Paterne_n8:
            n = 15 #voie sans issue avec une profondeur de 3 rangs
        elif (cas == Paterne_n9) or (cas == Paterne_n10) or (cas == Paterne_n11):
            n = 6 #couloir qui va tout droit avec une profondeur de 2 rangs
        elif (cas == Paterne_n12) or (cas == Paterne_n13) or (cas == Paterne_n14) \
              or (cas == Paterne_n15) or (cas == Paterne_n16) or (cas == Paterne_n17) \
              or (cas == Paterne_n18) or (cas == Paterne_n19) or (cas == Paterne_n72):
            n = 14 #2 couloirs avec une profondeur de 2 rangs, un couloir part à gauche et un couloir part à droite
        elif (cas == Paterne_n20) or (cas == Paterne_n21) or (cas == Paterne_n22) \
              or (cas == Paterne_n23) or (cas == Paterne_n24) or (cas == Paterne_n25) \
              or (cas == Paterne_n26) or (cas == Paterne_n27):
            n = 2 #couloir qui part à droite avec une profondeur de 2 rangs
        elif (cas == Paterne_n28) or (cas == Paterne_n29) or (cas == Paterne_n30) \
              or (cas == Paterne_n31) or (cas == Paterne_n32) or (cas == Paterne_n33) \
              or (cas == Paterne_n34) or (cas == Paterne_n35):
            n = 4 #couloir qui part à gauche avec une profondeur de 2 rangs
        elif (cas == Paterne_n36) or (cas == Paterne_n37) or (cas == Paterne_n38) \
              or (cas == Paterne_n39) or (cas == Paterne_n40) or (cas == Paterne_n41) \
              or (cas == Paterne_n42) or (cas == Paterne_n43):
            n = 10 #2 couloirs avec une profondeur de 2 rangs, un couloir part à droite et un couloir part tout droit
        elif (cas == Paterne_n44) or (cas == Paterne_n45) or (cas == Paterne_n46) \
              or (cas == Paterne_n47) or (cas == Paterne_n48) or (cas == Paterne_n49) \
              or (cas == Paterne_n50) or (cas == Paterne_n51):
            n = 8 #2 couloirs avec une profondeur de 2 rangs, un couloir part à gauche et un couloir part tout droit
        elif (cas == Paterne_n52) or (cas == Paterne_n53) or (cas == Paterne_n54) \
              or (cas == Paterne_n55) or (cas == Paterne_n56) or (cas == Paterne_n57) \
              or (cas == Paterne_n58) or (cas == Paterne_n59):
            n = 12 #3 couloirs avec une profondeur de 2 rangs, un couloir part à gauche, un couloir part tout droit, un couloir part à droite
        elif (cas == Paterne_n60) or (cas == Paterne_n61) or (cas == Paterne_n62) \
              or (cas == Paterne_n63) or (cas == Paterne_n64) or (cas == Paterne_n65) \
              or (cas == Paterne_n66) or (cas == Paterne_n67):
            n = 16 #voie sans issue avec une profondeur de 2 rangs
        else:
            n = 17 #mur en face de nous
                    
    if choix_de_direction == (1, 0): # on test le choix_de_direction pour pouvoir remplir la liste cas en fonction de notre orientation dans le labyrinthe
        y, x = emplacement_perso
        y = int(y) #on convertit la valeur de y en entier pour éviter d'obtenir une string
        x = int(x) #on convertit la valeur de x en entier pour éviter d'obtenir une string
        if (y == 25) and (x == 5):
            #on remplit la liste cas pour chaque élément
            cas.append(lst[y-1][x+2])
            cas.append(lst[y][x+2])
            cas.append('*')
            cas.append(lst[y-1][x+1])
            cas.append(lst[y][x+1])
            cas.append('*')
            cas.append(lst[y-1][x])
            cas.append('.')
            cas.append('*')
        elif x == 23:
            #on remplit la liste cas pour chaque élément
            cas.append('*')
            cas.append('*')
            cas.append('*')
            cas.append(lst[y-1][x+1])
            cas.append(lst[y][x+1])
            cas.append(lst[y+1][x+1])
            cas.append(lst[y-1][x])
            cas.append('.')
            cas.append(lst[y+1][x])
        else:
            #on remplit la liste cas pour chaque élément
            cas.append(lst[y-1][x+2])
            cas.append(lst[y][x+2])
            cas.append(lst[y+1][x+2])
            cas.append(lst[y-1][x+1])
            cas.append(lst[y][x+1])
            cas.append(lst[y+1][x+1])
            cas.append(lst[y-1][x])
            cas.append('.')
            cas.append(lst[y+1][x])
        #Ensuite on test si la liste cas rempli correspond ou non au paterne en question. Si oui on renvoie le n corespondant.
        if cas == Paterne_n1:
            n = 1 #couloir qui part à droite avec une profondeur de 3 rangs
        elif cas == Paterne_n2:
            n = 3 #couloir qui part à gauche avec une profondeur de 3 rangs
        elif cas == Paterne_n3:
            n = 5 #couloir qui va tout droit avec une profondeur de 3 rangs
        elif cas == Paterne_n4:
            n = 7 #2 couloirs avec une profondeur de 3 rangs, un couloir part à gauche et un couloir part tout droit
        elif cas == Paterne_n5:
            n = 9 #2 couloirs avec une profondeur de 3 rangs, un couloir part à droite et un couloir part tout droit
        elif cas == Paterne_n6:
            n = 11 #3 couloirs avec une profondeur de 3 rangs, un couloir part à gauche, un couloir part tout droit, un couloir part à droite
        elif cas == Paterne_n7:
            n = 13 #2 couloirs avec une profondeur de 3 rangs, un couloir part à gauche et un couloir part à droite
        elif cas == Paterne_n8:
            n = 15 #voie sans issue avec une profondeur de 3 rangs
        elif (cas == Paterne_n9) or (cas == Paterne_n10) or (cas == Paterne_n11):
            n = 6 #couloir qui va tout droit avec une profondeur de 2 rangs
        elif (cas == Paterne_n12) or (cas == Paterne_n13) or (cas == Paterne_n14) \
              or (cas == Paterne_n15) or (cas == Paterne_n16) or (cas == Paterne_n17) \
              or (cas == Paterne_n18) or (cas == Paterne_n19):
            n = 14 #2 couloirs avec une profondeur de 2 rangs, un couloir part à gauche et un couloir part à droite
        elif (cas == Paterne_n20) or (cas == Paterne_n21) or (cas == Paterne_n22) \
              or (cas == Paterne_n23) or (cas == Paterne_n24) or (cas == Paterne_n25) \
              or (cas == Paterne_n26) or (cas == Paterne_n27):
            n = 2 #couloir qui part à droite avec une profondeur de 2 rangs 
        elif (cas == Paterne_n28) or (cas == Paterne_n29) or (cas == Paterne_n30) \
              or (cas == Paterne_n31) or (cas == Paterne_n32) or (cas == Paterne_n33) \
              or (cas == Paterne_n34) or (cas == Paterne_n35):
            n = 4 #couloir qui part à gauche avec une profondeur de 2 rangs
        elif (cas == Paterne_n36) or (cas == Paterne_n37) or (cas == Paterne_n38) \
              or (cas == Paterne_n39) or (cas == Paterne_n40) or (cas == Paterne_n41) \
              or (cas == Paterne_n42) or (cas == Paterne_n43):
            n = 10 #2 couloirs avec une profondeur de 2 rangs, un couloir part à droite et un couloir part tout droit
        elif (cas == Paterne_n44) or (cas == Paterne_n45) or (cas == Paterne_n46) \
              or (cas == Paterne_n47) or (cas == Paterne_n48) or (cas == Paterne_n49) \
              or (cas == Paterne_n50) or (cas == Paterne_n51):
            n = 8 #2 couloirs avec une profondeur de 2 rangs, un couloir part à gauche et un couloir part tout droit
        elif (cas == Paterne_n52) or (cas == Paterne_n53) or (cas == Paterne_n54) \
              or (cas == Paterne_n55) or (cas == Paterne_n56) or (cas == Paterne_n57) \
              or (cas == Paterne_n58) or (cas == Paterne_n59) or (cas == Paterne_n71):
            n = 12 #3 couloirs avec une profondeur de 2 rangs, un couloir part à gauche, un couloir part tout droit, un couloir part à droite
        elif (cas == Paterne_n60) or (cas == Paterne_n61) or (cas == Paterne_n62) \
              or (cas == Paterne_n63) or (cas == Paterne_n64) or (cas == Paterne_n65) \
              or (cas == Paterne_n66) or (cas == Paterne_n67):
            n = 16 #voie sans issue avec une profondeur de 2 rangs
        else:
            n = 17 #mur en face de nous

    if choix_de_direction == (0, 1): # on test le choix_de_direction pour pouvoir remplir la liste cas en fonction de notre orientation dans le labyrinthe
        y, x = emplacement_perso
        y = int(y) #on convertit la valeur de y en entier pour éviter d'obtenir une string
        x = int(x) #on convertit la valeur de x en entier pour éviter d'obtenir une string
        if (y == 25) and (x == 5):
            #on remplit la liste cas pour chaque élément
            cas.append('*')
            cas.append('*')
            cas.append('*')
            cas.append('*')
            cas.append('*')
            cas.append('*')
            cas.append(lst[y][x+1])
            cas.append('.')
            cas.append(lst[y][x-1])
        elif y == 24:
            #on remplit la liste cas pour chaque élément
            cas.append('*')
            cas.append('*')
            cas.append('*')
            cas.append(lst[y+1][x+1])
            cas.append(lst[y+1][x])
            cas.append(lst[y+1][x-1])
            cas.append(lst[y][x+1])
            cas.append('.')
            cas.append(lst[y][x-1])
        else:
            #on remplit la liste cas pour chaque élément
            cas.append(lst[y+2][x+1])
            cas.append(lst[y+2][x])
            cas.append(lst[y+2][x-1]) 
            cas.append(lst[y+1][x+1])
            cas.append(lst[y+1][x])
            cas.append(lst[y+1][x-1])
            cas.append(lst[y][x+1])
            cas.append('.')
            cas.append(lst[y][x-1])
        #Ensuite on test si la liste cas rempli correspond ou non au paterne en question. Si oui on renvoie le n corespondant.
        if cas == Paterne_n1:
            n = 1 #couloir qui part à droite avec une profondeur de 3 rangs
        elif cas == Paterne_n2:
            n = 3 #couloir qui part à gauche avec une profondeur de 3 rangs
        elif cas == Paterne_n3:
            n = 5 #couloir qui va tout droit avec une profondeur de 3 rangs
        elif cas == Paterne_n4:
            n = 7 #2 couloirs avec une profondeur de 3 rangs, un couloir part à gauche et un couloir part tout droit
        elif cas == Paterne_n5:
            n = 9 #2 couloirs avec une profondeur de 3 rangs, un couloir part à droite et un couloir part tout droit
        elif cas == Paterne_n6:
            n = 11 #3 couloirs avec une profondeur de 3 rangs, un couloir part à gauche, un couloir part tout droit, un couloir part à droite
        elif cas == Paterne_n7:
            n = 13 #2 couloirs avec une profondeur de 3 rangs, un couloir part à gauche et un couloir part à droite
        elif cas == Paterne_n8 or (cas == Paterne_n73):
            n = 15 #voie sans issue avec une profondeur de 3 rangs
        elif (cas == Paterne_n9) or (cas == Paterne_n10) or (cas == Paterne_n11):
            n = 6 #couloir qui va tout droit avec une profondeur de 2 rangs
        elif (cas == Paterne_n12) or (cas == Paterne_n13) or (cas == Paterne_n14) \
              or (cas == Paterne_n15) or (cas == Paterne_n16) or (cas == Paterne_n17) \
              or (cas == Paterne_n18) or (cas == Paterne_n19):
            n = 14 #2 couloirs avec une profondeur de 2 rangs, un couloir part à gauche et un couloir part à droite
        elif (cas == Paterne_n20) or (cas == Paterne_n21) or (cas == Paterne_n22) \
              or (cas == Paterne_n23) or (cas == Paterne_n24) or (cas == Paterne_n25) \
              or (cas == Paterne_n26) or (cas == Paterne_n27):
            n = 2 #couloir qui part à droite avec une profondeur de 2 rangs 
        elif (cas == Paterne_n28) or (cas == Paterne_n29) or (cas == Paterne_n30) \
              or (cas == Paterne_n31) or (cas == Paterne_n32) or (cas == Paterne_n33) \
              or (cas == Paterne_n34) or (cas == Paterne_n35):
            n = 4 #couloir qui part à gauche avec une profondeur de 2 rangs
        elif (cas == Paterne_n36) or (cas == Paterne_n37) or (cas == Paterne_n38) \
              or (cas == Paterne_n39) or (cas == Paterne_n40) or (cas == Paterne_n41) \
              or (cas == Paterne_n42) or (cas == Paterne_n43):
            n = 10 #2 couloirs avec une profondeur de 2 rangs, un couloir part à droite et un couloir part tout droit
        elif (cas == Paterne_n44) or (cas == Paterne_n45) or (cas == Paterne_n46) \
              or (cas == Paterne_n47) or (cas == Paterne_n48) or (cas == Paterne_n49) \
              or (cas == Paterne_n50) or (cas == Paterne_n51):
            n = 8 #2 couloirs avec une profondeur de 2 rangs, un couloir part à gauche et un couloir part tout droit
        elif (cas == Paterne_n52) or (cas == Paterne_n53) or (cas == Paterne_n54) \
              or (cas == Paterne_n55) or (cas == Paterne_n56) or (cas == Paterne_n57) \
              or (cas == Paterne_n58) or (cas == Paterne_n59):
            n = 12 #3 couloirs avec une profondeur de 2 rangs, un couloir part à gauche, un couloir part tout droit, un couloir part à droite
        elif (cas == Paterne_n60) or (cas == Paterne_n61) or (cas == Paterne_n62) \
              or (cas == Paterne_n63) or (cas == Paterne_n64) or (cas == Paterne_n65) \
              or (cas == Paterne_n66) or (cas == Paterne_n67):
            n = 16 #voie sans issue avec une profondeur de 2 rangs
        else:
            n = 17 #mur en face de nous
            
    del cas
    return n

def spawn(n):
    efface_tout()
    for i in range(3):# on gère avec i qui varie de 0 à 2 la profondeur de l'affichage de la situation à l'écran dans laquelle le personnaga 
        if n == 1: #couloir qui part à droite avec une profondeur de 3 rangs
            if i == 0:
                rectangle(166, 100, 332, 200, couleur='black', remplissage='grey')# on trace un rectangle
                rectangle(332, 100, 500, 200, couleur='black', remplissage='grey') # on trace un rectangle
                rectangle(0, 100, 166, 200, couleur='black', remplissage='grey') # on trace un rectangle
            elif i == 1:
                polygone(((50, 30), (166, 100), (166, 200), (50, 307)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                polygone(((420, 65), (500, 0), (500, 350), (420, 280)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
            elif i == 2:
                polygone(((0, 0), (50, 30), (50, 307), (0, 350)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                
        elif n == 2: #couloir qui part à droite avec une profondeur de 2 rangs
            if i == 0:
                rectangle(166, 100, 332, 200, couleur='black', remplissage='grey') # on trace un rectangle
                rectangle(332, 100, 500, 200, couleur='black', remplissage='grey') # on trace un rectangle
                rectangle(0, 100, 166, 200, couleur='black', remplissage='grey') # on trace un rectangle
            elif i == 1:
                polygone(((0, 0), (166, 100), (166, 200), (0, 350)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                
        elif n == 3: #couloir qui part à gauche avec une profondeur de 3 rangs
            if i == 0:
                rectangle(166, 100, 332, 200, couleur='black', remplissage='grey') # on trace un rectangle
                rectangle(332, 100, 500, 200, couleur='black', remplissage='grey') # on trace un rectangle
                rectangle(0, 100, 166, 200, couleur='black', remplissage='grey') # on trace un rectangle
            elif i == 1:
                polygone(((332, 100), (445, 33), (445, 305), (332, 200)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                polygone(((0, 0), (90, 70), (90, 280), (0, 350)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
            elif i == 2:
                polygone(((445, 33), (500, 0), (500, 350), (445, 305)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                
        elif n == 4: #couloir qui part à gauche avec une profondeur de 2 rangs
            if i == 0:
                rectangle(166, 100, 332, 200, couleur='black', remplissage='grey') # on trace un rectangle
                rectangle(332, 100, 500, 200, couleur='black', remplissage='grey') # on trace un rectangle
                rectangle(0, 100, 166, 200, couleur='black', remplissage='grey') # on trace un rectangle
            elif i == 1:
                polygone(((332, 100), (500, 0), (500, 350), (332, 200)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                
        elif n == 5: #couloir qui va tout droit avec une profondeur de 3 rangs
            if i == 0:
                polygone(((166, 100), (216, 140), (216, 150), (166, 200)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                polygone(((305, 140), (355, 100), (355, 205), (305, 150)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
            elif i == 1:
                polygone(((50, 30), (166, 100), (166, 200), (50, 305)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                polygone(((355, 100), (445, 35), (445, 295), (355, 205)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
            elif i == 2:
                polygone(((0, 0), (50, 30), (50, 305), (0, 350)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté            
                polygone(((445, 35), (500, 0), (500, 350), (445, 295)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                
        elif n == 6: #couloir qui va tout droit avec une profondeur de 2 rangs
            if i == 0:
                polygone(((166, 100), (216, 140), (216, 150), (166, 200)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                polygone(((305, 140), (355, 100), (355, 205), (305, 150)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
            elif i == 1:
                polygone(((0, 0), (166, 100), (166, 200), (0, 350)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                polygone(((355, 100), (500, 0), (500, 350), (355, 205)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                
        elif n == 7: #2 couloirs avec une profondeur de 3 rangs, un couloir part à gauche et un couloir part tout droit
            if i == 0:
                rectangle(0, 100, 166, 200, couleur='black', remplissage='grey') # on trace un rectangle
                polygone(((166, 100), (216, 140), (216, 150), (166, 200)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                polygone(((305, 140), (355, 100), (355, 205), (305, 150)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
            elif i == 1:
                polygone(((355, 100), (445, 35), (445, 295), (355, 205)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                polygone(((0, 0), (90, 70), (90, 280), (0, 350)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
            elif i == 2:
                polygone(((445, 35), (500, 0), (500, 350), (445, 295)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                
        elif n == 8: #2 couloirs avec une profondeur de 2 rangs, un couloir part à gauche et un couloir part tout droit
            if i == 0:
                rectangle(0, 100, 166, 200, couleur='black', remplissage='grey') # on trace un rectangle
                polygone(((166, 100), (216, 140), (216, 150), (166, 200)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                polygone(((305, 140), (355, 100), (355, 205), (305, 150)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
            elif i == 1:
                polygone(((355, 100), (500, 0), (500, 350), (355, 205)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                
        elif n == 9: #2 couloirs avec une profondeur de 3 rangs, un couloir part à droite et un couloir part tout droit
            if i == 0:
                rectangle(322, 100, 500, 200, couleur='black', remplissage='grey') # on trace un rectangle
                polygone(((166, 100), (216, 140), (216, 150), (166, 200)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                polygone(((272, 140), (322, 100), (322, 200), (272, 150)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
            elif i == 1:
                polygone(((50, 30), (166, 100), (166, 200), (50, 305)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                polygone(((410, 70), (500, 0), (500, 350), (410, 280)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
            elif i == 2:
                polygone(((0, 0), (50, 30), (50, 305), (0, 350)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                
        elif n == 10: #2 couloirs avec une profondeur de 2 rangs, un couloir part à droite et un couloir part tout droit
            if i == 0:
                rectangle(322, 100, 500, 200, couleur='black', remplissage='grey') # on trace une rectangle
                polygone(((166, 100), (216, 140), (216, 150), (166, 200)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                polygone(((272, 140), (322, 100), (322, 200), (272, 150)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
            elif i == 1:
                polygone(((0, 0), (166, 100), (166, 200), (0, 350)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                
        elif n == 11: #3 couloirs avec une profondeur de 3 rangs, un couloir part à gauche, un couloir part tout droit, un couloir part à droite
            if i == 0:                         
                rectangle(332, 100, 500, 200, couleur='black', remplissage='grey') # on trace un rectangle
                polygone(((166, 100), (216, 140), (216, 150), (166, 200)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                rectangle(0, 100, 166, 200, couleur='black', remplissage='grey') # on trace un rectangle
                polygone(((282, 140), (332, 100), (332, 200), (282, 150)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
            elif i == 1:
                polygone(((0, 0), (90, 70), (90, 280), (0, 350)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                polygone(((410, 70), (500, 0), (500, 350), (410, 280)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                
        elif n == 12: #2 couloirs avec une profondeur de 3 rangs, un couloir part à gauche et un couloir part à droite
             if i == 0:                         
                rectangle(332, 100, 500, 200, couleur='black', remplissage='grey') # on trace un rectangle
                polygone(((166, 100), (216, 140), (216, 150), (166, 200)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                rectangle(0, 100, 166, 200, couleur='black', remplissage='grey') # on trace un rectangle
                polygone(((282, 140), (332, 100), (332, 200), (282, 150)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                
        elif n == 13: #2 couloirs avec une profondeur de 3 rangs, un couloir part à gauche et un couloir part à droite
            if i == 0:
                rectangle(166, 100, 332, 200, couleur='black', remplissage='grey') # on trace un rectangle
                rectangle(332, 100, 500, 200, couleur='black', remplissage='grey') # on trace un rectangle
                rectangle(0, 100, 166, 200, couleur='black', remplissage='grey') # on trace un rectangle
            elif i == 1:
                polygone(((0, 0), (90, 70), (90, 280), (0, 350)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                polygone(((410, 70), (500, 0), (500, 350), (410, 280)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                
        elif n == 14: #2 couloirs avec une profondeur de 2 rangs, un couloir part à gauche et un couloir part à droite
            if i == 0:
                rectangle(166, 100, 332, 200, couleur='black', remplissage='grey') # on trace un rectangle
                rectangle(332, 100, 500, 200, couleur='black', remplissage='grey') # on trace un rectangle
                rectangle(0, 100, 166, 200, couleur='black', remplissage='grey') # on trace un rectangle
                
        elif n == 15: #voie sans issue avec une profondeur de 3 rangs
            if i == 0:
                rectangle(166, 100, 332, 200, couleur='black', remplissage='grey') # on trace un rectangle
                rectangle(332, 100, 500, 200, couleur='black', remplissage='grey') # on trace un rectangle
                rectangle(0, 100, 166, 200, couleur='black', remplissage='grey') # on trace un rectangle
            elif i == 1:
                polygone(((50, 30), (166, 100), (166, 200), (50, 305)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                polygone(((332, 100), (445, 33), (445, 300), (332, 200)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
            elif i == 2:
                polygone(((0, 0), (50, 30), (50, 305), (0, 350)), couleur='black', remplissage='grey')  # on trace un polygone à quatre côté           
                polygone(((445, 33), (500, 0), (500, 350), (445, 300)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                
        elif n == 16: #voie sans issue avec une profondeur de 2 rangs
            if i == 0:
                rectangle(166, 100, 332, 200, couleur='black', remplissage='grey') # on trace un rectangle
                rectangle(332, 100, 500, 200, couleur='black', remplissage='grey') # on trace un rectangle
                rectangle(0, 100, 166, 200, couleur='black', remplissage='grey') # on trace un rectangle
            elif i == 1:
                polygone(((0, 0), (166, 100), (166, 200), (0, 350)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                polygone(((332, 100), (500, 0), (500, 350), (332, 200)), couleur='black', remplissage='grey') # on trace un polygone à quatre côté
                
        elif n == 17: #mur en face de nous
            if i == 0:
                rectangle(0, 0, 500, 350, couleur='black', remplissage='grey') # on trace un rectangle
        

def regard_a_gauche(avancer, reculer, aller_a_gauche, aller_a_droite):
    """
    Fonction qui modifie les valeurs des variables avancer, reculer, aller_a_gauche et
    aller_a_droite en fonction de la direction de vue du personnage.

    :param avancer: tuples
    :param reculer: tuples
    :param aller_a_gauche: tuples
    :param aller_a_droite: tuples
    :return lst

    >>> vision_gauche((0, -1),(0, 1),(-1, 0),(1, 0))
    ((-1, 0),(1, 0),(0, 1),(0, -1))
    """
    
    if (avancer == (0, -1)) and (reculer == (0, 1)) and (aller_a_gauche == (-1, 0)) and (aller_a_droite == (1, 0)):
        #On cherche à savoir quelles sont les valeurs des variables avancer, reculer, aller_a_gauche, aller_a_droite pour savoir de combien de dégré on doit tourner
        #Pour le regard, si le joueur appuye si le bouton camera_gauche, la camera va tourner de 90 degrés.
        avancer = (-1, 0) # avancer prend la valeur de aller_a_gauche
        reculer = (1, 0) # reculer prend la valeur de aller_a_droite
        aller_a_gauche = (0, 1) #aller_a_gauche prend la valeur de reculer
        aller_a_droite = (0, -1) #aller_a_droite prend la valeur de avancer
    elif (avancer == (-1, 0)) and (reculer == (1, 0)) and (aller_a_gauche == (0, 1)) and (aller_a_droite == (0, -1)):
        #On cherche à savoir quelles sont les valeurs des variables avancer, reculer, aller_a_gauche, aller_a_droite pour savoir de combien de dégré on doit tourner
        #Pour le regard, si le joueur appuye si le bouton camera_gauche, la camera va tourner de 90 degrés.
        avancer = (0, 1) # avancer prend la valeur de aller_a_gauche
        reculer = (0, -1) # reculer prend la valeur de aller_a_droite
        aller_a_gauche = (1, 0) #aller_a_gauche prend la valeur de reculer
        aller_a_droite = (-1, 0) #aller_a_droite prend la valeur de avancer
    elif (avancer == (0, 1)) and (reculer == (0, -1)) and (aller_a_gauche == (1, 0)) and (aller_a_droite == (-1, 0)):
        #On cherche à savoir quelles sont les valeurs des variables avancer, reculer, aller_a_gauche, aller_a_droite pour savoir de combien de dégré on doit tourner
        #Pour le regard, si le joueur appuye si le bouton camera_gauche, la camera va tourner de 90 degrés.
        avancer = (1, 0) # avancer prend la valeur de aller_a_gauche
        reculer = (-1, 0) # reculer prend la valeur de aller_a_droite
        aller_a_gauche = (0, -1) #aller_a_gauche prend la valeur de reculer
        aller_a_droite = (0, 1) #aller_a_droite prend la valeur de avancer
    elif (avancer == (1, 0)) and (reculer == (-1, 0)) and (aller_a_gauche == (0, -1)) and (aller_a_droite == (0, 1)):
        #On cherche à savoir quelles sont les valeurs des variables avancer, reculer, aller_a_gauche, aller_a_droite pour savoir de combien de dégré on doit tourner
        #Pour le regard, si le joueur appuye si le bouton camera_gauche, la camera va tourner de 90 degrés.
        avancer = (0, -1) # avancer prend la valeur de aller_a_gauche
        reculer = (0, 1) # reculer prend la valeur de aller_a_droite
        aller_a_gauche = (-1, 0) #aller_a_gauche prend la valeur de reculer
        aller_a_droite = (1, 0) #aller_a_droite prend la valeur de avancer
    return avancer, reculer, aller_a_gauche, aller_a_droite

def regard_a_droite(avancer, reculer, aller_a_gauche, aller_a_droite):
    """
    Fonction qui modifie les valeurs des variables avancer, reculer, aller_a_gauche et
    aller_a_droite en fonction de la direction de vue du personnage.

    :param avancer: tuples
    :param reculer: tuples
    :param aller_a_gauche: tuples
    :param aller_a_droite: tuples
    :return lst

    >>> vision_droite((0, -1),(0, 1),(-1, 0),(1, 0))
    ((1, 0),(-1, 0),(0, -1),(0, 1))
    """
    if (avancer == (0, -1)) and (reculer == (0, 1)) and (aller_a_gauche == (-1, 0)) and (aller_a_droite == (1, 0)):
        #On cherche à savoir quelles sont les valeurs des variables avancer, reculer, aller_a_gauche, aller_a_droite pour savoir de combien de dégré on doit tourner
        #Pour le regard, si le joueur appuye si le bouton camera_gauche, la camera va tourner de 90 degrés.
        avancer = (1, 0) #avancer prend la valeur de aller_a_droite
        reculer = (-1, 0) #reculer prend la valeur de aller_a_gauche
        aller_a_gauche = (0, -1) #aller_a_gauche prend la valeur de avancer
        aller_a_droite = (0, 1) #aller_a_droite prend la valeur de reculer
    elif (avancer == (1, 0)) and (reculer == (-1, 0)) and (aller_a_gauche == (0, -1)) and (aller_a_droite == (0, 1)):
        #On cherche à savoir quelles sont les valeurs des variables avancer, reculer, aller_a_gauche, aller_a_droite pour savoir de combien de dégré on doit tourner
        #Pour le regard, si le joueur appuye si le bouton camera_gauche, la camera va tourner de 90 degrés.
        avancer = (0, 1) #avancer prend la valeur de aller_a_droite
        reculer = (0, -1) #reculer prend la valeur de aller_a_gauche
        aller_a_gauche = (1, 0) #aller_a_gauche prend la valeur de avancer
        aller_a_droite = (-1, 0) #aller_a_droite prend la valeur de reculer
    elif (avancer == (0, 1)) and (reculer == (0, -1)) and (aller_a_gauche == (1, 0)) and (aller_a_droite == (-1, 0)):
        #On cherche à savoir quelles sont les valeurs des variables avancer, reculer, aller_a_gauche, aller_a_droite pour savoir de combien de dégré on doit tourner
        #Pour le regard, si le joueur appuye si le bouton camera_gauche, la camera va tourner de 90 degrés.
        avancer = (-1, 0) #avancer prend la valeur de aller_a_droite
        reculer = (1, 0) #reculer prend la valeur de aller_a_gauche
        aller_a_gauche = (0, 1) #aller_a_gauche prend la valeur de avancer
        aller_a_droite = (0, -1) #aller_a_droite prend la valeur de reculer
    elif (avancer == (-1, 0)) and (reculer == (1, 0)) and (aller_a_gauche == (0, 1)) and (aller_a_droite == (0, -1)):
        #On cherche à savoir quelles sont les valeurs des variables avancer, reculer, aller_a_gauche, aller_a_droite pour savoir de combien de dégré on doit tourner
        #Pour le regard, si le joueur appuye si le bouton camera_gauche, la camera va tourner de 90 degrés.
        avancer = (0, -1) #avancer prend la valeur de aller_a_droite
        reculer = (0, 1) #reculer prend la valeur de aller_a_gauche
        aller_a_gauche = (-1, 0) #aller_a_gauche prend la valeur de avancer
        aller_a_droite = (1, 0) #aller_a_droite prend la valeur de reculer
    return avancer, reculer, aller_a_gauche, aller_a_droite
                                  

def interface_jeu(choix_de_direction, avancer, reculer, aller_a_gauche, aller_a_droite):
    """
    Fonction qui qui prend en paramètre des tuples de valeurs. Et qui renvoie une direction en fonction du bouton presser par l'utilisateur.
    Si l'utilisateur presse le bouton avancer, la fonction va renvoyer un tuples de valeur qui indiquera la direction.

    :param direction_initiale: tuples
    :param avancer: tuples
    :param reculer: tuples
    :param aller_a_gauche: tuples
    :param aller_a_droite: tuples
    :return value

    >>> interfacejeu(choix_de_direction, avancer, reculer, aller_a_gauche, aller_a_droite, mouvement)
    ((0, -1),(0, -1),(0, 1),(-1 , 0),(1, 0),(0, -1))
    """
    
    #Le rectangle permet de d'encadrer la plateforme de jeu sur la fenetre.
    rectangle(1, 0, 500, 350, couleur='black', epaisseur=3)
    #La creation du bouton_gauche permet à l'utilisateur de choisir sa direction. (dans ce cas un pas à gauche.)
    bouton_gauche = [(250,400),(280,430)]
    rectangle(bouton_gauche[0][0], bouton_gauche[0][1], bouton_gauche[1][0], bouton_gauche[1][1],\
              couleur='black', remplissage='white', epaisseur=1, tag='gauche')
    texte(257, 405, f"←", taille =13, couleur='black')
    #La creation du bouton_reculer permet à l'utilisateur de choisir sa direction. (dans ce cas un pas en arrière.)
    bouton_reculer = [(280,400),(310,430)]
    rectangle(bouton_reculer[0][0], bouton_reculer[0][1], bouton_reculer[1][0], bouton_reculer[1][1],\
              couleur='black', remplissage='white', epaisseur=1, tag='reculer')
    texte(292, 405, f"↓", taille =13, couleur='black')
    #La creation du bouton_droite permet à l'utilisateur de choisir sa direction. (dans ce cas un pas à droite.)
    bouton_droite = [(310,400),(340,430)]
    rectangle(bouton_droite[0][0], bouton_droite[0][1], bouton_droite[1][0], bouton_droite[1][1],\
              couleur='black', remplissage='white', epaisseur=1, tag='droite')
    texte(317, 405, f"→", taille =13, couleur='black')
    #La creation de camera_gauche permet à l'utilisateur de choisir sa vicion. (dans ce cas voir à gauche.)
    camera_gauche = [(250,370),(280,400)]
    rectangle(camera_gauche[0][0], camera_gauche[0][1], camera_gauche[1][0], camera_gauche[1][1],\
              couleur='black', remplissage='white', epaisseur=1, tag='regarder à gauche')
    texte(262, 375, f"↺", taille =18, couleur='black')
    #La creation du bouton_avancer permet à l'utilisateur de choisir sa direction. (dans ce cas un pas en avant.)
    bouton_avancer = [(280,370),(310,400)]
    rectangle(bouton_avancer[0][0], bouton_avancer[0][1], bouton_avancer[1][0], bouton_avancer[1][1],\
              couleur='black', remplissage='white', epaisseur=1, tag='avancer')
    texte(292, 375, f"↑", taille =13, couleur='black')
    #La creation de camera_droite permet à l'utilisateur de choisir sa vision. (dans ce cas regarderà droite.)
    camera_droite = [(310,370),(340,400)]
    rectangle(camera_droite[0][0], camera_droite[0][1], camera_droite[1][0], camera_droite[1][1],\
              couleur='black', remplissage='white', epaisseur=1, tag='regarder à droite')
    texte(322, 375, f"↻", taille =18, couleur='black')
    
    mouvement = (0,0) # On définit une variable mouvement qui prend la valeur de la variable qui correspond au bouton pressé
    appuyer = attend_clic_gauche()
    while appuyer: # Tant que le joueur n'a pas appuyer sur un bouton, alors la boucle tourne
        # on teste si le joueur à appuyer sur le bouton_gauche
        if bouton_gauche[0][0] <= appuyer[0] and appuyer[0] <= bouton_gauche[1][0] and \
           bouton_gauche[0][1] <= appuyer[1] and appuyer[1] <= bouton_gauche[1][1]:
            mouvement = aller_a_gauche # Dans ce cas la variable mouvement prend la valeur de aller_a_gauche car on fait un pas à gauche
            # on teste si le joueur à appuyer sur le bouton_gauche
        elif bouton_reculer[0][0] <= appuyer[0] and appuyer[0] <= bouton_reculer[1][0] and \
             bouton_reculer[0][1] <= appuyer[1] and appuyer[1] <= bouton_reculer[1][1]:
            mouvement = reculer # Dans ce cas la variable mouvement prend la valeur de reculer car on fait un pas en arrière
            # on teste si le joueur à appuyer sur le bouton_droite
        elif bouton_droite[0][0] <= appuyer[0] and appuyer[0] <= bouton_droite[1][0] and \
             bouton_droite[0][1] <= appuyer[1] and appuyer[1] <= bouton_droite[1][1]:
            mouvement = aller_a_droite # Dans ce cas la variable prend la valeur de aller_a_droite car on fait un pas à droite
            # on teste si le joueur à appuyer sur le bouton camera_gauche
        elif camera_gauche[0][0] <= appuyer[0] and appuyer[0] <= camera_gauche[1][0] and \
             camera_gauche[0][1] <= appuyer[1] and appuyer[1] <= camera_gauche[1][1]:
            vue1 = regard_a_gauche(avancer, reculer, aller_a_gauche, aller_a_droite)
            #Vue que le joueur souhaite regarder à gauche alors on change les variables de avancer, reculer, aller_a_gauche et aller_a_droite en intervertissant les valeurs entre elles.
            for j in range(len(vue1)):
                if j == 0:
                    avancer = vue1[j]
                    choix_de_direction = avancer
                elif j == 1:
                    reculer = vue1[j]
                elif j == 2:
                    aller_a_gauche = vue1[j]
                elif j == 3:
                    aller_a_droite = vue1[j]
            mouvement = (0,0) # Ici la variable mouvement vaut (0, 0) car le personnage ne change pas de case, mais tourne juste sur lui-même
            # on teste si le joueur à appuyer sur le bouton_avancer
        elif bouton_avancer[0][0] <= appuyer[0] and appuyer[0] <= bouton_avancer[1][0] and \
             bouton_avancer[0][1] <= appuyer[1] and appuyer[1] <= bouton_avancer[1][1]:
            mouvement = avancer # Dans ce cas la variable mouvement prend la valeur de avancer car on fait un pas en avant
            # on teste sir le joueur à appuyer sur le bouton camera_droite
        elif camera_droite[0][0] <= appuyer[0] and appuyer[0] <= camera_droite[1][0] and \
             camera_droite[0][1] <= appuyer[1] and appuyer[1] <= camera_droite[1][1]:
            vue2 = regard_a_droite(avancer, reculer, aller_a_gauche, aller_a_droite)
            #Vue que le joueur souhaite regarder à gauche alors on change les variables de avancer, reculer, aller_a_gauche et aller_a_droite en intervertissant les valeurs entre elles.
            for z in range(len(vue2)):
                if z == 0:
                    avancer = vue2[z]
                    choix_de_direction = avancer
                elif z == 1:
                    reculer = vue2[z]
                elif z == 2:
                    aller_a_gauche = vue2[z]
                elif z == 3:
                    aller_a_droite = vue2[z]
            mouvement = (0,0) # Ici la variable mouvement vaut (0, 0) car le personnage ne change pas de case, mais tourne juste sur lui-même
        return choix_de_direction, avancer, reculer, aller_a_gauche, aller_a_droite, mouvement
    
def execution_personnage(mouvement, emplacement_perso, case_libre):
    """
    On prend on compte le mouvement choisie par l'utilisateur. Si il souhaite avancer d'un pas vers l'avant ou à droite ou à gauche ou vers l'arrière.
    Ceci modifiera donc les coordonnées du personnage sur le plateau de jeu.

    :param emplacement_perso:
    :param mouvement:
    :param case_libre:

    >>> execution_personnage((0,-1),(25, 5),(24, 5))
    (24, 5)
    """
    
    y, x = emplacement_perso # On place les valeurs présent dans le tuple de la varible emplacement_perso dans y et x
    nouvelle_position = emplacement_perso # on charge les veleurs présent dans emplacement_peros dans la variable nouvelle_position
    for libre in case_libre:
        if mouvement == (0, -1): # On teste si le mouvement est égale ou non à (0, -1)
            if (y-1, x) == libre: # On teste si les nouvelles coordonées calculer appartiennent à case_libre, si oui alors la variable nouvelle_position prend ses coordonnées
                nouvelle_position = (y-1, x)
        elif mouvement == (0, 1): # On teste si le mouvement est égale ou non à (0, 1)
            if (y+1, x) == libre: # On teste si les nouvelles coordonées calculer appartiennent à case_libre, si oui alors la variable nouvelle_position prend ses coordonnées
                nouvelle_position = (y+1, x)
        elif mouvement == (-1, 0): # on teste si le mouvement est égale ou non à (-1, 0)
            if (y, x-1) == libre: # On teste si les nouvelles coordonées calculer appartiennent à case_libre, si oui alors la variable nouvelle_position prend ses coordonnées
                nouvelle_position = (y, x-1)
        elif mouvement == (1, 0): # on teste si le mouvement est égale ou non à (1, 0)
            if (y, x+1) == libre: # On teste si les nouvelles coordonées calculer appartiennent à case_libre, si oui alors la variable nouvelle_position prend ses coordonnées
                nouvelle_position = (y, x+1)
        else:
            nouvelle_position = (y, x) #Si aucun des cas précedent ne coorespond alors on renvoie la nouvelle_position qui à pour valeur (y, x)
    return nouvelle_position

# Programme principal
if __name__ == "__main__":
    while ACCUEIL == True:
        #Initialisation du jeu
        #Variables et valeurs prises en compte par le programme pour jouer au jeu du labyrinthe 3D.
        framerate = 10 # taux de rafraîchissement du jeu en images
        lst = [] # Liste lst vide qui permettra de contenir chaque ligne du plan du labyrinthe sous la forme d'élément.
        direction_demarrage = (0, -1) # Direction de démarrage du personnage l'orsqu'il entre dans le labyrinthe.
        avancer = (0, -1)  #Variable pour faire un pas en avant
        reculer = (0, 1) # Variable pour faire un pas en arrière
        aller_a_gauche = (-1, 0) # Variable pour faire un pas à gauche
        aller_a_droite = (1, 0) # Variable pour faire un pas à droite
        mouvement =(0,0) # Variable qui indique le mouvement à exécuter
        
        #Création du labyrinthe
        n = 0# Permet d'obtenir les images 3D de l'endroit ou se trouve le personnage dans le labyrinthe.
        laby = "schéma.txt" #Fichier texte qui contient le schéma du labyrinthe
        case_libre = [] # lst des emplacement libre pour que le joueur puisse avancer dans le labyrinthe.
        lst = chargement_labyrinthe(laby) # on charge la liste renvoyer par la fonction chargement_labyrinthe dans la variable lst.
        emplacement_perso = emplacement_départ(lst) # Fonction qui rempli le tuple de l'emplacement de départ du personnage dans la labyrinthe et renvoie ce tuple dans la variable emplacement_perso
        case_sortie = emplacement_sortie(lst) # Fonction qui rempli le tuple de l'emplacment de sortie présent dans le labytinthe et renvoie ce tuple dans la variable case_sortie
        case_libre = emplacement_libre(lst) # Fonction qui rempli la liste de tous les emplacements libres présent dans le labyrinthe et renvoie cette liste dans la variable case_libre
        # Création de la fenêtre Tk pour jeu au jeu
        cree_fenetre(taille_case * largeur_plateau, \
                     taille_case * hauteur_plateau)
        efface_tout()
        rectangle(0, 0, 600, 500, couleur='black', remplissage='black') #Fond d'écran de la page d'accueil.

        #Boucle principale
        bouton_start = [(250,250),(350,300)] #Création d'un bouton start pour pouvoir lancer le jeu.
        rectangle(bouton_start[0][0], bouton_start[0][1], bouton_start[1][0], bouton_start[1][1], \
                  couleur='lightblue', remplissage='lightblue', epaisseur=1, tag='accueil')
        # Permet de définir le forme du bouton.
        texte(280, 260, f"Start", taille=15, couleur = 'white') # Texte présent sur le bouton, dans ce cas 'Start'.
        texte(170, 170, f"Welcome to the game 'Maze'\n   Press start button to play", taille =15, couleur='white') # Texte descriptif de début de partie
        Jouer = False
        
        appuyer = attend_clic_gauche()
        while appuyer :
            if bouton_start[0][0] <= appuyer[0] and appuyer[0] <= bouton_start[1][0] and \
               bouton_start[0][1] <= appuyer[1] and appuyer[1] <= bouton_start[1][1]:
                # on teste si l'utilisateur à cliquer sur le bouton_start pour commencer une nouvelle partie. Si c'est le cas alors la partie commencera.
                # Si ce n'est pas le cas, alors le programme attend que l'utilisateur appuyer sur le bouton_start
                efface_tout()
                Jouer = True
                break
            
        mise_a_jour()
        choix_de_direction = direction_demarrage
        while Jouer:
            #Affichage des boutons ainsi que les couloirs du labyrinthe
            efface_tout()
            n = affichage_ecran(lst, emplacement_perso, choix_de_direction, n) # on prend la valeur renvoyer par la fonction affichage_ecran et on la plce dans la variable n 
            spawn(n) # on affiche les couloirs du labyrinthe présent autour du personnage
            # on prend les valeurs renvoyer par la fonction interface_jeu et on place les valeurs respectivement dans les variables choix_de_direction, avancer, reculer, aller_a_gauche, aller_a_droite, mouvement 
            choix_de_direction, avancer, reculer, aller_a_gauche, aller_a_droite, mouvement = interface_jeu(choix_de_direction, avancer, reculer, aller_a_gauche, aller_a_droite)
            emplacement_perso = execution_personnage(mouvement, emplacement_perso, case_libre) # on prend la valeur renvoyer par la fonction et on la place dans la variable emplacement_perso
            # Ainsi, la nouvelle position du personnage remplace la valeur précedente dans la variable emplacement_pero. L'ancienne valeur est écrasée.
            mise_a_jour()

            #Gestion des évenements
            ev = donne_ev()
            ty = type_ev(ev)
            if ty == 'Quitte': # Si l'utilisateur souhaite quitter le jeu plus tôt, et qu'il appuye sur la croix de la fenetre alors le jeu s'arrête.
                Jouer = False
            elif emplacement_perso == case_sortie: # on teste si les coordonnées du personnage son identique à de la case_sortie. si c'est le cas, alors le jeu s'arrête.
            # Sinon le jeu continue
                Jouer = False
                mise_a_jour()
            sleep(1/framerate)
        efface_tout()
        rectangle(0, 0, 600, 500, couleur='black', remplissage='black') # Fond d'écran de la page de fin de Jeu
        texte(140, 125, f"Yes ! You've found the exit \n   Congratulations to you !\nDo you want to play again ?", taille =20, couleur='white')
        bouton_yes = [(130, 230),(250, 300)] # Création du bouton yes , pour recommmencer une nouvelle partie
        bouton_no = [(330, 230),(450, 300)] # Création du bouton no , pour finir définitive la partie et sortir du programme
        # Paramètre du bouton YES
        rectangle(bouton_yes[0][0], bouton_no[0][1], bouton_yes[1][0], bouton_yes[1][1],\
                  couleur='green', remplissage='green', epaisseur = 1, tag='YES')
        texte(170, 250, f"YES", taille = 15, couleur='white')
        # Paramètre du bouton NO
        rectangle(bouton_no[0][0], bouton_no[0][1], bouton_no[1][0], bouton_no[1][1],\
                  couleur='red', remplissage='red', epaisseur = 1, tag='NO')
        texte(380, 250, f"NO", taille = 15, couleur = 'white')
        
        appuyer = attend_clic_gauche()
        while appuyer:
            if bouton_yes[0][0] <= appuyer[0] and appuyer[0] <= bouton_yes[1][0] and \
               bouton_yes[0][1] <= appuyer[1] and appuyer[1] <= bouton_yes[1][1]:
                # on teste si l'utilisateur à appuyer sur le botuon_yes si c'est le cas, alors l'utilisateur reviens sur la page d'aacueil et peut commencer une nouvelle partie
                efface_tout()
                ACCUEIL = True
                break
            elif bouton_no[0][0] <= appuyer[0] and appuyer[0] <= bouton_no[1][0] and \
                 bouton_no[0][1] <= appuyer[1] and appuyer[1] <= bouton_no[1][1]:
                # on teste si l'utilisateur à appuyer sur le bouton_no si c'est le cas, alors l'utilisateur qui définitivement la jeu, et le programme s'arrête
                efface_tout()
                ACCUEIL = False
                break
            
        mise_a_jour()
        # Fermeture de la fenetre
        ferme_fenetre()
    # sortie du programme
    sys.exit()
        

