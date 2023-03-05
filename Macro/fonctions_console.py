## fonctions pour l'interface utilisateur en console ##


from constantes import *
from fonctions_logique import *

# affiche un rubik en console
# le rubik est affiché en mode "déplié"
# exemple :
    # ~ WWW
    # ~ WWW
    # ~ YYY
     # ~ U

# ~ OOR GGG ORR   BBB
# ~ OOR GGG ORR   BBB
# ~ OOR GGG ORR   BBB
 # ~ L   F   R     B

    # ~ WWW
    # ~ YYY
    # ~ YYY
     # ~ D
     

def afficher_rubik(rubik):
	R=rubik
	#UP
	print("-------------------------------------------------")
	print("                  RUBIK'S'5/2                    ")   
	print("-------------------------------------------------")
	for y in range(3):
		print("              ",end="")
		for x in range(3):
			print(R[x][2-y][2][0]," ",end="")
		print("")
		print("") 
			
	print()

	for z in range(3):
		#left
		for y in range(3):
			print(c(R[0][2-y][2-z],"L")," ",end="")
		print("     ",end="")
		
		#front
		for x in range(3):
			print(c(R[x][0][2-z],"F")," ",end="")
		print("     ",end="")
		
		#right
		for y in range(3):
			print(c(R[2][y][2-z],"R")," ",end="")
		print("     ",end="")
		
		#back
		for x in range(3):
			print(c(R[2-x][2][2-z],"B")," ",end="")
		print("     ",end="")
		print()
		print()
		
	#down
	print()
	
	for y in range(3):
		print("              ",end="")
		for x in range(3):
			print(c(R[x][y][0],"D")," ",end="")
			
		print("")
		print("")

	
	
		
	#fait appel à generer_rubik_terminé
	
	

# retourne True si le saisie est un mouvement valide
# les mouvements valides sont une chaine de caractères sous la forme (F|L|R|U|D|B['|2])
def saisie_valide(saisie):
#On teste une part un par un les caractères de la chaine de caractère afin de vérifier que celui-ci à une syntaxe valide
	if len(saisie)==2:		
		if saisie[0] in {"F","L", "R" ,"U","D","B"} :	
			if saisie[1] == "'" or saisie[1] == "2":	
					return(True)
	if len(saisie)==1:
		if saisie[0] in {"F","L", "R" ,"U","D","B"}:
			return(True)
	return (False)
		
	
# permet la saisie d'un mouvement à effectuer
# sous la forme (F|L|R|U|D|B['|2])
# lettre = face
# ' = anti-horaire
# 2 = 180°				
# renvoie toujours un tuple valide (f, sens, double) : l'utilisateur est invité à recommencer sa saisie tant que celle-ci est invalide

def saisie_mouvement():
	x= input("quel mouvement?")
	while not saisie_valide(x) :
		x=input("quel mouvement?")
	return mouv(x)

# permet la saisie d'une suite de mouvements à effectuer		
# renvoie toujours une liste de tuples valide (f, sens, double) : l'utilisateur est invité à recommencer sa saisie tant que celle-ci est invalide
def saisie_mouvements():
	saisie=input("quels mouvements ?")
	return saisie
	
def valide (carac):			### vérifier si la chaine est une succession de mouvements
	if carac=="":
		return False
	L=[i for i in carac]
	c=""
	while L!=[]:
		if L[0] in {"F","L", "R" ,"U","D","B"}:
			c+=L.pop(0)
			if L!=[]:
				if L[0] in {"'","2"}:
					c+=L.pop(0)
		elif L[0]==" ":
			L.pop(0)
			if saisie_valide(c)==False:
				return False
			c=""
		
		else:
			return False
	return True
print(valide("F"))


def valide_nombre(carac):
	chiffres="0123456789"
	for i in carac:
		if i not in chiffres:
			return False
	return True
	
