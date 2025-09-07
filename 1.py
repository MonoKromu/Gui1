import sys
from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton


class Flipper(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Flipper")
        self.setFixedSize(500, 200)
        self.field1 = QLineEdit(self)
        self.field1.setGeometry(50, 75, 100, 50)
        self.button = QPushButton("--->", self)
        self.button.setGeometry(200, 75, 100, 50)
        self.button.clicked.connect(self.flip)
        self.field2 = QLineEdit(self)
        self.field2.setGeometry(350, 75, 100, 50)

    def flip(self):
        if self.button.text() == "--->":
            self.button.setText("<---")
        else:
            self.button.setText("--->")
        texts = [self.field1.text(), self.field2.text()]
        self.field1.setText(texts[1])
        self.field2.setText(texts[0])

app = QApplication(sys.argv)
flipper = Flipper()
flipper.show()
app.exec()