import sys

# import QApplication and all required widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])  # list parameter is for command line arguments

# GUI SETUP
window = QWidget()
window.setWindowTitle("PyQT App")
window.setGeometry(1000, 250, 280, 80)  # x pos, y pos, width, height
# File Dialog Widget


# DISPLAY GUI
window.show()

# Run application's event loop
sys.exit(app.exec())
