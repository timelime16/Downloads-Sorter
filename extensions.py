# Map of extension types to destination
from collections import defaultdict
from config import AUDIO_PATH, IMAGE_PATH, VIDEOS_PATH, C_PATH, DATABASE_PATH, GO_PATH, JAVA_PATH, JAVASCRIPT_PATH, PYTHON_PATH, SHELL_PATH, EXCEL_PATH, POWERPOINT_PATH, WORD_PATH, PDF_PATH, TEXT_PATH, COMPRESSED_PATH, DEFAULT_PATH

extensions_folders = defaultdict(lambda: DEFAULT_PATH)
implemented_folders = {
    # Audio
    '.aif': AUDIO_PATH,
    '.cda': AUDIO_PATH,
    '.mid': AUDIO_PATH,
    '.midi': AUDIO_PATH,
    '.mp3': AUDIO_PATH,
    '.mpa': AUDIO_PATH,
    '.ogg': AUDIO_PATH,
    '.wav': AUDIO_PATH,
    '.wma': AUDIO_PATH,
    '.wpl': AUDIO_PATH,

    # Images
    '.ai': IMAGE_PATH,
    '.bmp': IMAGE_PATH,
    '.gif': IMAGE_PATH,
    '.ico': IMAGE_PATH,
    '.jpeg': IMAGE_PATH,
    '.jpg': IMAGE_PATH,
    '.png': IMAGE_PATH,
    '.ps': IMAGE_PATH,
    '.psd': IMAGE_PATH,
    '.scr': IMAGE_PATH,
    '.svg': IMAGE_PATH,
    '.tif': IMAGE_PATH,
    '.tiff': IMAGE_PATH,
    '.webp': IMAGE_PATH,

    # Videos
    '.3g2': VIDEOS_PATH,
    '.3gp': VIDEOS_PATH,
    '.avi': VIDEOS_PATH,
    '.flv': VIDEOS_PATH,
    '.h264': VIDEOS_PATH,
    '.m4v': VIDEOS_PATH,
    '.mkv': VIDEOS_PATH,
    '.mov': VIDEOS_PATH,
    '.mp4': VIDEOS_PATH,
    '.mpg': VIDEOS_PATH,
    '.mpeg': VIDEOS_PATH,
    '.rm': VIDEOS_PATH,
    '.swf': VIDEOS_PATH,
    '.vob': VIDEOS_PATH,
    '.webm': VIDEOS_PATH,
    '.wmv': VIDEOS_PATH,

    # Code
    '.c': C_PATH,
    '.cpp': C_PATH,
    '.db': DATABASE_PATH,
    '.dbf': DATABASE_PATH,
    '.sql': DATABASE_PATH,
    '.log': DATABASE_PATH,
    '.mdb': DATABASE_PATH,
    '.go': GO_PATH,
    '.java': JAVA_PATH,
    '.class': JAVA_PATH,
    '.js': JAVASCRIPT_PATH,
    '.ts': JAVASCRIPT_PATH,
    '.py': PYTHON_PATH,
    '.sh': SHELL_PATH, 

    # Microsoft
    '.xls': EXCEL_PATH,
    '.xlsm': EXCEL_PATH,
    '.xlsx': EXCEL_PATH,
    '.doc': WORD_PATH,
    '.docx': WORD_PATH,
    '.pps': POWERPOINT_PATH,
    '.ppt': POWERPOINT_PATH,
    '.pptx': POWERPOINT_PATH,

    # PDF
    '.pdf': PDF_PATH,
    
    # Text
    '.txt': TEXT_PATH,
    '.csv': TEXT_PATH,

    # Compressed files
    '.7z': COMPRESSED_PATH,
    '.arj': COMPRESSED_PATH,
    '.deb': COMPRESSED_PATH,
    '.pkg': COMPRESSED_PATH,
    '.rar': COMPRESSED_PATH,
    '.rpm': COMPRESSED_PATH,
    '.gz': COMPRESSED_PATH,
    '.z': COMPRESSED_PATH,
    '.zip': COMPRESSED_PATH,
}
extensions_folders.update(implemented_folders)
