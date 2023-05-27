# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'medai_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(805, 685)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon/med.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.TInput = QtWidgets.QPlainTextEdit(Form)
        self.TInput.setGeometry(QtCore.QRect(20, 20, 611, 121))
        self.TInput.setObjectName("TInput")
        self.BFind = QtWidgets.QPushButton(Form)
        self.BFind.setGeometry(QtCore.QRect(650, 20, 141, 121))
        self.BFind.setObjectName("BFind")
        self.BConfirm = QtWidgets.QPushButton(Form)
        self.BConfirm.setGeometry(QtCore.QRect(700, 640, 93, 28))
        self.BConfirm.setObjectName("BConfirm")
        self.BCancel = QtWidgets.QPushButton(Form)
        self.BCancel.setGeometry(QtCore.QRect(590, 640, 93, 28))
        self.BCancel.setObjectName("BCancel")
        self.LHerbs = QtWidgets.QListView(Form)
        self.LHerbs.setGeometry(QtCore.QRect(20, 180, 771, 441))
        self.LHerbs.setObjectName("LHerbs")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 160, 101, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "智能配药"))
        self.BFind.setText(_translate("Form", "查询"))
        self.BConfirm.setText(_translate("Form", "确认"))
        self.BCancel.setText(_translate("Form", "取消"))
        self.label.setText(_translate("Form", "智能推荐药方"))
