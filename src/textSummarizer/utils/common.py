import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:
    try:
        with open(path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path} loaded successfully!")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directory(paths: list,verbose = True):
    for path in paths:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
            
@ensure_annotations
def get_fileSize(file_path: str) -> str:
    path = Path(file_path)
    try:
        file_size_bytes = os.path.getsize(path)
        file_size_kb = file_size_bytes / 1024  # Convert bytes to kilobytes
        return f'~ {file_size_kb} KB'
    except OSError:
        raise FileNotFoundError("File not found")
    except Exception as e:
        raise e