import random
import traceback

from PyQt5 import QtCore, QtGui, QtWidgets

import anketa
from start_n import Ui_mainWindow as start_window
from anketa import Ui_Form as anketa_window
from selecting_color import Ui_Form as colors_window
from paint import Ui_Form as paint_window

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


class Program(start_window):
    def __init__(self):
        self.page_now = "start"

    def check_page1_correct(self):
        fio = self.lineEdit_page1.text()
        birthday = self.dateEdit_page1.text()
        gender_fields = [self.checkBox_page1, self.checkBox_2_page1, self.checkBox_3_page1]
        if fio != "Раз два три" and len(fio.split()) == 3 and \
                len(list(filter(lambda symbol: symbol.lower() not in alphabet + " ", fio))) == 0:
            pass
        else:
            return False, "Неверно указаны желания"
        if len(list(filter(lambda a: a.isChecked(), gender_fields))) != 0:
            pass
        else:
            return False, "Не указан пол"
        return True, ""

    def check_page2_correct(self):
        colors_fields = [self.checkBox_page2, self.checkBox_2_page2, self.checkBox_4_page2]
        if len(list(filter(lambda a: a.isChecked(), colors_fields))) != 0:
            pass
        else:
            return False, "Не указано предпочтение"
        return True, ""

    def next_page(self):
        if self.page_now == "start":
            self.widget.hide()
            self.widget_page1.show()
            self.page_now = "anketa"

        elif self.page_now == "anketa":
            status, info = self.check_page1_correct()
            if status:
                self.widget_page1.hide()
                self.widget_page2.show()
                self.page_now = "colors"
            else:
                self.label_5_page1.setText(info)

        elif self.page_now == "colors":
            status, info = self.check_page2_correct()
            if status:
                try:
                    self.paint_window = paint_window()
                    self.setup_paint_window()
                    self.paint_window.show()
                    self.MainWindow.hide()
                except:
                    print(traceback.format_exc())
            else:
                self.label_5_page3.setText(info)


    def get_user_data(self):
        gender_fields = [self.checkBox_page1, self.checkBox_2_page1, self.checkBox_3_page1]
        colors_fields = [self.checkBox_page2, self.checkBox_2_page2, self.checkBox_4_page2]
        data = {
            'gender': list(filter(lambda a: a.isChecked(), gender_fields))[0],
            'color': list(filter(lambda a: a.isChecked(), colors_fields))[0],
            'fio': self.lineEdit_page1.text(),
            'birthday': self.dateEdit_page1.text(),
        }
        return data


    def setup_paint_window(self):
        cold_colors = ["#000323", "#020F9C", "#0522FC", "#5062FB", "#A4B0FC", "#CFD7FC"]
        chemic_colors = ["#CC00AF", "#7308A5", "#FF0001", "#FF4600", "#FF7D00", "#FFFF00"]
        hot_colors = ["#F5AEFA", "#7BB0F7", "#7BB0F7", "#FEB686", "#ED145B", "#F76DD7"]

        colors_labels = [self.paint_window.pushButton, self.paint_window.pushButton_2, self.paint_window.pushButton_3,
                         self.paint_window.pushButton_4, self.paint_window.pushButton_5, self.paint_window.pushButton_6]

        user = self.get_user_data()
        self.paint_window.label.setText(user['fio'])
        self.paint_window.label_2.setText(user['fio'])
        pen_width = str(int(user['birthday'].split(".")[0])+int(user['birthday'].split(".")[1]))
        self.paint_window.lineEdit.setText(pen_width)
        self.paint_window.canvas.set_pen_width(int(pen_width))
        if user['gender'].text() == "Мужской":
            self.paint_window.canvas.set_pen_style("pen")
            self.paint_window.pushButton_8.setText("Ручка")
        elif user['gender'].text() == "Женский":
            self.paint_window.canvas.set_pen_style("pencil")
            self.paint_window.pushButton_8.setText("Карандаш")
        elif user['gender'].text() == "Не важно":
            self.paint_window.canvas.set_pen_style("marker")
            self.paint_window.pushButton_8.setText("Фломастер")
        if user['color'].text() == "Холодные тона":
            for i, color, label in zip(range(1, 7), cold_colors, colors_labels):
                label.setStyleSheet(f"background-color: {color};\n"
                                     "border: 0px;")
                label.clicked.connect(self.paint_window.__getattribute__(f"set_color{i}"))
        elif user['color'].text() == "Теплые тона":
            for i, color, label in zip(range(1, 7), hot_colors, colors_labels):
                label.setStyleSheet(f"background-color: {color};\n"
                                    "border: 0px;")
                label.clicked.connect(self.paint_window.__getattribute__(f"set_color{i}"))
        elif user['color'].text() == "Кислотные тона":
            for i, color, label in zip(range(1, 7), chemic_colors, colors_labels):
                label.setStyleSheet(f"background-color: {color};\n"
                                    "border: 0px;")
                label.clicked.connect(self.paint_window.__getattribute__(f"set_color{i}"))

    def setup(self, mainWindow):
        self.MainWindow = mainWindow
        anketa_window.setupUi(self, mainWindow, is_resetup=False)
        self.widget_page1.hide()
        colors_window.setupUi(self, mainWindow, is_resetup=False)
        self.widget_page2.hide()
        self.pushButton.clicked.connect(self.next_page)
        self.pushButton_page1.clicked.connect(self.next_page)
        self.pushButton_page2.clicked.connect(self.next_page)

        self.label_5_page1.setText("")
        self.label_5_page2.setText("")

        gender_fields = [self.checkBox_page1, self.checkBox_2_page1, self.checkBox_3_page1]
        colors_fields = [self.checkBox_page2, self.checkBox_2_page2, self.checkBox_4_page2]

        self.gender_group = QtWidgets.QButtonGroup()
        self.colors_group = QtWidgets.QButtonGroup()

        self.gender_group.setExclusive(True)
        self.colors_group.setExclusive(True)

        [self.gender_group.addButton(field) for field in gender_fields]
        [self.colors_group.addButton(field) for field in colors_fields]


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Program()

    ui.setupUi(MainWindow)
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
