@echo off
cd %2
gmcompiler.exe %1 | findstr /r "^[Ee]rror"
if errorlevel 1 (goto noerror) else (color 0C)
goto end
:noerror
color 0A 
echo No syntax errors in %1.
:end
pause
