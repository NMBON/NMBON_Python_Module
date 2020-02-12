'''
Used to auto increment the version number for Pypi setup file
'''
import re

with open('.\\NMBON\\setup.py', "r", encoding="utf-8-sig") as input_file:
    INPUT_FILE = str(input_file.read())

OLD_VERSION = re.search('[0-9]+.[0-9]+.[0-9]+', INPUT_FILE).group()
NEW_VERSION = OLD_VERSION.split('.')[0] + '.'
NEW_VERSION += OLD_VERSION.split('.')[1] + '.'
NEW_VERSION += str(int(OLD_VERSION.split('.')[2])+1)

with open('.\\NMBON\\setup.py', "w", encoding="utf-8-sig") as output_file:
    output_file.write(re.sub(OLD_VERSION, NEW_VERSION, INPUT_FILE))
