# Downloads File Manager

## Description
This project is a short Python script that helps manage your computer's Downloads folder. It is meant to be run as a background process and will sort any downloaded files into separate destination folders on the desktop. 
To prevent accidental overriding of files, the program will append a number to the end of the file name if it already exists in the destination folders.

The template of the destination folders can be found in and created using `destinationfolder.py`. <br> 
`config.py` must be edited for the script to work on your computer.

This program is easily customizable to fit how you want to sort the Downloaded files. All files that need to be edited are under the `custom` folder.

## Getting it Started
<b>Pre-requisite:</b> Make sure you have the latest version of Python installed. (Click [here](https://www.python.org/downloads/) if you do not)

1. Clone the repository onto your computer using `git clone <this_url>`
2. Navigate to the folder and install all dependencies
```
$ pip install -r requirements.txt
```
4. Open up `config.py` under the `custom` folder with an IDE. Edit `DOWNLOADS_FOLDER` and `DESKTOP_FOLDER` with the path to your Downloads and Desktop respectively. Put in your Operating System under `DIVIDER` (either WINDOWS, LINUX or MACOS)
```
DOWNLOADS_FOLDER = r'<downloads_folder_path>`
DESKTOP_FOLDER = r'<desktop_folder_path>'
DIVIDER = <OS, either WINDOWS, LINUX or MACOS>
```
4. Create the destination folders on your desktop <br> using `python destinationfolder.py`. Use `python3` for MacOS or Linux users
5. Run `sortdownloads.py`. All should be done!

As this program is meant to be running automatically in the background, a bash script for your computer should be written and included in your computer's tasks <b> TODO </b>

## Testing
<b> TODO </b>

## Customization
Under the `custom` folder, the program can be customized to your liking, in terms of the format of the destination folder and what file types each folder can store. <br> 
`config.py` defines all the paths to the destination folders. <br>
`extensions.py` defines the mapping of file type to destination. <br>
Remember to edit both files after you have customized the format of the destination folders.

## Additional Info
<b> How to find Downloads and Desktop path </b>
1. Navigate to the folder in your terminal
2. Type in `pwd` in your terminal. The file path will be displayed in the terminal
 
   
