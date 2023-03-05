## contient les constantes, structures de données et réprésentations utilisées dans le projet RUBIK ##

# taille du cube
TAILLE = 3

# couleurs du cube
# N = noir, B = bleu, W = blanc, Y = jaune, G = vert, O = orange, R = rouge
CO = ['N','B','W','Y','G','O','R']

# le cube est une matrice à 3 dimensions x,y,z réprésentée par une triple liste

# repère géométrique (identique à FreeCAD)
# z y
# |/
# --x

# chaque emplacement x,y,z dans la matrice (cubelet, ou cubie) est une chaîne de 3 caractères donnant ses couleurs et son orientation

# on nomme les faces selon l'orientation du cube de la manière suivante (imaginez le cube déplié) :
       # ~   U(p)
# ~ L(eft) F(ront) R(ight) - B(ack)
	  # ~    D(own)

# chaque cubelet est une chaîne de 3 caractères donnant les couleurs et l'orientation
# c1c2c3 : c1 = up/down, c2 = front/back, c3= left/right
# exemple : si cube[0][0][0] = "YGO", le cubelet en "bas-gauche-devant" (ou "Front-Left-Down", ou "FLD") est jaune sur ses faces Up/Down, vert sur ses faces Front/Back, orange sur ses faces Left/Right


