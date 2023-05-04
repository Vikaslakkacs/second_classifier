import os
from pathlib import Path ##To create proper path depends on operating system
import logging
##Configuring logging basics
logging.basicConfig(level=logging.INFO, format= '[%(asctime)s]: %(message)s: ')
project_name="secondClassifier"

###Create list of file folder paths that has to be created
list_of_filefolders=[
    ##src/secondClassifier folders
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/config/__init__.py",
    ##Testing
    "tests/__init__.py",
    "tests/test/__init__.py",
    "tests/integration/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",##Data Version control pipeline
    "params.yaml",
    ##Env setup
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "requirements_dev.yaml",##Installation of tensorflow in mac M1
    "setup.py",
    "setup.cfg",    
    "pyproject.toml",##Python Packaging
    "tox.ini",##Local testing
    "research/stage_01.ipynb"##Jupyter notebook files

]

for filepath in list_of_filefolders:
    filepath= Path(filepath)
    print(filepath)
    file_dir, filename= os.path.split(filepath)
    print(f"file_dir:{file_dir}")
    ##If file directory is not empty then create file directory
    if file_dir !="":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"File directory has been created with {file_dir} for {filepath}")

    ##Create files inside folder paths if it doesn't exists and hsa file size 0
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        ##Create empty files
        with open(file= filepath, mode='w') as f:
            logging.info(f"File has been created in {filepath}")
            pass
    else:
        logging.info(f"file already exists with file name {filepath}")