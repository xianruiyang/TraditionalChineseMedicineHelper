import json
import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#引入界面ui
import med_normal_form

class Med_normal(QDialog,med_normal_form.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height());

        self.name = ""
        self.row = -1
        self.column = -1

        self.table_init()
        self.connecter()

    def ouside_init(self,sick,med):
        self.ISick.setText(sick)
        self,current_content = med
        self.set_table(self.TContent,self.current_content)

    def table_init(self):
        self.current_content = []

        self.TContent_model = QStandardItemModel(0,3)
        self.TContent_model.setHorizontalHeaderLabels(["药材","预处理","剂量（克）"])

        self.TContent.setModel(self.TContent_model)
        self.TContent.setColumnWidth(0,250)
        self.TContent.setColumnWidth(1,200)
        self.TContent.setColumnWidth(2,250)
        self.TContent.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def set_table(self,table,data):
        table.setRowCount(len(data))
        for i in range(len(data)):
            for j in range(len(data[i])):
                table.setItem(i,j,QStandardItem(data[i][j]))

    def add(self):
        name = self.IMed.text()
        deal = self.IDeal.text()
        count = self.ICount.text()
        for i in range(len(self.current_content)):
            if name == self.current_content[i][0]:
                self.current_content[i][2]= str(int(self.current_content[i][2])+int(count))
                self.set_table(self.TContent_model,self.current_content)
                return
        self.current_content.append([name,deal,count])
        self.set_table(self.TContent_model,self.current_content)

    def delete(self):
        if self.row == -1:
            return
        self.current_content.pop(self.row)
        self.set_table(self.TContent_model,self.current_content)
        self.row = -1
        self.column = -1

    def select(self,i):
        self.row = i.row()
        self.column = i.column()
        popMenu = QMenu()
        change = popMenu.addAction("修改")
        delete = popMenu.addAction("删除")
        action = popMenu.exec_(QCursor.pos())
        if action == change:
            self.onClickedTableView(i)
        if action == delete:
            self.delete()

    def onClickedTableView(self, i):
        C=QInputDialog.getText(self, "修改", "请输入:", QLineEdit.Normal,text=self.current_content[i.row()][i.column()])
        if not C[1]:
            return
        self.current_content[i.row()][i.column()]=C[0]
        self.set_table(self.TContent_model,self.current_content)
            
    def confirm(self):
        if len(self.current_content)==0 or self.ISick.toPlainText()=="":
            self.close()
            return
        date = time.strftime("%Y/%m/%d %H:%M:%S")
        f = open("./data/patient.json","r",encoding="utf-8")
        self.patient_data = json.load(f)
        f.close()
        f = open("./data/patient.json","w",encoding="utf-8")
        if not self.name in self.patient_data.keys():
            self.patient_data[self.name] = []
        temp = {}
        temp["intro"] = [date,self.IAcount.text(),self.ISick.toPlainText()]
        temp["med"] = {}
        temp["med"]["deal"] = self.IAdeal.toPlainText()
        temp["med"]["use"] = self.IUse.toPlainText()
        temp["med"]["recipe"] = self.current_content
        self.patient_data[self.name].append(temp)
        json.dump(self.patient_data,f,ensure_ascii=False)
        f.close()
        self.close()

    def connecter(self):
        self.BConfirm.clicked.connect(self.confirm)
        self.BAdd.clicked.connect(self.add)
        self.BDelete.clicked.connect(self.delete)
        self.BClear.clicked.connect(self.table_init)
        self.TContent.clicked.connect(self.select)
    def reset(self):
        self.__init__()
    def setdata(self,inp):
        self.ISick.setPlainText(inp[0][1])
        self.IAdeal.setPlainText(inp[0][2])
        self.IUse.setPlainText(inp[0][3])
        self.current_content = inp[1]
        self.set_table(self.TContent_model,self.current_content)