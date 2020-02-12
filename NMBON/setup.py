from setuptools import setup

import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Read the README.md into a string
with open('..\README.md', "r", encoding="utf-8-sig") as input_file:
    README = str(input_file.read())

setup(
    name = 'NMBON',
    version = '0.0.26',
    description = 'Boiler plate module for NMBON development',
    author = 'Hunter Pearson',
    author_email = 'hunter.pearson@state.nm.us',
    url = 'https://github.com/NMBON/nmbon_pip_module',
    long_description = README, #Use the same README.md as github
    
    py_modules = ["nmbon"],
    package_dir = {'': 'source'},

    install_requires=[
        'pyperclip'
    ]
)