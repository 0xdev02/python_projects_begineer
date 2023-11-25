#pip install opencv-python

from pypdf import PdfWriter 

merger = PdfWriter()
pdfiles = ["1.pdf", "2.pdf"]

for pdf in pdfiles:
  merger.append(pdf)
  

merger.write("Merged.pdf")
merger.close()
print(f'sucessfully merged {pdfiles} check "Merged.pdf"')
