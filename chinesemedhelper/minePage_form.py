# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'minePage_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(791, 763)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon/med.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(150, 10, 441, 131))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(30, 20, 387, 90))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.IMinHerNum = QtWidgets.QLineEdit(self.widget)
        self.IMinHerNum.setObjectName("IMinHerNum")
        self.gridLayout.addWidget(self.IMinHerNum, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.IMinChainLen = QtWidgets.QLineEdit(self.widget)
        self.IMinChainLen.setObjectName("IMinChainLen")
        self.gridLayout.addWidget(self.IMinChainLen, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.IMinChainNum = QtWidgets.QLineEdit(self.widget)
        self.IMinChainNum.setObjectName("IMinChainNum")
        self.gridLayout.addWidget(self.IMinChainNum, 2, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.BMine = QtWidgets.QPushButton(self.widget)
        self.BMine.setObjectName("BMine")
        self.horizontalLayout.addWidget(self.BMine)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(20, 180, 761, 261))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 759, 259))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.TResult = QtWidgets.QTableView(self.scrollAreaWidgetContents)
        self.TResult.setGeometry(QtCore.QRect(0, 0, 761, 261))
        self.TResult.setObjectName("TResult")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(30, 160, 72, 15))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(30, 460, 72, 15))
        self.label_9.setObjectName("label_9")
        self.scrollArea_2 = QtWidgets.QScrollArea(Form)
        self.scrollArea_2.setGeometry(QtCore.QRect(20, 480, 761, 261))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 759, 259))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.LRecipe = QtWidgets.QListView(self.scrollAreaWidgetContents_2)
        self.LRecipe.setGeometry(QtCore.QRect(0, 0, 761, 261))
        self.LRecipe.setObjectName("LRecipe")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "配伍挖掘"))
        self.label.setText(_translate("Form", "药材最小频繁度"))
        self.label_6.setText(_translate("Form", "配伍最小链长"))
        self.label_7.setText(_translate("Form", "配伍最小频繁度"))
        self.BMine.setText(_translate("Form", "开始挖掘"))
        self.label_8.setText(_translate("Form", "挖掘结果"))
        self.label_9.setText(_translate("Form", "包含药方"))
