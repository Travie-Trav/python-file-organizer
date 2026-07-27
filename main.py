# Imports
from pathlib import Path
import shutil

# Variables
base = Path.cwd()
files = list(base.iterdir())
categories = {
    "documents": [".docx", ".doc", ".pdf", ".txt", ".xlsx", ".pptx"],
    "images": [".png", ".jpeg", ".jpg", ".gif", ".svg", ".webp"],
    "audio": [".mp3", ".wav", ".flac"],
    "video": [".mp4", ".mkv", ".avi", ".mov"]
}

def create_folders():
    """Creates the folders if they do not already exist"""
    folder_names = ["Documents", "Videos", "Images", "Audio", "Misc"]
    
    for folder in folder_names:
        full_path = base / folder
        full_path.mkdir(exist_ok=True)
        
def classify_files(file):
    suffix = file.suffix.lower()
    for category, extension in categories.items():
        if suffix in extension:
            return category
        
    return "misc"

def move_files():
    folder_structure = {
                "documents": "Documents",
                "audio": "Audio",
                "video": "Videos",
                "images": "Images",
                "misc": "Misc"
            }
    
    for file in files:
        source = Path(file)
        
        if file.is_dir() or file.suffix.lower() == ".py":
            continue

        category = classify_files(file)
        destination_folder = folder_structure.get(category, "Misc")
        destination = base / destination_folder
        
        shutil.move(source, destination)

create_folders()
move_files()
