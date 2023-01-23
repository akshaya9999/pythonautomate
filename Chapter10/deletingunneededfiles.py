import os
from pathlib import Path
import shutil


p=Path.cwd()
for foldername,subfolders,filenames in os.walk(p):
    for filename in filenames:
        x=os.path.getsize(p/foldername/filename)
        if x>104857600:
            print(x)
            print(p/foldername/filename)
