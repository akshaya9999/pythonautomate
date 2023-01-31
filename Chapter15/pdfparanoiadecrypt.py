import os
from pathlib import Path
import PyPDF2

n=[]
p=Path.cwd()
for foldername,subfolders,filenames in os.walk(p):
    for filename in filenames:
        if filename.endswith('.pdf'):
            pdfReader = PyPDF2.PdfFileReader(open(filename, 'rb'))
            if pdfReader.isEncrypted==True:
                n.append(filename)
        
for i in n:
    passs=input("enter password")
    a=pdfReader.decrypt(passs)
    if a!=1:
        print("password is incorrect")
    