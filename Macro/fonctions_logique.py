## fonctions implémentant la logique du projet : ##
## génération du cube, mélange, application des mouvements, vérifications de victoire, etc. ## 

from constantes import *
from fonctions_debug import *

import random
import copy


# génère et retourne un rubik's cube résolu
# voir constantes.py pour la réprésentation
def generer_rubik_termine():

	A=[["OWB","NWB","RWB"],["ONB","NNB","RNB"],["OYB","NYB","RYB"]]
	B=[["OWN","NWN","RWN"],["ONN","NNN","RNN"],["OYN","NYN","RYN"]]
	C=[["OWG","NWG","RWG"],["ONG","NNG","RNG"],["OYG","NYG","RYG"]]
	
	rubik=[A,B,C]
	return rubik
	# TODO



# genere un rubik aleatoire
# nb_mouvs : nombre de mouvements aléatoires à appliquer
# retourne un tuple (rubik, scramble) (rubik : le cube généré, scramble : liste de tuples des mouvements effectués)
def generer_rubik(nb_mouvs):
		R=generer_rubik_termine()
		instruction=melanger(R,nb_mouvs)
		a=scramble(instruction)
		R=m(R,a)
		return(R)

# genere un rubik mélangé grâce au scramble en paramètre
# scramble : une cdc des mouvements à effectuer (par exemple "B2 F2 F' L2 B")
def generer_rubik_scramble(scramble):
	R=generer_rubik_termine()
	R=m(R,scramble)
	return R
	
# applique au rubik en paramètre nb_mouvs mouvements aléatoires
# retourne le scramble (liste de tuples des mouvements effectués)
def melanger(rubik,nb_mouvs):
	L=["F","B","L","R","U","D"]
	B=[True,False]
	scramble=[]
	for i in range(nb_mouvs):
		scramble.append((random.choice(L),random.choice(B),random.choice(B)))
	
	# TODO
	return scramble
		
	
# retourne la couleur du cubelet correspondante à la face demandée
# exemple : ("YGO", "U") renvoie "Y"
def c(cubelet,f):
	a=False
	if f in {"U","D"}:
		a=0
	elif f in {"F","B"}:
		a=1
	elif f in {"R","L"}:
		a=2
	return cubelet[a]

# les fonctions suivantes permettent d'extraire une face du rubik en paramètre
# la face retournée, une matrice à deux dimensions, est ordonnée comme si le rubik avait été déplié
# f : lettre de la face à extraire, f = caractère (U,L,F,R,B,D)
# note : ces fonctions ne modifient PAS l'orientation (couleur) des cubelets
def extraire(rubik, f):
	R=rubik
	
	if f=="F":
		return [[R[x][0][z] for x in range(3)] for z in range(3)]
		
	if f=="B":
		return [[R[2-x][2][z] for x in range(3)] for z in range(3)]
		
	if f=="R":
		return [[R[2][y][z] for y in range(3)] for z in range(3)]
		
	if f=="L":
		return [[R[0][2-y][z] for y in range(3)] for z in range(3)]
		
	if f=="U":
		return [[R[x][y][2] for x in range(3)] for y in range(3)]
		
	if f=="D":
		return [[R[x][2-y][0] for x in range(3)] for y in range(3)]
	

	
# applique une rotation à la face passée en paramètre
# cette fonction ne modifie PAS l'orientation (couleur) des cubelets
# face : matrice 2D de cubelets
# sens : True pour horaire
# double : True pour 180°
def appliquer_rotation(face, sens, double):
	if double:
		face1=[[face[2-i][2-j] for j in range(3)] for i in range(3)]
	
	else:                                            
		if sens :
			face1=[[face[i][2-j] for i in range(3)]for j in range(3)] #sens horaire 90°
		else:
			face1=[[face[2-i][j] for i in range(3)]for j in range(3)] #sens trigo 90°
	return face1
	
# reimplante (remplace) la face f de rubik avec les cubelets du paramètre face
# note : cette fonction n'applique PAS de rotation ou de réorientation des cubelets
# f : lettre de la face à remplacer, f = caractère (U,L,F,R,B,D)
# face : matrice 2D de cubelets

def reimplanter(rubik, f, face):
	R=rubik
	#A chaque fois que l'on veut implanter face dans R, il faut faire correspondre les 
	#COORDONNEES LOCALES de face et les COORDONNEES GLOBALES du rubik
	for z in range(3):
		if f=="F":          
			for x in range(3):
				R[x][0][z]=face[z][x]    #FAIRE TRES ATTENTION AUX COORDONNEES DE LA FACE (Z= lignes, x= colonnes)
	
		elif f=="B":
			for x in range(3):
				R[2-x][2][z]=face[z][x]

		elif f=="R":
			for y in range(3):
				R[2][y][z]=face[z][y]
		
		elif f=="L":
			for y in range(3):
				R[0][y][z]=face[z][2-y]
	
	for y in range(3):
		
		if f=="U":
			for x in range(3):
				R[x][y][2]=face[y][x]
		elif f=="D":
			for x in range(3):
				R[x][y][0]=face[2-y][x]
		
	return R

# effectue un mouvement du rubik
# extrait, applique la rotation, réoriente les couleurs et réimplante la face
# mouv est un tuple (f, sens, double)
# f = caractère (U,L,F,R,B,D)
# sens = booleen (True = horaire)
# double = boolean (True = 180°)
def appliquer_mouvement(rubik, mouv):
	(f,sens,double)=mouv
	face=extraire(rubik,f)
	face1=appliquer_rotation(face,sens,double)
	#réorientation des couleurs : on inverse les deux couleurs qui ne sont pas parallèle à la face.
	#méthode "bourin" car il faut réécrire les string qu'on ne peut pas manipuler comme des listes.
	if double==False: #on profite du fait que deux faces d'un cubelet en vis-à-vis ont les mêmes couleurs
		if f=="F" or f=="B":     #on regroupe les faces en vis-à-vis
			for i in range(3):
				for j in range(3):
					face1[i][j]=face1[i][j][2]+face1[i][j][1]+face1[i][j][0]
		elif f=="R" or f=="L":
			for i in range(3):
				for j in range(3):
					face1[i][j]=face1[i][j][1]+face1[i][j][0]+face1[i][j][2]
		elif f=="U" or f=="D" :
			for i in range(3):
				for j in range(3):
					face1[i][j]=face1[i][j][0]+face1[i][j][2]+face1[i][j][1]  
				
	rubik=reimplanter(rubik,f,face1)
	return rubik
# renvoie True si la face est terminée
# face : matrice 2D de cubelets
# f : caractère (U,L,F,R,B,D)
def face_terminee(face,f):  #bouclé pour toutes les faces, cette fonction permet de vérifier si le rubik est terminé
	if f=="F" or f=="B":a=1
	elif f=="R" or f=="L":a=2
	elif f=="U" or f=="D" :a=0
	couleur=face[1][1][a]
	for i in range(3):
		for j in range(3):
			if face[i][j][a]!=couleur:
				return False
	return True  #si toutes les couleurs sont identiques à "couleur"
	
# renvoie True si le cube est terminé
def victoire(rubik):
	L={"F","B","U","D","L","R"}
	for i in L:
		face=extraire(rubik,i)
		if face_terminee(face,i)==False:
			return False
	return True
	
# renvoie un tuple (face, sens, double) correspondant au mouvement m
# x : chaîne de caractères représentant un mouvement
# exemples: "F" renvoie ('F',True,False), "R'" renvoie ('R',False,False), "L2" renvoie ('L',False,True)
# x DOIT être valide
def mouv(x):
	if len(x) ==1:
		return(x[0],True,False)
	else:
		if x[1]==("'"):
			return(x[0],False,False)
		else:
			return(x[0],False,True)
			print("a")


# renvoie une liste de tuples correspondants aux mouvements ms
# ms : chaîne de caractères représentant des mouvements (scramble)
# exemple: "F R' L2" renvoie [('F',True,False),('R',False,False),('L',False,True)]
# ms DOIT être valide
def mouvements(ms):
	L=[]
	c=""
	for i in ms:
		if i==" ":
			L.append(mouv(c))
			c=""
		else:
			c=c+i
	L.append(mouv(c))
	return L

# applique les mouvements ms au cube rubik
# ms : chaîne de caractères représentant des mouvements (scramble)
def m(rubik, ms):
	mouv=mouvements(ms)
	for i in mouv:
		rubik=appliquer_mouvement(rubik,i)
	return rubik
	
# renvoie une chaîne de caractères correspondant aux mouvements mouvs
# exemple: [('F',True,False),('R',False,False),('L',False,True)] renvoie "F R' L2"
def scramble(mouvs):
	carac=""
	for m in mouvs:
		f,sens,double=m
		carac+=f
		if sens==False:
			carac+="'"
		elif double==True:
			carac+="2"
		carac+=" "
	corrige=""
	for i in range(len(carac)-1):	
		corrige+=carac[i] 
	return corrige
	

	
