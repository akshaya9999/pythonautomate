import re


word=input("enter string")
hasc=re.compile(',')
g=hasc.findall(word)   #checking if a second parameter is defined or not
if g==[]:
    hasspace=re.compile('\S')   #returs just the non space values hence mimicking stripping
    x=hasspace.findall(word)
    y="".join(x)   #since findall returns list joining it to give string
    print(y)
 #to check if user has inputed a string to be stripped from the word

else:
    hascomma=re.compile(',\w*')
    c=hascomma.findall(word)
    z="".join(c)
    zz=z[1:]
    finn=re.search('^((.?!))*$'+zz+'^((.?!))*$')
    h=finn.findall(word)
    hh="".join(h)
    print(hh)