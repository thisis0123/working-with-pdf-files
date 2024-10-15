from fpdf import FPDF

pdf=FPDF(unit="in")

pdf.add_page()
pdf.add_font("Arial_TTF","",r"C:\Windows\Fonts\Arial.ttf",uni=True)
pdf.set_font("Arial_TTF","",14)

pdf.multi_cell(w=6.27,h=0.25,txt="hello world")

pdf.output("this is new.pdf")