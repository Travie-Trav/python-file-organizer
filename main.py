# Imports
from pathlib import Path
import shutil

# Variables
base = Path.cwd()
files = list(base.iterdir())

def create_folders():
    """Creates the folders if they do not already exist"""
    folder_names = ["Documents", "Videos", "Pictures", "Music", "Misc"]
    
    for folder in folder_names:
        full_path = base / folder
        full_path.mkdir(exist_ok=True)

def move_files():
    for file in files:
        suffix = file.suffix.lower()
        source = Path(file)
        
        if file.is_dir():
            continue
        
        match suffix:
            case ".pdf" | ".docx" | ".doc":
                destination = Path(f"{base}/Documents")
                shutil.move(source, destination)
            case ".mp3":
                destination = Path(f"{base}/Music")
                shutil.move(source, destination)
            case ".mp4":
                destination = Path(f"{base}/Videos")
                shutil.move(source, destination)
            case ".jpg" | ".jpeg" | ".png":
                destination = Path(f"{base}/Pictures")
                shutil.move(source, destination)
            case ".py":
                continue
            case _:
                destination = Path(f"{base}/Misc")
                shutil.move(source, destination)

create_folders()
move_files()
