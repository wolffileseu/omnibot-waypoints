@echo off
if not exist %1 goto nodir
if not exist %2 goto nofile
cd %1
gmcompiler.exe %2 | findstr /r "^[Ee]rror"
if errorlevel 1 echo No syntax errors found in %2!
goto end
:nodir
echo Working directory %1 not found!
goto end
:nofile
echo File %2 not found!
:end