Python update_version.py
cd NMBON
python setup.py sdist
twine upload dist/*
cd src
RMDIR /S /Q NMBON.egg-info
cd ..
RMDIR /S /Q dist
pause
pip install NMBON --upgrade
pause