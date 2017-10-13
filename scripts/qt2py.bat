::Pyside-uic script for Windows
@echo off

SET basepath=%~dp0..\primecounter\view\gen\

for /f %%i in ('dir /b "%basepath%\qt"') do (
	pyside-uic -o "%basepath%%%~ni.py" "%basepath%qt\%%i"
	echo Converting %%i to %%~ni.py...
)

echo.
echo All ui files in  view\gen converted successfully!
