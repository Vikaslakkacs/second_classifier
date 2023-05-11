import os
import yaml
from box import ConfigBox##Converts dictionary into proper format where we can access as functions
from pathlib import Path ##Provides correct path.

def read_yaml(filepath: Path)-> ConfigBox:
    """It takes file path, reads the file and converts yaml object which is easily accesible.

    Args:
        filepath (str): file path of yaml
    """
    with open(filepath) as yaml_file:
        content= yaml.safe_load(yaml_file)
        return ConfigBox(content)

def create_directory(file_dir: Path):
    """Creates file directory for the path passed
    """
    ## Checking if path exists and creates if not.
    if not os.path.exists(file_dir):
        os.makedirs(file_dir, exist_ok=True)