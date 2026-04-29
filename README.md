This is ASSIGNMENT 1 of the Python course. It has been developed by group N.5 :
Alberto De Davide mat. 2186228, phd student at DTG
Cristian Ceccolin mat. 2185895, phd student at DEI

This Python project implements a prototype of the main classes required in order to develop a Pokémon simulator 
(first gen). The Database folder contains the main base Pokémon, a list of possible moves and the TYPE_CHART which 
is used to evaluate the effectivness of the moves based on the Pokémon types.
The main.py file implements a simple scripts which is used to test the battle system, in particulare the 
"Use_move" method of the PokemonCharacterClass.


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
