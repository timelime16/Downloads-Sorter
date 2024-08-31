import shutil
from pathlib import Path
from time import sleep
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from constants import DOWNLOAD_EXTENSIONS
from extensions import extensions_folders
from utils import is_downloading, add_date_to_path, rename_file

class EventHandler(FileSystemEventHandler):
    def __init__(self, downloads_path: Path):
        self.downloads_path = downloads_path.resolve()

    def on_modified(self, event: FileSystemEvent):
        for child in self.downloads_path.iterdir():
            if is_downloading(child.suffix.lower()):
                continue
            # To allow anti-virus to run checks on the newly downloaded files
            sleep(10)

            if child.is_file() or child.is_dir():
                dest_path = Path(extensions_folders[child.suffix.lower()])
                dest_path = add_date_to_path(dest_path)
                dest_path = rename_file(child, dest_path)
                shutil.move(src=child, dst=dest_path)


