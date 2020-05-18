import PyPDF2
from utilities import merger

# with open('./assets/dummy.pdf', 'rb') as file:  # 'rb' to read binary files.
    # reader = PyPDF2.PdfFileReader(file)
    # print(f'Number of pages: { reader.numPages }')

    # page0 = reader.getPage(0)
    # print(f'Page 1:\n { page0 }')

    # Rotate page 0 and save it in a new file.
    # writer = PyPDF2.PdfFileWriter()
    # with open('outputs/tilt.pdf', 'wb') as crooked_file:
    #    writer.addPage(page0.rotateCounterClockwise(90))
    #    writer.write(crooked_file)

# Merge files.
merger.merge_pdfs('./assets/dummy.pdf', './assets/twopage.pdf', 'outputs/merged.pdf')

# Watermark the pages of the merged pdf.
output = PyPDF2.PdfFileWriter()

watermark_reader = PyPDF2.PdfFileReader(open('./assets/wtr.pdf', 'rb'))
template = PyPDF2.PdfFileReader(open('./outputs/merged.pdf', 'rb'))

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark_reader.getPage(0))
    output.addPage(page)

with open('./outputs/watermarked.pdf', 'wb') as watermarked_pdf:
    output.write(watermarked_pdf)
