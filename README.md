# Rubicks-Cube-simulation
Student project of a rubiks cube simulation (python) and user interface (Freecad)


Le but de ce projet est de simuler un rubiks cube. Cela passe dans un premier temps par le développement sous forme de listes du rubik. Il faut donc penser à la structure de celui-ci et à comment nos fonctions vont fonctionner. La seconde partie est quant à elle la création d’une interface graphique donc d’une interface utilisateur commode ainsi qu’une représentation 3D du cube. Nous utiliserons pour ceci le logiciel FreeCad.

Le joueur choisit son mode de mélange : aléatoire donnant un chemin aléatoire composé du
nombre de mouvements désirés à partir d’un état terminé du rubik, ou scramble qui génère
un rubikub à partir d’une combinaison de mouvements renseignés par le joueur.

Le programme vérifie si les commandes entrées par le joueur sont syntaxiquement justes. Il renvoie un message d’erreur dans le cas contraire.

Une rotation s'exécute informatiquement suivant la logique :
fonctions logiques :
1) on extrait la face qu’on souhaite tourner (fonction extraire)
2) on tourne cette face (fonction appliquer rotation)
3) on change l’orientation des couleurs
4) on réimplante la face dans la matrice rubikub (fonction reimplanter, “inverse”
d’extraire)
interface graphique :
5) afficher graphiquement dans la console la nouvelle matrice rubikub. C’est un patron
du rubikub affiché comme si ce dernier était complètement déplié.


---ADAPTATION DU CODE A FREECAD POUR L'INTERFACE GRAPHIQUE EN 3D:---

Description des fonctions :

Géneration du cube en 3D:
La fonction génerer_rubik_3D va prendre en argument R, à savoir le rubik sous forme
d’une matrice obtenue au travers de la partie 1. Il va alors parcourir la matrice et créer un
cube de dimension 10 pour chaque cubelet rencontré. On décide alors de sa position en
faisant en sorte de bien le placer dans l’espace vis-à-vis de sa position réelle dans le cube.
La prochaine étape est alors de colorier ces cubelets pour le moment vierge. On fait alors
appel à la liste couleurs créée au préalable qui associe à chaque couleur du cube son code
couleur dans FreeCad. Il ne nous reste plus qu’à colorer chaque face de chaque cubelet en
fonction des couleurs de ce dernier( que l’on obtient via la matrice R)
Il existe maintenant une fonction permettant de créer un rubikcube en 3D peut importe sa
configuration de base seulement avec la matrice R (R est défini en variable global dans
toute la fonction). La seconde étape avant la création de l’interface est maintenant de créer
une fonction permettant de mettre à jour le cube en temps réel selon les commandes de
l’utilisateur.

Mouvement du cube en 3D:
La fonction prend un argument la matrice représentant le cube, un tuple représentant le
mouvement voulu et sur quelle face l’appliquer. Elle prend un booléen qui traduit la présence
ou non d’animation dans le programme. Ici nous n’avons codé que le cas sans animation
donc par défaut l’animation doit être False. Dans un premier temps, on applique le
mouvement voulu à la matrice 2D du rubik. Une fois cela fait, on utilise la fonction
supprimer_ancien_cube qui permet d’effacer tous les objets 3D de FreeCad. Ainsi on va
supprimer notre ancien cube. Par la suite on recrée avec la fonction generer_rubik_3D le
nouveau cube ayant subi le mouvement voulu. Par ce procédé, on réussit à créer une
impression de mouvement du cube 3D.

Interface du jeu :
Nous rentrons maintenant dans la partie interface. Il est nécessaire de maximiser le confort
utilisateur. Par conséquent, notre interface se doit d’être intuitive. Notre choix s’est arrêté sur cette interface assez sobre. Le widget de commande réalisé sous QT permet au joueur
d’interagir avec le rubik.

Le fonctionnement des boutons étant assez similaire, nous ne développerons pas en
profondeur l’ensemble des boutons. Nous ciblerons cependant ceux qui sont révélateurs du
fonctionnement de notre programme.
Mais avant tout, comment se déroule une partie normale? L’utilisateur choisit son mode de
jeu parmi les deux disponibles à savoir aléatoire et scramble. Une fois cliqué sur l’un des
deux boutons le texte” choix du mode” change et l’on demande au choix soit le nombre de
mouvements soit la combinaison scramble. Une fois l’information rentrée on appuie sur “ok”
et le cube se crée.Si la syntaxe est fausse, la saisie s’efface et il faut recommencer. Il ne
reste plus qu’à jouer au rubik's avec les différents mouvements disponibles via les boutons.

1) Création du bouton dans le widget
Ici, on crée l’existence dans le widget du bouton. On lui associe ses coordonnées ainsi que
ses dimensions. On associe alors un nom à ce bouton (ici scrambleButton). Il ne reste plus
qu’à associer ce bouton à une fonction( ici “fonctionScramble” défini plus tard).Cela est
réalisé par la fonction self.scrambleButton.clicked.connect(self.fonctionScramble).

2) Attribution d’un texte au bouton

3) Définition de la fonction appelée
Dans notre cas notre bouton va écrire dans la zone éditable le texte “Quelle combinaison”
afin de guider l’utilisateur sur la démarche à suivre
Ainsi, chaque bouton est relié à une fonction. Dans les grandes lignes , le bouton scramble
et aléatoire écrivent un texte dans la zone de texte, le bouton ok vérifie si l’input est un entier
ou une chaîne de caractères et adapte le mode de fonctionnement en conséquence. Il va
alors créer le cube en fonction du mode de jeu. Le bouton effacer supprime le contenu de la
zone de texte afin de garantir un confort utilisateur. Le bouton supprimer supprime le cube
actuel. Enfin les différents boutons de mouvements permettent de mouvoir le cube comme
on le souhaite.
Une fois les blocs imbriqués entre eux, le programme peut fonctionner et l’utilisateur peut
réaliser une partie du début à la fin.




