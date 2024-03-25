import os
import shutil


file_extensions_and_types = {
    "txt": "Text Documents",
    "docx": "Text Documents",
    "pdf": "Text Documents",
    "odt": "Text Documents",
    "xlsx": "Spreadsheets",
    "csv": "Spreadsheets",
    "ods": "Spreadsheets",
    "pptx": "Presentations",
    "odp": "Presentations",
    "jpg": "Images",
    "jpeg": "Images",
    "png": "Images",
    "gif": "Images",
    "bmp": "Images",
    "svg": "Images",
    "mp3": "Audio",
    "wav": "Audio",
    "flac": "Audio",
    "m4a": "Audio",
    "mp4": "Video",
    "avi": "Video",
    "mkv": "Video",
    "mov": "Video",
    "wmv": "Video",
    "zip": "Compressed Files",
    "rar": "Compressed Files",
    "tar.gz": "Compressed Files",
    "tgz": "Compressed Files",
    "7z": "Compressed Files",
    "py": "Programming Code",
    "js": "Programming Code",
    "java": "Programming Code",
    "cpp": "Programming Code",
    "c": "Programming Code",
    "html": "Programming Code",
    "sqlite": "Database Files",
    "db": "Database Files",
    "sql": "Database Files",
    "exe": "Executable Files",
    "app": "Executable Files",
    "sh": "Executable Files",
    "ttf": "Fonts",
    "otf": "Fonts",
    "iso": "Archive and Disk Images",
    "dmg": "Archive and Disk Images",
    "img": "Archive and Disk Images",
    "xml": "Documents and Data Formats",
    "json": "Documents and Data Formats",
    "yaml": "Documents and Data Formats",
    "yml": "Documents and Data Formats",
    "other": "Other Files",
}


path = os.getcwd()  # Path to the directory


def main():
    folders, files = get_names(os.listdir(path))
    create_folders(folders)
    move(folders, files)


# Get all files and directories
def get_names(files_and_dirs):
    folders_name = []
    filenames = []
    for filename in files_and_dirs:
        if not os.path.isdir(f"{path}\\{filename}"):  # Check if it is file or directory
            file_ext = filename.split(".")[
                -1
            ]  # Get file extension for dictionary check
            if file_ext in file_extensions_and_types:
                folders_name.append(file_extensions_and_types[file_ext])
                filenames.append(filename)
            else:
                folders_name.append(file_extensions_and_types["other"])
                filenames.append(filename)
    return folders_name, filenames


# Create folders
def create_folders(folders):
    for folder in set(folders):
        os.mkdir(f"{path}\\{folder}")


# Move files into new folders
def move(foldername, filename):
    for file, folder in zip(filename, foldername):
        current = f"{path}\\{file}"
        destination = f"{path}\\{folder}"
        shutil.move(current, destination)


if __name__ == "__main__":
    main()





"""As it is a simple script where most functions don't have return values
I need to cheat a little with testing, that is my jar project from the past,
but i'm very proud of it, because I finally understood some of OOP"""


class Jar:
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError("Capacity can't be less than 1")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount to deposit must be non-negative")
        if self._size + amount > self._capacity:
            raise ValueError("The jar is full")
        self._size += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount to withdraw must be non-negative")
        if self._size - amount < 0:
            raise ValueError("Not enough cookies in the jar")
        self._size -= amount

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
