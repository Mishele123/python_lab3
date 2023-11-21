from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget

import os
import csv

def create_dataset(select_folder: str, new_folder_path: str) -> None:
    print("Создание файла аннотации исходного датасета")
    annotation_file = "annotation.csv"

    print(select_folder)
    print(new_folder_path)

    annotation_file = "annotation.csv"

    print(new_folder_path + "/" + annotation_file)

    with open(new_folder_path + "/" + annotation_file, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)

        for folder in os.listdir(select_folder):
            if folder != "tiger" or folder != "leopard":
                print("Не правильная папка")
                return None

            path_folder = os.path.join(select_folder, folder)

            for img in os.listdir(path_folder):
                img_path = os.path.join(path_folder, img)

                # Абсолютный путь
                absolute_path = os.path.abspath(img_path)

                # Относительный путь
                relative_path = os.path.relpath(img_path, select_folder)

                csv_writer.writerow([absolute_path, relative_path, folder])

    print("Файл создался")

def on_clicked_button(main_windows: QWidget) -> str:
    folderpath = QtWidgets.QFileDialog.getExistingDirectory(main_windows, "Выберите папку")
    print(f"Вы выбрали: {folderpath}")
    return folderpath
    

def on_clicked_button_for_make_dataset(main_windows: QWidget, select_folder: str) -> None:
    print(select_folder)
    folderpath = QtWidgets.QFileDialog.getExistingDirectory(main_windows, "Выберите папку")
    print(f"Вы выбрали: {folderpath}")
    
    create_dataset(select_folder, folderpath)