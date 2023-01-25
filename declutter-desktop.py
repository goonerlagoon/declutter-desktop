'''
small script for organizing my desktop by clearing everything except
shortcut links and placing them in their appropriate location (i.e. "home_base").
Author:  Gavin A.
Date:    12-11-2021
'''

from pathlib import Path
from pathlib import PureWindowsPath

desktop_folder = Path.home() / 'Desktop'
home_base = Path.home() / 'Documents'

for file_obj in desktop_folder.glob('*/'):
    print(file_obj)
    if file_obj.is_dir():
        try:
            file_obj.replace(home_base / file_obj.parts[-1]) # parts[-1] grabs the file name plus ext
        except IOError as err:
            print(f"couldn't move {file_obj}. here's the error msg: {err}")
            continue
        except Exception as err:
            print(f"couldnt move {file_obj}. err msg: {err}")
            continue
    elif file_obj.suffix == '.lnk':
        file_obj.unlink()
    else:
        # extract the extension of each file and make it the dir name
        # in plural form if it doesnt already exist
        sfx = file_obj.suffix[1:].upper() + 's'
        try:
            extension_dir = home_base / sfx
            extension_dir.mkdir(exist_ok=True)
            file_obj.replace(extension_dir / file_obj.parts[-1])
        except Exception as err:
            print(f"couldnt move {file_obj}. err msg: {err}")
            continue

public_desktop = Path("C:\\Users\\Public\\Desktop\\")

for file_obj in public_desktop.glob('*/'):
    if file_obj.suffix == '.lnk':
        file_obj.unlink()

print("*" * 40)
print("PROCESS COMPLETE!")