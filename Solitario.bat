@echo off
cd /d "%~dp0"
set PYTHONDONTWRITEBYTECODE=1
where py >nul 2>nul && (py -3 solitario.py) || (python solitario.py)
if errorlevel 1 pause
