'''
this is and essential part of packaging, and distributing python projects...used by setup tools to 
define configuration in project such as: 
metadata
dependencies and many more.....
'''

from setuptools import setup, find_packages #basically will scan the complete directory and where it will find the __init__.py, ye usse ek package ki tarah treat krega
from typing import List

def get_requirements()->List[str]:
    '''
    this fn, will return the list of requirements of our projects
    '''
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            #reading the complete file
            lines=file.readlines()
            for line in lines:
                requirement=line.strip() #will remove all the spaces
                # will ignore the empty lined and -e. ( so that redutant instllatiion of packages is avoided)
                '''
                Reads requirements.txt and returns a clean list of dependencies.
                
                Notes on '-e .':
                    '-e .' is used for editable installs in development (pip install -e .).
                    This links your project source to the Python environment so changes 
                    are reflected immediately without reinstalling.
                    
                    In MLOps production builds (Docker, CI/CD), '-e .' should be ignored because:
                        1. The source code may not be present at dependency installation time.
                        2. Editable mode is unnecessary in immutable deployments.
                    
                    Hence, we skip it when parsing requirements for production use.
                '''
                if requirement and requirement!='-e.':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print(' the specified file is not found!!')
        
    return requirement_list

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='arushKarnatak',
    author_email='arushkarnatak1881@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
    
)

print(get_requirements())