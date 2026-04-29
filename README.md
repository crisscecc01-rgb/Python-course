This is ASSIGNMENT 5 of the Python course. It has been developed by group N.5 :
Alberto De Davide mat. 2186228, phd student at DTG
Cristian Ceccolin mat. 2185895, phd student at DEI


Assignment description:
In this fifth assignment, additional data are stored during the randomization process, such as the starter type list 
and statistics as well as the enemy statistics ("hp", "attack", "defense",...). Such data are then used to train a 
machine learning model, which is based on the implementation of a random forest provided by the "sklearn" module. 
This model is than evaluated and stored, ready to be used as an advisor during the non-random condition of the game.


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
