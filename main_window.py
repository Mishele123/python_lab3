import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
import sys

from PyQt6.QtWidgets import QWidget


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setUi()


    def create_textbox1(self) -> QLabel:
        textbox1 = QLabel("Введите путь к папке исходного датасета:")
        return textbox1


    def setUi(self) -> None:
        layout = QVBoxLayout()
        
        layout.addWidget(self.create_textbox1())

        self.setLayout(layout)

# def main() -> None:
#     app = QApplication([])
#     window = QWidget()

#     layout = QVBoxLayout()

#     label = QLabel("запрашивать у пользователя путь к папке исходного датасета")
#     textbox = QTextEdit()
#     textbox.setFixedHeight(27)
#     button = QPushButton("Press me!")
#     textbox2 = QTextEdit()

#     button.clicked.connect(lambda: on_clicked(textbox.toPlainText()))

#     layout.addWidget(label)    
#     layout.addWidget(textbox)    
#     layout.addWidget(button)    
#     layout.addWidget(textbox2)    

#     window.setLayout(layout)

#     window.show()
#     app.exec()

# def on_clicked(msg):
#     print(msg)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()

    window.show()
    app.exec()