from pathlib import Path
import re
import shutil

shutil.copy(Path.home()/'ch9.txt',Path.home()/'ch9replaced.txt')
l=[]
ch9file=open(Path.home() / 'ch9.txt')
ch9filecontent=ch9file.read()
ch9file.close()
x=re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)')
l=x.findall(ch9filecontent) #putting all the matching ones in list
i=''
for i in l:
    word=input(f'enter a {i}')
    ch9filecontent=ch9filecontent.replace(i,word,1) #replace the match with the inputed value
#that 1 is to replace it once otherwise it will replace all instances
new=open('ch9replaced.txt','w')
new.write(ch9filecontent)
print(ch9filecontent)
new.close()
#the new file will be created in the current directory
