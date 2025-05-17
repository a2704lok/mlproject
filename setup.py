from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of packages.
    """
    with open(file_path) as file:
        requirements = file.readlines()
    
    # Remove any whitespace characters like `\n` at the end of each line
    requirements = [req.strip() for req in requirements]
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    # If -e . is present, remove it
    return requirements


setup(
    name='ml_project',
    version='0.1',
    author='Alok Kumar',
    author_email='alokkumarsingh230@gmail.com',
    description='A simple ML project',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
    