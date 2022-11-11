# dialog.py

"""Dialog-style application."""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout
)


# Create GUI inherits from QDialog, the base class of all dialog windows.
# Dialog window = standalone window used as main window for application
class Window(QDialog):
    def __init__(self):
        super().__init__(parent=None)  # No parent window since this dialog is main window
        self.setWindowTitle("PDF Combiner")
        dialogLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow("File 1:", QLineEdit())
        formLayout.addRow("File 2:", QLineEdit())
        dialogLayout.addLayout(formLayout)
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
        )
        dialogLayout.addWidget(buttons)
        self.setLayout(dialogLayout)


# Code block to execute only when run as script, not imported as module
if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())




