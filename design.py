# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(372, 376)
        Form.setMinimumSize(QtCore.QSize(372, 376))
        Form.setMaximumSize(QtCore.QSize(372, 376))
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget{\n"
"    background-color: rgb(240, 240, 240);\n"
"}\n"
"\n"
"QFrame{\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    background-color : white;\n"
"}")
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 10, 81, 23))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border-radius:7px;\n"
"    background-color:white;\n"
"}\n"
"QPushButton::hover{\n"
"    border-radius:7px;\n"
"    background-color:silver;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 261, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(10, 40, 351, 23))
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 70, 351, 291))
        self.plainTextEdit.setAutoFillBackground(True)
        self.plainTextEdit.setStyleSheet("QPlainTextEdit{\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"    color:black;\n"
"}")
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "YouSound v1.0"))
        self.pushButton.setText(_translate("Form", "Download"))
