#lettura file DOCX file di word dal 2007
#!pip install docx2txt

import docx2txt
my_text = docx2txt.process("c:\dati\doc1.docx")
print(my_text)