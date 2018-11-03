@echo off

echo Updating Inkscape local extensions in folder '%APPDATA%\inkscape\extensions'.

echo Removing existing cut-craft extensions.

del /Q %APPDATA%\inkscape\extensions\cutcraft*.inx > NUL
del /Q %APPDATA%\inkscape\extensions\cutcraft*.py > NUL
rmdir /S /Q %APPDATA%\inkscape\extensions\cutcraft

echo Installating latest cut-craft extensions.

copy /Y cutcraft*.inx %APPDATA%\inkscape\extensions > NUL
copy /Y cutcraft*.py %APPDATA%\inkscape\extensions > NUL
mkdir %APPDATA%\inkscape\extensions\cutcraft
xcopy /S /Q /Y ..\cutcraft %APPDATA%\inkscape\extensions\cutcraft > NUL

echo Installation of cut-craft extensions for Inkscape complete.
echo Restart Inkscape to ensure updates are available.
