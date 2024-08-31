# Helper functions
from datetime import date
from pathlib import Path
from config import DOWNLOADS_FOLDER, DESKTOP_FOLDER
from constants import DOWNLOAD_EXTENSIONS

def is_downloading(extension: str) -> bool:
    """
    Helper function that checks whether a file in the Downloads folder is still downloading
    """
    return extension in DOWNLOAD_EXTENSIONS

def add_date_to_path(path: Path):
    """
    Helper function that adds current year & month of download to destination path. If the path doesn't exist, it is created

    :param Path path: destination path (sorting folder) to apppend the subdirectories based on date
    """
    path_with_date = path / f'{date.today().year}' / f'{date.today().month:02d}'
    path_with_date.mkdir(parents=True, exist_ok=True)
    return path_with_date

def rename_file(source: Path, dest_path: Path):
    """
    Helper function that renames file to reflect new path. If a file of the same name already exists in the sorting folder, a number is appended
    to the file name and incremented until it is unique. This is to prevent overwriting of files.

    :param Path source: source of file to be moved
    :param Path destination_path: path to sorting folder 
    """
    new_name = dest_path / source.name
    increment = 2
    while new_name.exists():
        new_name = dest_path / f'{source.stem}_{increment}{source.suffix}'
        increment += 1
    return new_name

def check_folder_paths():
    """
    Helper function that ensures that DOWNLOADS_FOLDER and DESKPTOP_FOLDER are correct in config.py
    """
    downloads_path = Path(DOWNLOADS_FOLDER)
    desktop_path = Path(DESKTOP_FOLDER)
    if not downloads_path.exists():
        raise Exception("Downloads path does not exist")
    if not desktop_path.exists():
        raise Exception("Desktop path does not exist")

