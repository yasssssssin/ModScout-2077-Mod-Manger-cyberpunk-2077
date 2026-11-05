@echo off
setlocal
cd /d "%~dp0"
title Build ModScout 2077

if not exist "cp2077_mod_toggle.py" goto :nofile

set "PY="
where py >nul 2>nul && set "PY=py -3"
if not defined PY where python >nul 2>nul && set "PY=python"
if not defined PY goto :nopython

echo Installing PyInstaller (one-time, about a minute)...
%PY% -m pip install --upgrade pyinstaller
if errorlevel 1 goto :fail

rem Pillow shows the mod pictures in Browse Nexus. Without it the program still works.
set "EXTRA="
echo.
echo Installing Pillow (for the mod pictures)...
%PY% -m pip install --upgrade pillow
if errorlevel 1 goto :nopillow
set "EXTRA=--hidden-import PIL.JpegImagePlugin --hidden-import PIL.PngImagePlugin --hidden-import PIL.WebPImagePlugin --hidden-import PIL.GifImagePlugin"
goto :build

:nopillow
echo.
echo Pillow could not be installed. The program will still work,
echo but Browse Nexus will show fewer pictures.

:build
rem The icon of the exe: put modscout.ico in this same folder. Without it the exe gets the default icon.
set "ICON="
if exist "modscout.ico" set "ICON=--icon modscout.ico"
echo.
if defined ICON echo Using the icon modscout.ico
if not defined ICON echo No modscout.ico next to this file, so the exe gets the default icon.
echo.
echo Building the exe...
%PY% -m PyInstaller --noconfirm --clean --onefile --windowed %ICON% %EXTRA% --name ModScout2077 cp2077_mod_toggle.py
if errorlevel 1 goto :fail

echo.
echo Done! Your program is here:
echo   %~dp0dist\ModScout2077.exe
echo You can move that single file anywhere. It does not need Python.
explorer "%~dp0dist"
pause
exit /b 0

:nofile
echo Put this file in the same folder as cp2077_mod_toggle.py and run it again.
pause
exit /b 1

:nopython
echo Python was not found.
echo Install it from https://www.python.org/downloads/ and tick the box
echo "Add python.exe to PATH" in the installer, then run this file again.
pause
exit /b 1

:fail
echo.
echo Something went wrong. Read the messages above, then tell Claude what they say.
pause
exit /b 1
