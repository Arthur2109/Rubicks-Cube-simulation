The goal of this project is to simulate a rubiks cube. This is done by first developing the rubik in list form. We have to think about the structure of the rubik and how our functions will work. The second part is the creation of a GUI, including a convenient user interface and a 3D representation of the cube. We will use FreeCad for this.

The player chooses his mixing mode: random giving a random path composed of the number of desired moves from a completed state of the rubik, or scramble which generates a rubikub from a combination of moves entered by the player.

The program checks if the commands entered by the player are syntactically correct. It returns an error message if they are not.

A rotation is executed according to the following logic :

-extract the face you want to rotate (extract function)
-we turn this face (apply rotation function)
-we change the orientation of the colors
-we reimplant the face in the rubikub matrix (reimplant function, "inverse" of extract) graphic interface :
-display in the console the new rubikub matrix. It is a rubikub pattern displayed as if it was completely unfolded.

---ADAPTATION OF THE CODE TO FREECAD FOR THE GRAPHIC INTERFACE IN 3D:---

Description of the functions :


Generation of the cube in 3D: The function generate_rubik_3D will take in argument R, namely the rubik in the form of a matrix obtained through the part 1. It will then browse the matrix and create a cube of dimension 10 for each cubelet encountered. We then decide on its position by making sure to place it in space with respect to its real position in the cube. The next step is then to color these cubelets for the moment blank. We then use the color list created beforehand which associates to each color of the cube its color code in FreeCad. We only have to color each face of each cubelet according to the colors of the latter (which we obtain via the R matrix). There is now a function allowing to create a rubikcube in 3D no matter its basic configuration only with the R matrix (R is defined as a global variable in the whole function). The second step before the creation of the interface is now to create a function allowing to update the cube in real time according to the user's commands.

Movement of the cube in 3D: The function takes as argument the matrix representing the cube, a tuple representing the desired movement and on which face to apply it. It takes a boolean which translates the presence or not of animation in the program. Here we have only coded the case without animation so by default the animation must be False. First, we apply the desired movement to the 2D matrix of the rubik. Once this is done, we use the delete_old_cube function which allows us to delete all the 3D objects in FreeCad. So we will delete our old cube. Then we recreate with the function generate_rubik_3D the new cube having undergone the desired movement. By this process, we manage to create an impression of movement of the 3D cube.

Interface of the game: We now enter the interface part. It is necessary to maximize the user comfort. Therefore, our interface must be intuitive. We chose this rather sober interface. The command widget realized under QT allows the player to interact with the rubik.


As the operation of the buttons is quite similar, we will not develop in depth all the buttons. However, we will focus on the ones that reveal how our program works. But first of all, how does a normal game work? The user chooses his game mode among the two available ones, namely random and scramble. Once you click on one of the two buttons, the text "choice of mode" changes and you are asked to choose either the number of moves or the scramble combination. Once the information is entered, press "ok" and the cube is created. if the syntax is wrong, the entry is deleted and you have to start again. All that is left to do is to play rubik's with the different movements available via the buttons.

Assigning a text to the button

Creation of the button in the widget Here, we create the existence in the widget of the button. We associate its coordinates and its dimensions. We associate a name to this button (here scrambleButton). All that remains is to associate this button with a function (here "functionScramble" defined later).this is done by the function self.scrambleButton.clicked.connect(self.functionScramble).

Definition of the called function In our case our button will write in the editable area the text "What combination" in order to guide the user on how to proceed Thus, each button is connected to a function. Basically, the scramble and random buttons write a text in the text area, the ok button checks if the input is an integer or a string and adapts the operating mode accordingly. It will then create the cube according to the game mode. The delete button deletes the content of the text box to ensure user comfort. The delete button deletes the current cube. Finally, the different movement buttons allow you to move the cube as you wish. Once the blocks are nested together, the program can run and the user can complete a game from start to finish.

