@echo off
python -m pip install -r requirements.txt


if %errorlevel% neq=0 (
    echo Erro ao instalar as dependências.
    pause
    exit
)

python main.py

start "" /b cmd /c "timeout /t 2 >nul & del"%~f0""