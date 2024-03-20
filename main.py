# import the necessary modules
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from style_sheet import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(700, 700)
        self.setWindowTitle("Food Order GUI")

        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(style)
    window = MainWindow()
    sys.exit(app.exec())