from setuptools import setup, find_packages
import pathlib
HERE = pathlib.Path(__file__).parent
README= (HERE/"README.md").read_text()

VERSION = '0.0.1' 
DESCRIPTION = 'In this package we simplifying the linked list concepts with useful functions'
LONG_DESCRIPTION = 'Created a module to automate the operations that can be performed using linked list such as creating a new node, adding a new element,inserting an element at the head node, tail node and required location, merging the linked lists,sorting,duplicates removing and deleting the elements etc.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="slinkedList", 
        version=VERSION,
        author="Sree Ramya Gudiwada",
        author_email="<sreeramyagud@gmail.com>",
        description=DESCRIPTION,
        long_description=README,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)