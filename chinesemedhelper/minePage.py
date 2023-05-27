#引入pyqt5库
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#引入界面ui
import minePage_form

import mining

class Mine(QDialog, minePage_form.Ui_Form):
    def __init__(self):
        super(Mine, self).__init__()
        self.setupUi(self)

        self.TResult_data = []
        self.TResult_model = QStandardItemModel(0,2)
        self.TResult_model.setHorizontalHeaderLabels(["配伍","频繁度"])
        self.TResult.setModel(self.TResult_model)
        self.TResult.setColumnWidth(0,600)
        self.TResult.setColumnWidth(1,100)

        self.LRecipe_model = QStringListModel()
        self.LRecipe_model.setStringList([])
        self.LRecipe.setModel(self.LRecipe_model)

        self.connecter()
    def connecter(self):
        self.BMine.clicked.connect(self.mine)
        self.TResult.clicked.connect(self.writeList)
    def mine(self):
        try:
            IMinHerNum = int(self.IMinHerNum.text())
            IMinChainLen = int(self.IMinChainLen.text())
            IMinChainNum = int(self.IMinChainNum.text())
            if IMinHerNum < IMinChainNum:
                IMinHerNum = IMinChainNum
            self.TResult_data = mining.mineUsing_fpTree(IMinHerNum,IMinChainLen,IMinChainNum)
        except:
            return
        self.writeTable()
    def writeTable(self):
        table = self.TResult_model
        data = self.TResult_data
        table.setRowCount(len(data))
        for i in range(len(data)):
            table.setItem(i,0,QStandardItem("，".join(data[i]["chain"])))
            table.setItem(i,1,QStandardItem(str(data[i]["num"])))
        return
    def writeList(self,id):
        id = id.row()
        self.LRecipe_model.setStringList(self.TResult_data[id]["recipes"])

