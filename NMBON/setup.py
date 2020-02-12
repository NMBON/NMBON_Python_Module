from setuptools import setup

setup(
    name = 'NMBON',
    version = '0.0.21',
    description = 'Boiler plate for NMBON development',
    author = 'Hunter Pearson',
    author_email = 'hunter.pearson@state.nm.us',
    url = 'https://github.com/user/reponame',
    
    
    py_modules = ["nmbon"],
    package_dir = {'': 'src'},

    install_requires=[
        'pyperclip'
    ]
)