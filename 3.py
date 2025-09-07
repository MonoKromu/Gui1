import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel, QGridLayout, QCheckBox


class Boxes(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("CheckBoxes")
        self.setFixedSize(350, 400)
        layout = QGridLayout(self)

        self.label = QLabel("Custom Label")
        self.button = QPushButton("Useless Button")
        self.editor = QLineEdit("Enter your text")

        row = 1
        for widget in [self.label, self.button, self.editor]:
            checkbox = QCheckBox()
            checkbox.widget = widget
            checkbox.clicked.connect(self.onBoxClicked)
            checkbox.setChecked(True)
            layout.addWidget(checkbox, row, 1, Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(widget, row, 2, Qt.AlignmentFlag.AlignCenter)
            row += 1

        self.setLayout(layout)

    def onBoxClicked(self):
        sender = self.sender()
        if sender.isChecked():
            sender.widget.show()
        else:
            sender.widget.hide()

app = QApplication(sys.argv)
boxes = Boxes()
boxes.show()
app.exec()