# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\select_color.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form, is_resetup=True):
        if is_resetup:
            Form.setObjectName("Form_page2")
            Form.resize(835, 591)
        self.widget_page2 = QtWidgets.QWidget(Form)
        self.widget_page2.setGeometry(QtCore.QRect(0, 0, 841, 591))
        self.widget_page2.setStyleSheet("background-color: #22222e\n"
"")
        self.widget_page2.setObjectName("widget_page2")
        self.pushButton_page2 = QtWidgets.QPushButton(self.widget_page2)
        self.pushButton_page2.setGeometry(QtCore.QRect(280, 480, 291, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(11)
        self.pushButton_page2.setFont(font)
        self.pushButton_page2.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #fb5b5d;\n"
"    border-radius: 30\n"
"}")
        self.pushButton_page2.setObjectName("pushButton_page2")
        self.frame_page2 = QtWidgets.QFrame(self.widget_page2)
        self.frame_page2.setGeometry(QtCore.QRect(0, -1, 841, 81))
        self.frame_page2.setStyleSheet("background-color: #fb5b5d;")
        self.frame_page2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_page2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_page2.setObjectName("frame_page2")
        self.label_page2 = QtWidgets.QLabel(self.frame_page2)
        self.label_page2.setGeometry(QtCore.QRect(0, 7, 841, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_page2.setFont(font)
        self.label_page2.setStyleSheet("color: white\n"
"")
        self.label_page2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_page2.setObjectName("label_page2")
        self.label_5_page2 = QtWidgets.QLabel(self.widget_page2)
        self.label_5_page2.setGeometry(QtCore.QRect(280, 550, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(9)
        self.label_5_page2.setFont(font)
        self.label_5_page2.setStyleSheet("color: #fb5b5d;")
        self.label_5_page2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5_page2.setObjectName("label_5_page2")
        self.frame_2_page2 = QtWidgets.QFrame(self.widget_page2)
        self.frame_2_page2.setGeometry(QtCore.QRect(220, 230, 411, 101))
        self.frame_2_page2.setStyleSheet("    color: white;\n"
"    border: 2px solid #fb5b5d;\n"
"    border-radius: 30")
        self.frame_2_page2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2_page2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2_page2.setObjectName("frame_2_page2")
        self.checkBox_page2 = QtWidgets.QCheckBox(self.frame_2_page2)
        self.checkBox_page2.setGeometry(QtCore.QRect(150, 20, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(12)
        self.checkBox_page2.setFont(font)
        self.checkBox_page2.setStyleSheet("color:white;\n"
"border: 0px;")
        self.checkBox_page2.setObjectName("checkBox_page2")
        self.label_2_page2 = QtWidgets.QLabel(self.frame_2_page2)
        self.label_2_page2.setGeometry(QtCore.QRect(40, 20, 61, 61))
        self.label_2_page2.setStyleSheet("border: 2px solid #fb5b5d;\n"
"border-radius: 0;")
        self.label_2_page2.setText("")
        self.label_2_page2.setPixmap(QtGui.QPixmap(".\\color_palitres/2 (1).png"))
        self.label_2_page2.setScaledContents(True)
        self.label_2_page2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2_page2.setObjectName("label_2_page2")
        self.frame_3_page2 = QtWidgets.QFrame(self.widget_page2)
        self.frame_3_page2.setGeometry(QtCore.QRect(220, 110, 411, 101))
        self.frame_3_page2.setStyleSheet("    color: white;\n"
"    border: 2px solid #fb5b5d;\n"
"    border-radius: 30")
        self.frame_3_page2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3_page2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3_page2.setObjectName("frame_3_page2")
        self.checkBox_2_page2 = QtWidgets.QCheckBox(self.frame_3_page2)
        self.checkBox_2_page2.setGeometry(QtCore.QRect(150, 20, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(12)
        self.checkBox_2_page2.setFont(font)
        self.checkBox_2_page2.setStyleSheet("color:white;\n"
"border: 0px;")
        self.checkBox_2_page2.setObjectName("checkBox_2_page2")
        self.label_3_page2 = QtWidgets.QLabel(self.frame_3_page2)
        self.label_3_page2.setGeometry(QtCore.QRect(40, 20, 61, 61))
        self.label_3_page2.setStyleSheet("border: 2px solid #fb5b5d;\n"
"border-radius: 0;")
        self.label_3_page2.setText("")
        self.label_3_page2.setPixmap(QtGui.QPixmap(".\\color_palitres/1 (3).png"))
        self.label_3_page2.setScaledContents(True)
        self.label_3_page2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3_page2.setObjectName("label_3_page2")
        self.frame_4_page2 = QtWidgets.QFrame(self.widget_page2)
        self.frame_4_page2.setGeometry(QtCore.QRect(220, 350, 411, 101))
        self.frame_4_page2.setStyleSheet("    color: white;\n"
"    border: 2px solid #fb5b5d;\n"
"    border-radius: 30")
        self.frame_4_page2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4_page2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4_page2.setObjectName("frame_4_page2")
        self.checkBox_4_page2 = QtWidgets.QCheckBox(self.frame_4_page2)
        self.checkBox_4_page2.setGeometry(QtCore.QRect(150, 20, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(12)
        self.checkBox_4_page2.setFont(font)
        self.checkBox_4_page2.setStyleSheet("color:white;\n"
"border: 0px;")
        self.checkBox_4_page2.setObjectName("checkBox_4_page2")
        self.label_6_page2 = QtWidgets.QLabel(self.frame_4_page2)
        self.label_6_page2.setGeometry(QtCore.QRect(40, 20, 61, 61))
        self.label_6_page2.setStyleSheet("border: 2px solid #fb5b5d;\n"
"border-radius: 0;")
        self.label_6_page2.setText("")
        self.label_6_page2.setPixmap(QtGui.QPixmap(".\\color_palitres/3 (1).png"))
        self.label_6_page2.setScaledContents(True)
        self.label_6_page2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6_page2.setObjectName("label_6_page2")
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_page2.setText(_translate("Form", "Далее"))
        self.label_page2.setText(_translate("Form", "Ваши цветовые предпочтения"))
        self.label_5_page2.setText(_translate("Form", "Неверно указаны желания"))
        self.checkBox_page2.setText(_translate("Form", "Теплые тона"))
        self.checkBox_2_page2.setText(_translate("Form", "Холодные тона"))
        self.checkBox_4_page2.setText(_translate("Form", "Кислотные тона"))
        QtCore.QMetaObject.connectSlotsByName(Form)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())