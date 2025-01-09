import os
import yaml
from src.HeartAttackAnalysis.logging.logger import logging
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """Reads yaml file and returns 
    
    Args:
        path_to_yaml: Path to yaml file
    
    Raises:
        ValueError: if yaml file is Empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directory, verbose = True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directory:
        os.makedirs(path, exist_ok= True)
        if verbose:
            logging.info(f"created directory at: {path}")
    
    