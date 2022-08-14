@echo off

:start
cls

python getdata.py %*
timeout /t 86400 /nobreak
tasklist | find /i "python.exe" >NUL && taskkill /f /im "python.exe" || taskkill /f /im "py.exe"

goto start