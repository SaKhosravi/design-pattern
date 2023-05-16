"""
imagen we have a flashlight that has three state:
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
from  abc import ABC,abstractmethod

class State(ABC):
    def __init__(self,context):
        self.context = context

    @abstractmethod
    def state_changed(self,label:QLabel):
        pass



class Context:
    current_state = None
    def __init__(self,label:QLabel):
        self.label = label

    def transition_to(self,state:State):
        self.current_state =state

    def state_changed(self):
        self.current_state.state_changed(label=self.label)

class ON(State):

    def state_changed(self,label:QLabel):
        label.setText("On")
        self.context.transition_to(state=LowLight(self.context))

class LowLight(State):

    def state_changed(self,label:QLabel):
        label.setText("Low")
        self.context.transition_to(state = Off(self.context))

class Off(State):
    def state_changed(self,label:QLabel):
        label.setText("Off")
        self.context.transition_to(state=ON(self.context))

class FlashLightWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.context = Context(label=self.label)
        off = Off(self.context)
        self.context.transition_to(off)
        self.context.state_changed()

    def initUI(self):
        self.resize(400,300)

        self.label = QLabel("No status", self)
        self.label.resize(100,20)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.move(150,50)
        self.label.setFont(QFont("Times", 10))

        self.button = QPushButton('Press Me',self)
        self.button.move(150,100)
        self.button.clicked.connect(self.pressed)

    def pressed(self):
        self.context.state_changed()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlashLightWindow()
    ex.show()
    sys.exit(app.exec_())