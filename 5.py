import sys

from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QPlainTextEdit, QLabel


class Food:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Menu")
        self.setFixedSize(800, 300)
        layout = QGridLayout(self)

        self.editor = QPlainTextEdit()
        layout.addWidget(self.editor, 0, 3, 5, 1)
        self.food_items = [
            Food("Margherita Pizza", 12.50, 0),
            Food("Grilled Salmon with Vegetables", 22.00, 0),
            Food("Caesar Salad", 9.75, 0),
            Food("Beef Burger with Fries", 15.99, 0),
            Food("Chocolate Lava Cake", 7.50, 0)
        ]
        for i, food in enumerate(self.food_items):
            minus = QPushButton("-")
            minus.food = food
            minus.clicked.connect(self.changeFood)
            plus = QPushButton("+")
            plus.food = food
            plus.clicked.connect(self.changeFood)
            label = QLabel(f"{food.name} ${food.price}")
            layout.addWidget(minus, i, 0)
            layout.addWidget(plus, i, 1)
            layout.addWidget(label, i, 2)

        self.setLayout(layout)

    def changeFood(self):
        button = self.sender()
        if button.text() == "-":
            if button.food.quantity > 0:
                button.food.quantity -= 1
        else:
            button.food.quantity += 1
        self.updateCheck()

    def updateCheck(self):
        self.editor.setPlainText("")
        self.editor.appendPlainText("Check:")
        total_price = 0
        for food in self.food_items:
            if food.quantity != 0:
                self.editor.appendPlainText(f"{food.name} ({food.quantity}): {food.price * food.quantity}")
                total_price += food.quantity * food.price
        self.editor.appendPlainText(f"Total: {total_price}")


app = QApplication(sys.argv)
menu = Menu()
menu.show()
app.exec()