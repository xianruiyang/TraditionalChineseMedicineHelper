# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'learn_log_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(870, 569)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon/med.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(10, 50, 281, 511))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 279, 509))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.LName = QtWidgets.QListView(self.scrollAreaWidgetContents)
        self.LName.setGeometry(QtCore.QRect(10, 10, 261, 491))
        self.LName.setObjectName("LName")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(Form)
        self.scrollArea_2.setGeometry(QtCore.QRect(310, 10, 541, 551))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 539, 549))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.LTime = QtWidgets.QListView(self.scrollAreaWidgetContents_2)
        self.LTime.setGeometry(QtCore.QRect(10, 10, 521, 531))
        self.LTime.setObjectName("LTime")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.IFind = QtWidgets.QLineEdit(Form)
        self.IFind.setGeometry(QtCore.QRect(10, 10, 181, 31))
        self.IFind.setObjectName("IFind")
        self.BFind = QtWidgets.QPushButton(Form)
        self.BFind.setGeometry(QtCore.QRect(200, 10, 93, 28))
        self.BFind.setObjectName("BFind")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "学习时间查询"))
        self.BFind.setText(_translate("Form", "查找"))
