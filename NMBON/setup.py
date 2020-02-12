from setuptools import setup

setup(
    name = 'NMBON',
    version = '0.0.25',
    description = 'Boiler plate for NMBON development',
    author = 'Hunter Pearson',
    author_email = 'hunter.pearson@state.nm.us',
    url = 'https://github.com/NMBON/nmbon_pip_module',
    long_description = 'Test!',
    
    py_modules = ["nmbon"],
    package_dir = {'': 'source'},

    install_requires=[
        'pyperclip'
    ]
)