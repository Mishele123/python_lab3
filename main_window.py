from handler import *

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.resize(300, 100)
        self.setUi()
        self.select_folder: str
        
    def create_label2(self) -> QLabel:
        textbox1 = QLabel("Путь к файлу назначения:")
        return textbox1

    def create_label3(self) -> QLabel:
        textbox1 = QLabel("Путь к папке назначения:")
        return textbox1

    def create_button(self) -> QPushButton:
        button = QPushButton("Путь к датасету")

        button.setCheckable(True)
        self.select_folder = button.clicked.connect(lambda: on_clicked_button(self))

        return button

    def create_button1(self) -> QPushButton:
        button = QPushButton("Создать файл аннотацию исходного датасета")
        return button
    
    def create_button2(self) -> QPushButton:
        button = QPushButton("создания датасета с другой организацией файлов ")
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
        layout.addWidget(self.create_label2())
        layout.addWidget(self.create_button1())
        layout.addWidget(QLabel("Задание 2"))
        layout.addWidget(self.create_label3())
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