# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'decide_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1119, 843)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon/med.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.IName = QtWidgets.QLineEdit(Form)
        self.IName.setGeometry(QtCore.QRect(20, 80, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.IName.setFont(font)
        self.IName.setObjectName("IName")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(270, 50, 841, 331))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 839, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.TContent = QtWidgets.QTableView(self.scrollAreaWidgetContents)
        self.TContent.setGeometry(QtCore.QRect(10, 10, 821, 311))
        self.TContent.setObjectName("TContent")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.IFind = QtWidgets.QLineEdit(Form)
        self.IFind.setGeometry(QtCore.QRect(830, 10, 171, 31))
        self.IFind.setText("")
        self.IFind.setObjectName("IFind")
        self.BFind = QtWidgets.QPushButton(Form)
        self.BFind.setGeometry(QtCore.QRect(1010, 10, 93, 28))
        self.BFind.setObjectName("BFind")
        self.BMed_Normal = QtWidgets.QPushButton(Form)
        self.BMed_Normal.setGeometry(QtCore.QRect(20, 160, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BMed_Normal.setFont(font)
        self.BMed_Normal.setObjectName("BMed_Normal")
        self.BMed_Help = QtWidgets.QPushButton(Form)
        self.BMed_Help.setGeometry(QtCore.QRect(20, 230, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BMed_Help.setFont(font)
        self.BMed_Help.setObjectName("BMed_Help")
        self.BMed_AI = QtWidgets.QPushButton(Form)
        self.BMed_AI.setGeometry(QtCore.QRect(20, 300, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BMed_AI.setFont(font)
        self.BMed_AI.setObjectName("BMed_AI")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(270, 400, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Tips = QtWidgets.QLabel(Form)
        self.Tips.setGeometry(QtCore.QRect(350, 410, 181, 16))
        self.Tips.setObjectName("Tips")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(270, 440, 841, 391))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 130, 841, 261))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 839, 259))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.TMed = QtWidgets.QTableView(self.scrollAreaWidgetContents_2)
        self.TMed.setGeometry(QtCore.QRect(10, 10, 821, 241))
        self.TMed.setObjectName("TMed")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.LDeal = QtWidgets.QPlainTextEdit(self.groupBox)
        self.LDeal.setGeometry(QtCore.QRect(110, 20, 721, 41))
        self.LDeal.setReadOnly(True)
        self.LDeal.setPlainText("")
        self.LDeal.setObjectName("LDeal")
        self.LUse = QtWidgets.QPlainTextEdit(self.groupBox)
        self.LUse.setGeometry(QtCore.QRect(110, 80, 721, 41))
        self.LUse.setReadOnly(True)
        self.LUse.setPlainText("")
        self.LUse.setObjectName("LUse")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(50, 30, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(50, 90, 72, 15))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "对症辅助决策下方"))
        self.IName.setText(_translate("Form", "未知"))
        self.label.setText(_translate("Form", "病人名称"))
        self.label_2.setText(_translate("Form", "病历史"))
        self.BFind.setText(_translate("Form", "查询"))
        self.BMed_Normal.setText(_translate("Form", "常规开药"))
        self.BMed_Help.setText(_translate("Form", "辅助开药"))
        self.BMed_AI.setText(_translate("Form", "智能开药"))
        self.label_3.setText(_translate("Form", "药方"))
        self.Tips.setText(_translate("Form", "请选择病例以查看历史药方"))
        self.label_4.setText(_translate("Form", "制法"))
        self.label_5.setText(_translate("Form", "用法"))
