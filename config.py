# File to edit to match the user's computer
from constants import *

# Folder: put in your filepath to the respective folder with the prefix 'r' eg. r'C:\Users\test\Downloads'
DOWNLOADS_FOLDER = r'foo'
DESKTOP_FOLDER = r'bar'
# Divider: put in your OS
DIVIDER = WINDOWS

# Destination folders for your sorter
completed_path = DESKTOP_FOLDER + DIVIDER 

MEDIA_PATH = completed_path + r'Media' + DIVIDER
AUDIO_PATH = MEDIA_PATH + r'Audio'
IMAGE_PATH = MEDIA_PATH + r'Images'
VIDEOS_PATH = MEDIA_PATH + r'Videos'

CODE_PATH = completed_path + r'Code' + DIVIDER
C_PATH = CODE_PATH + r'C or C++'
DATABASE_PATH = CODE_PATH + r'Database'
GO_PATH = CODE_PATH + r'Go'
JAVA_PATH = CODE_PATH + r'Java'
JAVASCRIPT_PATH = CODE_PATH + r'Javascript or Typescript'
PYTHON_PATH = CODE_PATH + r'Python'
SHELL_PATH = CODE_PATH + r'Shell'

DOCUMENT_PATH = completed_path + r'Document' + DIVIDER
MICROSOFT_PATH = DOCUMENT_PATH + r'Microsoft' + DIVIDER
EXCEL_PATH = MICROSOFT_PATH + r'Excel'
POWERPOINT_PATH = MICROSOFT_PATH + r'Powerpoint'
WORD_PATH = MICROSOFT_PATH + r'Word'
PDF_PATH = DOCUMENT_PATH + r'PDF'
TEXT_PATH = DOCUMENT_PATH + r'Text'

MISC_PATH = completed_path + r'Misc' + DIVIDER
COMPRESSED_PATH = MISC_PATH + r'Compressed'
DEFAULT_PATH = MISC_PATH + r'Others'
