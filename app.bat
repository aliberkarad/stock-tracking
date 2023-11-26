if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit
@echo off
@chcp 65001
@cls

@cd "C:\Users\Ali Berkay Karadeniz\Desktop\stok-takip"

echo ---------------------------------------
ipconfig
echo ---------------------------------------
echo.
echo.

@py manage.py runsslserver 0.0.0.0:900

echo. 
echo. 
echo --------------- BİTİŞ ------------------------
echo Çıkış için herhangi bir tuşa basınız ...
pause>nul
exit
