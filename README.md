This is ASSIGNMENT 2 of the Python course. It has been developed by group N.5 :
Alberto De Davide mat. 2186228, phd student at DTG
Cristian Ceccolin mat. XXXXXXX, phd student at DEI


Assignment description:
In this second assignment a game engine is developed using the given FSM (from the moodle of the course). 
User have the possibility to create a new trainer selecting one starter. Then it automatically enters the story
and from here the trainer can go wherever he wants. At the Pokémon Store trainer can buy heals or pokeballs. 
At the Pokémon Center trainer can heal his Pokémons. Trainer can enter the Explore zone where he can find a
wild pokemon to fight with. The battle engine is based on a tree structure in order to move in the MENU selection
up and down as trainer wants. The tree is rebuilt in every battle turn in order to update nodes with heals, pokeballs, 
moves and pokemons available. User can exit the game selecting Exit from the story.

ALL THE FOLLOWING COMMANDS CAN BE SKIPPED BY EXECUTING FILE: initialize.bat
1) create VENV
    
WINDOWS:

    py -m venv pk_venv

LINUX\MACOS:

    python3 -m venv pk_venv

2) activate VENV:
	
WINDOWS:
	
    pk_venv\Scripts\activate

UX\MACOS:
	
    source pk_venv/bin/activate

3) install requirements:

WINDOWS/LINUX/MACOS: 
    
    pip install -r requirements.txt

4) run program:

WINDOWS:
    
    py main.py

LINUX\MACOS:

	python3 main.py
