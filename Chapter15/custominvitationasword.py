import docx
from docx import Document 
from collections import Sequence
from docx.parts.document import DocumentPart
from docx.section import Section, Sections

doc=docx.Document()
file=open('guests.txt')
n=file.readlines
print(n)
for i in n:
    doc.add_paragraph('It would be the pleasure to have the company of').QuoteChar=True
    doc.add_paragraph(i).bold=True
    doc.add_paragraph('at 11011 Memory Lane on the Evening of').italics=True
    doc.add_paragraph('April 1st').bold=True
    doc.add_paragraph('at 7 o\' clock').italics=True
    doc.add_page_break()
doc.save('custominv.docx')
#e