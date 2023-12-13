# python -m pip install PyPDF2 

from PyPDF2 import PdfReader
file = PdfReader("D:\\Corso ITS IIOT\\2 anno\AI Python\AI-Python\\4 lezione 13_12_2023\Codice\Macchine Learning\\Dati per es\\doc1.pdf")
number_of_pages = len(file.pages)
print(number_of_pages)
page = file.pages[0]
text = page.extract_text()
print(text)