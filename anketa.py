# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\anketa.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form, is_resetup=True):
        if is_resetup:
                Form.setObjectName("Form_page1")
                Form.resize(835, 591)

        self.widget_page1 = QtWidgets.QWidget(Form)
        self.widget_page1.setGeometry(QtCore.QRect(0, 0, 841, 591))
        self.widget_page1.setStyleSheet("background-color: #22222e\n"
"")
        self.widget_page1.setObjectName("widget_page1")
        self.pushButton_page1 = QtWidgets.QPushButton(self.widget_page1)
        self.pushButton_page1.setGeometry(QtCore.QRect(280, 480, 291, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(11)
        self.pushButton_page1.setFont(font)
        self.pushButton_page1.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #fb5b5d;\n"
"    border-radius: 30\n"
"}")
        self.pushButton_page1.setObjectName("pushButton_page1")
        self.frame_page1 = QtWidgets.QFrame(self.widget_page1)
        self.frame_page1.setGeometry(QtCore.QRect(0, -1, 841, 81))
        self.frame_page1.setStyleSheet("background-color: #fb5b5d;")
        self.frame_page1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_page1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_page1.setObjectName("frame_page1")
        self.label_page1 = QtWidgets.QLabel(self.frame_page1)
        self.label_page1.setGeometry(QtCore.QRect(0, 7, 841, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_page1.setFont(font)
        self.label_page1.setStyleSheet("color: white\n"
"")
        self.label_page1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_page1.setObjectName("label_page1")
        self.label_2_page1 = QtWidgets.QLabel(self.widget_page1)
        self.label_2_page1.setGeometry(QtCore.QRect(130, 130, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(12)
        self.label_2_page1.setFont(font)
        self.label_2_page1.setStyleSheet("color: white\n"
"")
        self.label_2_page1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2_page1.setObjectName("label_2_page1")
        self.lineEdit_page1 = QtWidgets.QLineEdit(self.widget_page1)
        self.lineEdit_page1.setGeometry(QtCore.QRect(370, 130, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        self.lineEdit_page1.setFont(font)
        self.lineEdit_page1.setStyleSheet("color:white;\n"
"border: 2px solid #fb5b5d;\n"
"border-radius: 30;")
        self.lineEdit_page1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_page1.setObjectName("lineEdit_page1")
        self.label_3_page1 = QtWidgets.QLabel(self.widget_page1)
        self.label_3_page1.setGeometry(QtCore.QRect(90, 220, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(12)
        self.label_3_page1.setFont(font)
        self.label_3_page1.setStyleSheet("color: white\n"
"")
        self.label_3_page1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3_page1.setObjectName("label_3_page1")
        self.dateEdit_page1 = QtWidgets.QDateEdit(self.widget_page1)
        self.dateEdit_page1.setGeometry(QtCore.QRect(370, 220, 331, 61))
        self.dateEdit_page1.setStyleSheet("color:white;\n"
"border: 2px solid #fb5b5d;\n"
"border-radius: 30;")
        self.dateEdit_page1.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_page1.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit_page1.setCalendarPopup(False)
        self.dateEdit_page1.setDate(QtCore.QDate(2000, 12, 1))
        self.dateEdit_page1.setObjectName("dateEdit_page1")
        self.label_4_page1 = QtWidgets.QLabel(self.widget_page1)
        self.label_4_page1.setGeometry(QtCore.QRect(90, 340, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(12)
        self.label_4_page1.setFont(font)
        self.label_4_page1.setStyleSheet("color: white\n"
"")
        self.label_4_page1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4_page1.setObjectName("label_4_page1")
        self.checkBox_page1 = QtWidgets.QCheckBox(self.widget_page1)
        self.checkBox_page1.setGeometry(QtCore.QRect(380, 330, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        self.checkBox_page1.setFont(font)
        self.checkBox_page1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_page1.setAutoFillBackground(False)
        self.checkBox_page1.setStyleSheet("color:white;")
        self.checkBox_page1.setIconSize(QtCore.QSize(20, 20))
        self.checkBox_page1.setShortcut("")
        self.checkBox_page1.setCheckable(True)
        self.checkBox_page1.setChecked(False)
        self.checkBox_page1.setAutoRepeat(False)
        self.checkBox_page1.setAutoExclusive(False)
        self.checkBox_page1.setTristate(False)
        self.checkBox_page1.setObjectName("checkBox_page1")
        self.checkBox_2_page1 = QtWidgets.QCheckBox(self.widget_page1)
        self.checkBox_2_page1.setGeometry(QtCore.QRect(380, 360, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        self.checkBox_2_page1.setFont(font)
        self.checkBox_2_page1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_2_page1.setAutoFillBackground(False)
        self.checkBox_2_page1.setStyleSheet("color:white;")
        self.checkBox_2_page1.setIconSize(QtCore.QSize(20, 20))
        self.checkBox_2_page1.setShortcut("")
        self.checkBox_2_page1.setCheckable(True)
        self.checkBox_2_page1.setChecked(False)
        self.checkBox_2_page1.setAutoRepeat(False)
        self.checkBox_2_page1.setAutoExclusive(False)
        self.checkBox_2_page1.setTristate(False)
        self.checkBox_2_page1.setObjectName("checkBox_2_page1")
        self.checkBox_3_page1 = QtWidgets.QCheckBox(self.widget_page1)
        self.checkBox_3_page1.setGeometry(QtCore.QRect(380, 390, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        self.checkBox_3_page1.setFont(font)
        self.checkBox_3_page1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_3_page1.setAutoFillBackground(False)
        self.checkBox_3_page1.setStyleSheet("color:white;")
        self.checkBox_3_page1.setIconSize(QtCore.QSize(20, 20))
        self.checkBox_3_page1.setShortcut("")
        self.checkBox_3_page1.setCheckable(True)
        self.checkBox_3_page1.setChecked(False)
        self.checkBox_3_page1.setAutoRepeat(False)
        self.checkBox_3_page1.setAutoExclusive(False)
        self.checkBox_3_page1.setTristate(False)
        self.checkBox_3_page1.setObjectName("checkBox_3_page1")
        self.label_5_page1 = QtWidgets.QLabel(self.widget_page1)
        self.label_5_page1.setGeometry(QtCore.QRect(280, 440, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(9)
        self.label_5_page1.setFont(font)
        self.label_5_page1.setStyleSheet("color: #fb5b5d;")
        self.label_5_page1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5_page1.setObjectName("label_5_page1")

        window_name = "Form_page1"
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_page1.setText(_translate(window_name, "Далее"))
        self.label_page1.setText(_translate(window_name, "Ваша анкета"))
        self.label_2_page1.setText(_translate(window_name, "Три желания"))
        self.lineEdit_page1.setText(_translate(window_name, "Раз два три"))
        self.label_3_page1.setText(_translate(window_name, "Когда они исполнятся"))
        self.dateEdit_page1.setDisplayFormat(_translate(window_name, "dd.MM"))
        self.label_4_page1.setText(_translate(window_name, "Ваш пол"))
        self.checkBox_page1.setText(_translate(window_name, "Мужской"))
        self.checkBox_2_page1.setText(_translate(window_name, "Женский"))
        self.checkBox_3_page1.setText(_translate(window_name, "Не важно"))
        self.label_5_page1.setText(_translate(window_name, "Неверно указаны желания"))

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        window_name = "Form_page1"
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate(window_name, "Form_page1"))
        self.pushButton_page1.setText(_translate(window_name, "Далее"))
        self.label_page1.setText(_translate(window_name, "Ваша анкета"))
        self.label_2_page1.setText(_translate(window_name, "Три желания"))
        self.lineEdit_page1.setText(_translate(window_name, "Раз два три"))
        self.label_3_page1.setText(_translate(window_name, "Когла они исполнятся"))
        self.dateEdit_page1.setDisplayFormat(_translate(window_name, "dd.MM"))
        self.label_4_page1.setText(_translate(window_name, "Ваш пол"))
        self.checkBox_page1.setText(_translate(window_name, "Мужской"))
        self.checkBox_2_page1.setText(_translate(window_name, "Женский"))
        self.checkBox_3_page1.setText(_translate(window_name, "Не важно"))
        self.label_5_page1.setText(_translate(window_name, "Неверно указаны желания"))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())