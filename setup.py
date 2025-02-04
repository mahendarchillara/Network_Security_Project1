
'''
The setup.py file is an essential part of packaging
and distributing python projects.it is used 
to define  configuration and more

'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirements
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read the line from the file
            lines=file.readlines()
            #process each line
            for line in lines:
                requirement=line.strip()
                #ignore empty lines and -e .
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst


# to setup metadata

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Mahendar Chillara",
    author_email="mahendarchillara464@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

