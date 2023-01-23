import os
from pathlib import Path
import shutil

l=[]
p=Path.cwd()
for foldername,subfolders,filenames in os.walk(p):
    for filename in filenames:
        y=list(p.glob('*00*.txt'))
        if y not in l:
            l.append(y[])


l.sort()
print(l)
# for i in range(1,len(l)+1):
#     y=l[i]
#     j=y[-5]
#     if j!=i:
#         shutil.move(p/y,p/'spam00'+i)
