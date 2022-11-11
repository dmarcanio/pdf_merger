from PyPDF4 import PdfFileReader, PdfFileWriter

file1 = r"C:\Users\DominicMarcanio\OneDrive - we-do-IT, Inc\Documents\Expenses\Filed\Marcanio Amazon Mouse and Headset.pdf"
file2 = r"C:\Users\DominicMarcanio\OneDrive - we-do-IT, Inc\Documents\Expenses\Filed\Marcanio TSA PreCheck Receipt 20221006.pdf"
out_file_name = r"C:\Users\DominicMarcanio\OneDrive - we-do-IT, Inc\Documents\Expenses\Filed\merged.pdf"

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path, strict=False)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

        # Write out merged PDF
        with open(output, 'wb') as out:  # wb mode to write bytes
            pdf_writer.write(out)
        print("Merge completed successfully.")

# Code block to execute only when run as script, not imported as module
if __name__ == '__main__':
    paths = [file1, file2]
    merge_pdfs(paths, output=out_file_name)