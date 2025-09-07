import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QBoxLayout, QLabel


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 150)
        layout = QBoxLayout(QBoxLayout.Direction.TopToBottom, self)

        self.exp = QLineEdit()
        self.res = QLabel()
        self.res.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn = QPushButton("Calculate")
        self.btn.clicked.connect(self.calculate)
        for widget in [self.exp, self.res, self.btn]:
            widget.setMinimumHeight(40)
            layout.addWidget(widget)

    def calculate(self):
        self.res.setText(str(eval(self.exp.text())))

app = QApplication(sys.argv)
calculator = Calculator()
calculator.show()
app.exec()