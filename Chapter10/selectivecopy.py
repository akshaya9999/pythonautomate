import os
from pathlib import Path
import shutil


p=Path.cwd()
search=input('enter the file extension to search')
loc=input('enter copy location')
for foldername,subfolders,filenames in os.walk(p):
    for filename in filenames:
        if filename.endswith(search):
            shutil.copy(p/foldername/filename,loc)


