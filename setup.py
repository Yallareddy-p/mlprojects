# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''Read requirements file and return list of requirements'''
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        # Strip the newline characters and remove '-e .' if it exists
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    author='Yallareddy',
    author_email='pathakoti.ml@gmail.com',
    version='0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)