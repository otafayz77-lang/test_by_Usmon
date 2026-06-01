@echo off
REM PowerShell-da loyihani tayyorlash script-i

echo ==================================
echo Django App - Deployment Preparation
echo ==================================
echo.

REM Activate virtual environment
echo [1/5] Virtual environment faollashtirilmoqda...
call env\Scripts\activate.bat

REM Install requirements
echo [2/5] Requirements o'rnatilmoqda...
pip install -r requirements.txt

REM Collect static files
echo [3/5] Static fayllar yig'ilmoqda...
python manage.py collectstatic --noinput

REM Run migrations
echo [4/5] Migrations ishga tushmoqda...
python manage.py migrate

REM Check Django setup
echo [5/5] Django setup tekshirilmoqda...
python manage.py check

echo.
echo ==================================
echo ✅ Tayyor! Render.com-ga joyash mumkin
echo ==================================
echo.
echo Keyingi qadamlar:
echo 1. Git repository yarating
echo 2. Render.com-da login qiling
echo 3. Bu repository-ni deploy qiling
echo.
pause