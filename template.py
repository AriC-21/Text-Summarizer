import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s')

project_name = "text-Summarizer"
list_files =[
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]

for file in list_files:
    file=Path(file)
    filedir,filename=os.path.split(file)

    if(filedir!=""):
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    if(not os.path.exists(file) or os.path.getsize(file)==0): 
        with open(file, 'w') as f:
            pass
            logging.info(f"Creating empty file: {file}")
    else:
        logging.info(f"{file} is already existing")