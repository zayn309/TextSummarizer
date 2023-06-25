import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO , format = '[%(asctime)s] : %(message)s:')

project_name = 'textSummarizer'

list_of_files = [
    
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeLine/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
]

for filePath in list_of_files:
    filepath = Path(filePath)
    fileDir, fileName = os.path.split(filepath)

    if fileDir and not os.path.exists(fileDir):
        os.makedirs(fileDir, exist_ok=True)
        logging.info(f'Creating directory: {fileDir}')

    if not os.path.exists(filepath) or not os.path.getsize(filepath):
        with open(filePath, 'w') as f:
            pass
        logging.info(f'Creating file: {fileName}')

    else:
        logging.info(f'{fileName} already exists.')