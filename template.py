import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textsummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/_init_.py",
    f"src/{project_name}/components/_init_.py",
    f"src/{project_name}/utils/_init_.py",
    f"src/{project_name}/utils/common.py"
    f"src/{project_name}/logging/_init_.py",
    f"src/{project_name}/config/_init_.py",
    f"src/{project_name}/config/configuration/_init_.py",
    f"src/{project_name}/pipeline/_init_.py",
    f"src/{project_name}/entity/_init_.py",
    f"src/{project_name}/constants/_init_.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "requirements.txt",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/trials.ipynb"
    
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file{filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"creating wmpty file: {filepath}")



    else:
        logging.info(f"File {filepath} already exists.")
