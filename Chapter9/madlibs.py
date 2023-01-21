from pathlib import Path
import re


ch9file=open(Path.home() / 'ch9.txt')
ch9filecontent=ch9file.read()
x=re.compile(r'[ADJECTIVE]')
Y=re.search

