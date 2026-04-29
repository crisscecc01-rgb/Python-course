This is ASSIGNMENT 3 of the Python course. It has been developed by group N.5 :
Alberto De Davide mat. 2186228, phd student at DTG
Cristian Ceccolin mat. 2185895, phd student at DEI


Assignment description:
In this third assignment the randomization is included. User has the possibility to play a randomized
game, by repeating the game creation multiple times and by playing multiple battles in each games 
in a completely automized and random way. User can still play the normal game. The randomization is very
simple since the "random user" will only enter the explore and battle zone and will only go through 
the battle tree by climbing the tree toward the leafs without ever going toward the root. 
Battle statistics are gathered as trainer attributes which are then passed to an outer scope gathering 
the battle statistics for each game. The datas are gathered in form of "story" as a dictionary of lists of 
dictionaries of lists. This is then exploded into a dataframe for manipulation and plotting of results and 
informations. 

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

