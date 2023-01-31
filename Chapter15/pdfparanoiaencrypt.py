import os
from pathlib import Path
import PyPDF2

n=[]
p=Path.cwd()
for foldername,subfolders,filenames in os.walk(p):
    for filename in filenames:
        if filename.endswith('.pdf') :
            n.append(filename)

for i in n:
    pdffile=open(i,'rb')
    pdfreader=PyPDF2.PdfFileReader(pdffile)
    pdfwriter=PyPDF2.PdfFileWriter()
    for pagenum in range(pdfreader.numPages):
        pdfwriter.addPage(pdfreader.getPage(pagenum))

    pdfwriter.encrypt('paranoia')
    resultpdf=open('encryptedparanoia.pdf','wb')
    pdfwriter.write(resultpdf)
    resultpdf.close()

#trying to read the file to see if it is encrypted
    pdfread=PyPDF2.PdfFileReader(open('encryptedparanoia.pdf','rb'))
    
    


