    # SIMPLE_SORT
    #### Video Demo:  https://youtu.be/6H3pgxqmOCo
    #### Description:
    As i don't like to work with files in python, I decided to make a file-related project.
    As follows from the title above this is a simple sorting "script", which will sort files by their extensions.
    It will create folders, depending on the file extensions and move those files to the suitable folder.
    How it works:
    It use only "os" and "shutil" modules, but I also used the "auto-py-to-exe" module te generate an ".exe" file for alternative usage.
    By default folder path is "os.getcwd()" so it will sort out the current folder.
    "get_names" function gets names of all files in folder, checks if it is a folder or an actual file,
    and if it is a file take it's extension as a key and create a list of names of folders we want to create.
    It has dict with main extensions and types, if there is no extension in the original dict,
    it will use "other" key, create the folder "Other files", and drop such files there.
    Than "create_folders" function turns the list of folder name to a set to avoid duplication folders.
    Last function "move" it the loop, that creates paths for files and folders via "zip()" and shutil does the rest.
    How to use:
    1. Use "simple_sort.py", specify the path to the directory in the "path" variable and run from any folder.
    2. Use "auto-py-to-exe simple_sort.py" in terminal to create an ".exe" file. Move the "simple_sort.exe" file in the folder and run it.