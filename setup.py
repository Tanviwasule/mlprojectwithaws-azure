from setuptools import setup, find_packages
from typing import List
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->list[str]:
    """
    This function reads a requirements file and returns a list of packages.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements



setup(
    name='ml_project',
    version='0.0.1',
    author='Tanvi',
    author_email='tanviwasule9460@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)