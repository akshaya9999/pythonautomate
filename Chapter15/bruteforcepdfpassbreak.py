import PyPDF2

pdfreader=PyPDF2.PdfFileReader(open('encryptedparanoia.pdf','rb'))
file=open('dictionary.txt')
l=[]
f=0
l=file.readlines()
for i in l:
    j=i[:-1]   #to remove \n from the i
    x=pdfreader.decrypt(j)
    y=pdfreader.decrypt(j.lower())
    if x==1 or y==1:
        print("password is",j)
        f=1
        break
    else:
        continue
if f==0:
    print("password not found")

