from pypdf import PdfWriter

merger = PdfWriter()

pdfs = []

n = int(input("How Many Pdfs do you want to merge?\n"))

for i in range(0, n):
    inp = input(f"Enter The Name Of Pdf {i + 1}: ")
    pdfs.append(inp)
print(pdfs)
for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()