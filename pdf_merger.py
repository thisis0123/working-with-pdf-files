from PyPDF2 import PdfMerger

merger=PdfMerger()
pdfs=[r"C:\Users\DELL\Desktop\Lord of the mysteries 1\chapter1.pdf",r"C:\Users\DELL\Desktop\Lord of the mysteries 1\chapter2.pdf"]

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()