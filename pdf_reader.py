from PyPDF2 import PdfReader

reader=PdfReader(r"C:/Users/DELL/Desktop/Lord of the mysteries 1/chapter3.pdf")
file=open("new.txt","a")
for page in reader.pages:
    file.write(page.extract_text())
    file.write("\n")
file.close()