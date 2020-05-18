import PyPDF2


def merge_pdfs(path_pdf1, path_pdf2, path_merged):
    merger = PyPDF2.PdfFileMerger()

    merger.append(path_pdf1)
    merger.append(path_pdf2)

    merger.write(path_merged)

