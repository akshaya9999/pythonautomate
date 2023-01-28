import os
from pathlib import Path

n=[]
p=Path.cwd()
for foldername,subfolders,filenames in os.walk(p):
    for filename in filenames:
        if filename.endswith('.pdf') :
            n.append(filename)

