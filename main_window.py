from handler import *

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.resize(300, 100)
        self.setUi()
        self.select_folder = ""

    def create_button(self) -> QPushButton:
        button = QPushButton("Путь к датасету")

        self.select_folder = button.clicked.connect(lambda: on_clicked_button(self))
        return button

    def create_button1(self) -> QPushButton:
        button = QPushButton("Создать файл аннотацию исходного датасета")
        button.clicked.connect(lambda: create_dataset(self.select_folder, on_clicked_button(self)))
        return button
    
    def create_button2(self) -> QPushButton:
        button = QPushButton("создания датасета с другой организацией файлов ")
        button.clicked.connect(lambda: create_dataset(self.select_folder, on_clicked_button(self)))
        return button

    def create_button3(self) -> QPushButton:
        button = QPushButton("Следующая картинка tiger")
        return button

    def create_button4(self) -> QPushButton:
        button = QPushButton("Следующая картинка leopard")
        return button
    

    def setUi(self) -> None:
        layout = QVBoxLayout()
        button = self.create_button()
        layout.addWidget(button)
        layout.addWidget(QLabel("Задание 1"))
        layout.addWidget(self.create_button1())
        layout.addWidget(QLabel("Задание 2"))
        layout.addWidget(self.create_button2())
        layout.addWidget(QLabel("Задание 3"))
        layout.addWidget(self.create_button3())
        layout.addWidget(self.create_button4())
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