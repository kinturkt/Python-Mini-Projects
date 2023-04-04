from fpdf import FPDF

make_pdf=FPDF()
make_pdf.add_page()
make_pdf.set_font("Arial",size=20)
make_pdf.cell(200,10,txt="Hello")
make_pdf.cell(200,10,txt="My name is Kintur.")
make_pdf.cell(200,10,txt="I'm studying in 4th year computer engineering")
make_pdf.output("new.pdf")


import PyPDF2
pdf = open("Sample1.pdf", "rb")
reader = PyPDF2.PdfFileReader(pdf)
page = reader.getPage(0)
print(page.extractText())