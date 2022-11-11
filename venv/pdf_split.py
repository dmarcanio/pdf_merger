from PyPDF4 import PdfFileReader, PdfFileWriter

in_file = 'Pipeline Referencing Vocabulary.pdf'

def split(path, name_of_split):
    pdf = PdfFileReader(path, strict=False)  #strict False disables superfluous warnings
    # for each page in input pdf
    for page in range(pdf.getNumPages()):
        # create new pdf writer for individual page
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        # write output page as individual pdf file
        output = f'{name_of_split}{page+1}.pdf'
        print(f"Writing page {page+1} of {pdf.getNumPages()}...")
        with open(output, 'wb') as output_pdf:  # wb = write bytes mode
            pdf_writer.write(output_pdf)
    print(f"PDF successfully split into {pdf.getNumPages()} pages.")

# Code block to execute only when run as script, not imported as module
if __name__ == '__main__':
    split(in_file, 'split_page')
