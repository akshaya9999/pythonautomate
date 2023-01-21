from pathlib import Path
import re
p=Path.home()
l=list(p.glob('*.txt'))
i=input("enter the regex expression")

for j in range (len(l)):
    infile=l[j].read_text()
    r=re.compile(i)
    x=r.findall(infile)
    print(x)
