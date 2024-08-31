from pathlib import Path
from time import sleep
from watchdog.observers import Observer
from EventHandler import EventHandler
from config import DOWNLOADS_FOLDER
from utils import check_folder_paths

if __name__ == '__main__':
    check_folder_paths()
    
    event_handler = EventHandler(Path(DOWNLOADS_FOLDER))

    observer = Observer()
    observer.schedule(event_handler, DOWNLOADS_FOLDER, recursive=True)
    observer.start()

    try:
        while True:
            sleep(60)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()