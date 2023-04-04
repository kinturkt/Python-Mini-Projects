from PyPDF2 import PdfMerger

pdfs = ['sample1.pdf','sample2.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

print("Your pdf files are merged now.")

merger.write("Merged_PDF.pdf")
merger.close()