pip install requests

@ECHO OFF

SETLOCAL

SET someOtherProgram=SomeOtherProgram.exe
TASKKILL /IM "%someOtherProgram%"

ECHO "This script will now self-destruct. Please ignore the next error message"
DEL "%~f0"