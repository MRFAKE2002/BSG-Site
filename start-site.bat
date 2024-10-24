@echo off
cd /d "."

python -m venv venv 
call .\venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

@REM @echo off
@REM cd /d "C:\Users\Nehzat\OneDrive\Desktop\BSG-Site\Code"

@REM echo Creating virtual environment...
@REM python -m venv venv
@REM echo Virtual environment created.

@REM echo Activating virtual environment...
@REM call .\venv\Scripts\activate
@REM echo Virtual environment activated.

@REM echo Installing libraries...
@REM pip install -r requirements.txt
@REM echo libraries has been installed.

@REM echo Making migrations...
@REM python manage.py makemigrations
@REM echo Migrations created.

@REM echo Applying migrations...
@REM python manage.py migrate
@REM echo Migrations applied.

@REM echo Running server...
@REM python manage.py runserver



@REM linux

@REM #!/bin/bash

@REM cd /home/user/My_Vscode/Django/Work_Group_Fake_Devs/Code

@REM echo "Activating virtual environment..."
@REM source ./venv/bin/activate
@REM echo "Virtual environment activated."

@REM echo "Making migrations..."
@REM python manage.py makemigrations
@REM echo "Migrations created."

@REM echo "Applying migrations..."
@REM python manage.py migrate
@REM echo "Migrations applied."

@REM echo "Running server..."
@REM python manage.py runserver