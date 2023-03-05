## fonctions utiles au debug programme pendant son développement ##
## ces fonctions ne font pas partie du projet final ##
## ne les implémentez que si cela vous est utile, vous pouvez évidemment en ajouter d'autres ##

from constantes import *
from fonctions_logique import *


# affiche un rubik en console en mode debug
# par exemple, affichage des 3 couleurs des cubelets :
             # ~ YGO|WBN|WBR|
             # ~ YNO|WNN|WNR|
             # ~ YBO|WGN|WGR|
                  # ~ U

# ~ YGO|YNO|YBO| YBO|WGN|WGR| WGR|WNR|WBR|   WBR|WBN|YGO|
# ~ NGO|NNO|NBO| NBO|NGN|NGR| NGR|NNR|NBR|   NBR|NBN|NGO|
# ~ WGO|WNO|WBO| WBO|YGN|YGR| YGR|YNR|YBR|   YBR|YBN|WGO|
     # ~ L            F           R               B

             # ~ WBO|YGN|YGR|
             # ~ WNO|YNN|YNR|
             # ~ WGO|YBN|YBR|
                  # ~ D
def debug_rubik(rubik):
			
	R=rubik
	#UP
	for y in range(3):
		print("                  ",end="")
		for x in range(3):
			print(R[x][2-y][2]," ",end="")
		print("")
		print("") 
		
	print()
	

	for z in range(3):
		#left
		for y in range(3):
			print(R[0][2-y][2-z]," ",end="")
		print("   ",end="")
		
		#front
		for x in range(3):
			print(R[x][0][2-z]," ",end="")
		print("   ",end="")
		
		#right
		for y in range(3):
			print(R[2][y][2-z]," ",end="")
		print("   ",end="")
		
		#back
		for x in range(3):
			print(R[2-x][2][2-z]," ",end="")
		print("   ",end="")
		print()
		print()
		
	#down
	print()
	
	for y in range(3):
		print("                  ",end="")
		for x in range(3):
			print(R[x][y][0]," ",end="")
			
		print("")
		print("")

# affiche une face en mode debug
# par exemple :
# ~ YGO|WBN|WBR|
# ~ YNO|WNN|WNR|
# ~ YBO|WGN|WGR|


def debug_face(face):
	for i in range(3):
		for j in range(3):
			print(face[2-i][j]," ",end="")
		print("")
		print("") 
	
	
