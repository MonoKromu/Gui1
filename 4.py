import sys

from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QPlainTextEdit


class Morse(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Morse encoder")
        self.setFixedSize(600, 300)
        layout = QGridLayout(self)

        self.editor = QPlainTextEdit()
        layout.addWidget(self.editor, 0, 0, 1, 10)
        morse = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..'
        }
        qwerty = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
        for i, row in enumerate(qwerty):
            for j, char in enumerate(row):
                button = QPushButton(char)
                button.morse = morse.get(char)
                button.clicked.connect(self.printChar)
                layout.addWidget(button, i + 1, j)

        self.setLayout(layout)

    def printChar(self):
        self.editor.insertPlainText(self.sender().morse + " ")

app = QApplication(sys.argv)
morse = Morse()
morse.show()
app.exec()