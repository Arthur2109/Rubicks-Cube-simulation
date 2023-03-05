## le projet Rubik en interaction console (script executable) ##
print("")
print("Cette macro est l'interface utilisateur console du jeu rubikscube. A utiliser si vous n'avez pas Freecad. Pour une interface utilisateur plus pratique, executez la macro Freecad qui se situe dans ce meme dossier.")
print("")
print("Pour executer une combinaison de mouvements:\nLaissez un espace entre chaque mouvement\nUn mouvement se compose d'une face (FBRLUD) auquel on ajoute un sens de rotation (rien pour le sens horaire, ' pour le sens trigo) et d'un angle (par defaut 90, ajouter '2' pour faire 180 degrés).\nVoici un exemple de combinaison de mouvements :\nF' D R2")



from constantes import *
from fonctions_logique import *
from fonctions_console import *


# TODO


test=False
while test==False:
	a=input("0 : génération aléatoire       1 : scramble\n")  #choisir le mode de mélange (aléatoire ou scramble)
	if a=='0':                                                  # si aléatoire, on demande le nb de coups                                              
		n=input("combien de mouvements de mélange ? ")
		while not valide_nombre(n):                           # le caractère saisi doit être un nombre
			n=input("Erreur de syntaxe. Combien de mouvements de mélange ? ")
		R=generer_rubik(int(n))
		test=True
	elif a=="1":                                                 # si scramble, on demande la combinaison de coups
		comb=input("quelle combinaison faire ?")   
		while not valide(comb):                                  # le caractère doit être une suite de mouvements valides  
			comb=input("Erreur de syntaxe. Quelle combinaison faire ?")          
		R=generer_rubik_scramble(comb)
		test=True

afficher_rubik(R)
print("Le rubik est mélangé")
while victoire(R)==False: #on boucle jusqu'à la condition d'arrêt (victoire du joueur)
	ms=input("quelle combinaison faire ?")
	while not valide(ms):
		ms=input("Erreur de syntaxe. Quelle combinaison faire ?")
	R=m(R,ms)
	afficher_rubik(R)
	
print("VICTOIRE")
	

