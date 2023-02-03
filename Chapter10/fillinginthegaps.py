import os
from pathlib import Path
import shutil
import re

isfile=re.compile(r'\d\d\d*')
l=[]
p=Path.cwd()
for foldername,subfolders,filenames in os.walk(p):
    for filename in filenames:
        if filename.endswith('.txt') and isfile.findall(filename)!=[]:
            l.append(filename)


l.sort()
print(l)
starting=re.compile(r'[1-9]')
startt=starting.findall(l[0])
start="".join(startt)
# print(start)

# print(int(start)+len(l)-1)
for i in range(int(start),int(start)+len(l)-1):
    namee=starting.findall(l[i])
    name="".join(namee)
    # print(name,",",i)
    
    if i==int(start):
        continue
    elif int(name)==i+1:
        continue
    else:
        shutil.move(p/f'spam00{name}.txt',p/f'spam00{i+1}.txt')
print(l)

    

# for i in range(1,len(l)+1):
#     y=l[i]
#     j=y[-5]
#     if j!=i:
#         shutil.move(p/y,p/'spam00'+i)
