from PyPDF2 import PdfReader
file = PdfReader("C:\dati\doc1.pdf")
number_of_pages = len(file.pages)
print(number_of_pages)
page = file.pages[0]
text = page.extract_text()
print(text)