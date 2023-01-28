import openpyxl
from pathlib import Path
import os

n=[]
p=Path.cwd()
for foldername,subfolders,filenames in os.walk(p):
    for filename in filenames:
        if filename.endswith('.txt') and filename!='ch9replaced.txt':
            n.append(filename)
print(n)
wb=openpyxl.Workbook()
sheet=wb.active
l=len(n)
for i in range(l):
    currentfile=open(n[i])
    text=currentfile.readlines()
    x=len(text)
    for j in range (x):
        sheet.cell(row=j+1,column=i+1).value=str(text[j])
    currentfile.close()
wb.save('texttospreadsheet.xlsx')