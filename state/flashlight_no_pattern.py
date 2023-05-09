"""
imagen we have an flashlight that has three state:
    -on
    -low light mode
    -off

we create a simple ui that contain a one button
and with press the button, the state of flashlight must be changed:
    - from off to on
    - from on to low light mode
    - from low light mode to off
"""
import sys

from PyQt5.QtCore import Qt
import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class FlashLightWindow(QWidget):
    status = "off"
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(400,300)

        self.label = QLabel(self.status, self)
        self.label.resize(100,20)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.move(150,50)
        self.label.setFont(QFont("Times", 10))

        self.button = QPushButton('Press Me',self)
        self.button.move(150,100)
        self.button.clicked.connect(self.pressed)

    def pressed(self):
        print(self.status)
        if self.status == "off":
            self.status = "on"

        elif self.status == "on":
            self.status = "low_light"

        elif self.status == "low_light":
            self.status = "off"

        self.label.setText(self.status)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlashLightWindow()
    ex.show()
    sys.exit(app.exec_())