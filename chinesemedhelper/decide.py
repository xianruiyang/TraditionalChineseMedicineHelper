import json

import myfun as mf

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import med_normal
import med_db
import medai
#引入界面ui
import decide_form

class Decide(QWidget,decide_form.Ui_Form):
    back_signal = pyqtSignal()
    def closeEvent(self, event):
        self.back_signal.emit()
        event.accept()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height());

        self.med_n = med_normal.Med_normal()
        self.med_h = med_db.med_db()
        self.med_a = medai.medai()

        f = open("./data/patient.json",encoding="utf-8")
        self.patient_data = json.load(f)
        f.close()

        self.table_init()
        self.connecter()
    def table_init(self):
        self.LDeal.setPlainText("")
        self.LUse.setPlainText("")

        self.current_content = []

        self.TContent_model = QStandardItemModel(0,3)
        self.TContent_model.setHorizontalHeaderLabels(["日期","剂数","症状"])

        self.TMed_model = QStandardItemModel(0,3)
        self.TMed_model.setHorizontalHeaderLabels(["药材","预处理","剂量（克）"])

        self.TContent.setModel(self.TContent_model)
        self.TContent.setColumnWidth(0,200)
        self.TContent.setColumnWidth(1,100)
        self.TContent.setColumnWidth(2,500)
        self.TContent.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.TMed.setModel(self.TMed_model)
        self.TMed.setColumnWidth(0,300)
        self.TMed.setColumnWidth(1,200)
        self.TMed.setColumnWidth(2,300)
        self.TMed.setEditTriggers(QAbstractItemView.NoEditTriggers)
    def set_table(self,table,data):
        table.setRowCount(len(data))
        for i in range(len(data)):
            for j in range(len(data[i])):
                table.setItem(i,j,QStandardItem(data[i][j]))
    def set_table_pro(self,table,data,str):
        table.setRowCount(len(data))
        for i in range(len(data)):
            for j in range(len(data[i][str])):
                table.setItem(i,j,QStandardItem(data[i][str][j]))
    def change_name(self):
        name = self.IName.text()
        if name in self.patient_data.keys():
            self.current_content = self.patient_data[name]
            self.set_table_pro(self.TContent_model,self.current_content,'intro')
            self.TContent.setModel(self.TContent_model)
            self.TMed_model.setRowCount(0)
            return
        self.table_init()
    def select_item(self,i):
        i = i.row()
        self.LDeal.setPlainText(self.current_content[i]["med"]["deal"])
        self.LUse.setPlainText(self.current_content[i]["med"]["use"])
        self.set_table(self.TMed_model,self.current_content[i]["med"]["recipe"])
    def find(self):
        inp = self.IFind.text()
        self.current_content = mf.sort_list(self.current_content,inp,mf.compare_strs)
        self.set_table_pro(self.TContent_model,self.current_content,'intro')
    def show_med_n(self):
        self.hide()
        self.med_n.reset()
        self.med_n.name = self.IName.text()
        self.med_n.exec()
        self.show()
        f = open("./data/patient.json")
        self.patient_data = json.load(f)
        f.close()
        self.change_name()
        self.set_table_pro(self.TContent_model,self.current_content,'intro')
    def show_med_h(self):
        self.hide()
        self.med_h.reset()
        self.med_h.exec()
        if self.med_h.confirm:
            self.med_n.reset()
            self.med_n.name = self.IName.text()
            self.med_n.setdata(self.med_h.out)
            self.med_n.exec()
            self.show()
            f = open("./data/patient.json",encoding="utf-8")
            self.patient_data = json.load(f)
            f.close()
            self.med_h.confirm = False
        self.show()
        self.change_name()
        self.set_table_pro(self.TContent_model,self.current_content,'intro')
    def show_med_a(self):
        self.hide()
        self.med_a.reset()
        self.med_a.exec()
        if self.med_a.confirm:
            self.med_n.reset()
            self.med_n.name = self.IName.text()
            self.med_n.setdata(self.med_a.out)
            self.med_n.exec()
            self.show()
            f = open("./data/patient.json",encoding="utf-8")
            self.patient_data = json.load(f)
            f.close()
            self.med_a.confirm = False
        self.show()
        self.change_name()
        self.set_table_pro(self.TContent_model,self.current_content,'intro')

    def connecter(self):
        self.IName.textChanged.connect(self.change_name)
        self.TContent.clicked.connect(self.select_item)
        self.BFind.clicked.connect(self.find)
        self.BMed_Normal.clicked.connect(self.show_med_n)
        self.BMed_Help.clicked.connect(self.show_med_h)
        self.BMed_AI.clicked.connect(self.show_med_a)
