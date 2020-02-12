@echo off
:: Update the version in python
Python update_version.py
:: Move into directory
cd NMBON
:: Create a Source Distribution
python setup.py sdist
:: Upload Source Distribution to PyPI (https://pypi.org/project/NMBON/)
twine upload dist/*
:: Move into directory
cd source
:: Remove temp code 'egg'
RMDIR /S /Q NMBON.egg-info
:: Go up a directory
cd ..
:: Remove the generated code
RMDIR /S /Q dist


:: Clear the screen
cls
echo Please wait 40 seconds for the updated version of NMBON to be available to pip
: Wait for 20 seconds then continue
TIMEOUT /T 40
:: Clear the screen
cls

::upgrade NMBON in pip (Run multiple times to be sure)
pip install NMBON --upgrade
pip install NMBON --upgrade
pip install NMBON --upgrade
echo.
echo.
echo Update Complete
echo.
pause