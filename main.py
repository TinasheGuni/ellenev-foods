# import the necessary modules
import random
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget,
                             QLabel, QRadioButton)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle("Guessing Game")
        self.setWindowIcon(QIcon("resources/pyqt_logo.png"))

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        lbl_instruction = QLabel("<b>Guess the fruit</b>")

        # choice
        rbtn_apple = QRadioButton("Apple")
        rbtn_pineapple = QRadioButton("Pineapple")
        rbtn_watermelon = QRadioButton("Watermelon")
        rbtn_banana = QRadioButton("Banana")

        lbl_info = QLabel("Click the pushbutton to select an icon")

        self.images = [
            "resources/1_apple.png",
            "resources/2_pineapple.png",
            "resources/3_watermelon.png",
            "resources/4_banana.png",
        ]

        self.btn_icon = QPushButton()
        self.btn_icon.setIconSize(QSize(60, 60))
        self.btn_icon.setIcon(QIcon(random.choice(self.images)))
        self.btn_icon.clicked.connect(self.changeIcon)

        lyt_main = QVBoxLayout()
        lyt_main.addWidget(lbl_instruction)

        lyt_main.addWidget(rbtn_apple)
        lyt_main.addWidget(rbtn_pineapple)
        lyt_main.addWidget(rbtn_watermelon)
        lyt_main.addWidget(rbtn_banana)

        lyt_main.addWidget(lbl_info)
        lyt_main.addWidget(self.btn_icon)

        container = QWidget()
        container.setLayout(lyt_main)

        self.setCentralWidget(container)

    def changeIcon(self):
        self.btn_icon.setIcon(QIcon(random.choice(self.images)))

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())