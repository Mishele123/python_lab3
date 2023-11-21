from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget



def on_clicked_button(main_windows: QWidget) -> str:
    folderpath = QtWidgets.QFileDialog.getExistingDirectory(main_windows, "Выберите папку")
    print(f"Вы выбрали: {folderpath}")

    return folderpath