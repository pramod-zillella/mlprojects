from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT= '-e .'
def get_requirements(filename:str)->List[str]:
    ''' 
    Read the requirements file and return the list of requirements
    '''
    requirements = []
    with open(filename, 'r') as file:
        requirements = file.readlines()
        requirements = [requirement.replace("\n", "") for requirement in requirements]
    
setup( 
    name='mlprojects', 
    version='0.1',
    author='Pramod',
    author_email= 'zillellapramod@gmail.com',   
    packages=find_packages(), 
    install_requires=get_requirements('requirements.txt')
)

# where setup.py is running the find_packages() function will search for the folders that contain __init__.py files and include them in the package. Once the packages are found, the install_requires parameter is used to specify the dependencies that are required for the package to run.