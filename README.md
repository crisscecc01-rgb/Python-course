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

