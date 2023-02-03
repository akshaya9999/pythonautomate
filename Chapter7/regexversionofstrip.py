import re


word=input("enter string")
toremove=input("enter the string to remove")
asspace=re.compile('\S')

def strip(word,toremove):
    if len(toremove)==0:
        hasspace=re.compile('\S')        #returs just the non space values hence mimicking stripping
        x=hasspace.findall(word)
        y="".join(x)         #since findall returns list joining it to give string
        print(y)


    else:
        hascomma=re.compile(f'^{toremove}*|{toremove}*$')
        c=hascomma.sub("",word)
        print(c)
    
strip(word,toremove)