from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog, QDialog
from PyPDF4 import PdfFileReader, PdfFileWriter
from PyQt6 import uic
import sys

default_directory = r"C:\Users\DominicMarcanio\OneDrive - we-do-IT, Inc\Documents"


# Class to create QT window and import UI designed in QT designer.exe
class UI(QDialog):
    def __init__(self):
        super(UI, self).__init__()

        # Self attributes for file 1, file 2, output directory
        self.files = []        # list of PDF files to pass into merge function later
        self.output_file = ""  # output PDF file

        # Load the UI file from QT designer
        uic.loadUi("MergePDF_UI_Designer.ui", self)  # file must be located in venv directory

        # Define widgets. findChild strings must match widget names assigned in Qt Designer
        self.file1button = self.findChild(QPushButton, "file1button")  # file 1 selector button
        self.file1label = self.findChild(QLabel, "file1label")         # file 1 label
        self.file2button = self.findChild(QPushButton, "file2button")  # file 2 selector button
        self.file2label = self.findChild(QLabel, "file2label")         # file 2 label
        self.merge_button = self.findChild(QPushButton, "merge_button")
        self.out_dir_button = self.findChild(QPushButton, "out_dir_button")
        self.out_dir_label = self.findChild(QLabel, "out_dir_label")
        self.completed_label = self.findChild(QLabel, "completed_label")
        self.completed_label.setHidden(True)

        # Call functions on button click. One function per button in this program.
        # Could be refined via function factories later

        self.file1button.clicked.connect(self.clicker1)  # clicker function called on button press
        self.file2button.clicked.connect(self.clicker2)
        self.out_dir_button.clicked.connect(self.out_directory)
        self.merge_button.clicked.connect(lambda: self.merge_pdfs(self.files, self.output_file))

        # Show the app
        self.show()

    def clicker1(self):
        """Display file name when button is pressed. """
        # self, "Title Bar of Dialog Box", "default path to show", "types of files to filter";"other types to filter
        # returns tuple with file name, type of file
        fname = QFileDialog.getOpenFileName(self, "Open File", default_directory, "PDF Files (*.pdf)")
        file1only = str(fname[0])  # Grab first item of tuple and convert to string.
        # Output file name to screen as label.
        if fname:  # only show fname if file was selected (show null if dialog was cancelled.)
            self.file1label.setText(file1only)  # 0th item from tuple = file name only
            self.files.append(file1only)

    def clicker2(self):
        """Select 2nd file and display file name on label """
        fname2 = QFileDialog.getOpenFileName(self, "Open File", default_directory, "PDF Files (*.pdf)")
        file2only = str(fname2[0])  # Grab first item of tuple and convert to string
        if fname2:
            self.file2label.setText(file2only)
            self.files.append(file2only)

    def out_directory(self):
        """ On button press, user select output directory and new file name.
            File does not have to exist.
            """
        path_var = QFileDialog.getSaveFileName(self, "Select Directory", default_directory, "PDF Files (*.pdf)")
        file_only = str(path_var[0])  # Grab first item of tuple and return string
        self.out_dir_label.setText(file_only)
        self.output_file = file_only  # convert string to raw string for file path
        return file_only

    def merge_pdfs(self, pdf_list, out_dir):
        """ Merge two user-selected PDF files into one user-selected output file
            :param pdf_list: list of paths to two PDF files to merge
            :param out_dir: output directory and file name
            """
        pdf_writer = PdfFileWriter()

        for doc in pdf_list:
            pdf_reader = PdfFileReader(doc, strict=False)
            for page in range(pdf_reader.getNumPages()):
                # Add each page to writer object
                pdf_writer.addPage(pdf_reader.getPage(page))

            # Write out merged PDF
            with open(out_dir, 'wb') as out:  # wb mode to write bytes
                pdf_writer.write(out)

            # Show Completed label.
            self.completed_label.setHidden(False)


# Initialize the app
# Code block to execute only when run as script, not imported as module
if __name__ == '__main__':
    app = QApplication(sys.argv)
    UIWindow = UI()
    sys.exit(app.exec())

