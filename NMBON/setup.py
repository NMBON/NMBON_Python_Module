from setuptools import setup

setup(
    name = 'NMBON',
    version = '0.0.30',
    description = 'Boiler plate module for NMBON development',
    author = 'Hunter Pearson',
    author_email = 'hunter.pearson@state.nm.us',
    url = 'https://github.com/NMBON/nmbon_pip_module',
    
    py_modules = ["nmbon"],
    package_dir = {'': 'source'},

    install_requires=[
        'pyperclip'
    ]
)