# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'merge_input_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(417, 116)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon/med.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.BY = QtWidgets.QPushButton(Form)
        self.BY.setGeometry(QtCore.QRect(170, 80, 93, 28))
        self.BY.setObjectName("BY")
        self.BN = QtWidgets.QPushButton(Form)
        self.BN.setGeometry(QtCore.QRect(300, 80, 93, 28))
        self.BN.setObjectName("BN")
        self.splitter_3 = QtWidgets.QSplitter(Form)
        self.splitter_3.setGeometry(QtCore.QRect(10, 20, 387, 39))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.IMed1 = QtWidgets.QLineEdit(self.splitter)
        self.IMed1.setObjectName("IMed1")
        self.label_3 = QtWidgets.QLabel(self.splitter_3)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        self.label_2.setObjectName("label_2")
        self.IMed2 = QtWidgets.QLineEdit(self.splitter_2)
        self.IMed2.setObjectName("IMed2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "合并药材"))
        self.BY.setText(_translate("Form", "确定"))
        self.BN.setText(_translate("Form", "取消"))
        self.label.setText(_translate("Form", "药材1"))
        self.label_3.setText(_translate("Form", "合并到"))
        self.label_2.setText(_translate("Form", "药材2"))
