import my_database as md
#引入pyqt5库
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#引入其他窗口

#引入界面ui
import recipe_input_form

class recipe_input(QDialog, recipe_input_form.Ui_Form):
    def __init__(self):
        super(recipe_input, self).__init__()
        self.setupUi(self)
        self.connecter()

        self.output = []
        self.recipe = md.recipe_input_helper()
        self.db = md.herb_db('./data/meddb.json')
        self.db.update()

        self.TContent_model = QStandardItemModel(0,3)
        self.TContent_model.setHorizontalHeaderLabels(["药材","预处理","剂量（克）"])

        self.TContent.setModel(self.TContent_model)
        self.TContent.setColumnWidth(0,250)
        self.TContent.setColumnWidth(1,200)
        self.TContent.setColumnWidth(2,250)
        self.TContent.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.confirm = False
    def connecter(self):
        self.BY.clicked.connect(self.write)
        self.BN.clicked.connect(self.close)
        self.BAdd.clicked.connect(self.add)
        self.BDelete.clicked.connect(self.delete)
        self.BClear.clicked.connect(self.clear)
    def update(self):
        self.TContent_model.setRowCount(len(self.recipe.compose))
        for i in range(len(self.recipe.compose)):
            self.TContent_model.setItem(i,0,QStandardItem(self.recipe.compose[i][0]))
            self.TContent_model.setItem(i,1,QStandardItem(self.recipe.compose[i][1]))
            self.TContent_model.setItem(i,2,QStandardItem(str(self.recipe.compose[i][2])))
    def write(self):
        self.recipe.set_name(self.IName.text())
        self.recipe.set_usage(self.IUsage.toPlainText())
        self.recipe.set_dipose(self.IAdeal.toPlainText())
        self.recipe.set_use(self.IUse.toPlainText())
        self.output = self.recipe.output()
        if self.output:
            self.confirm = True
            self.close()
            return
    def add(self):
        temp = self.ICount.text()
        try:
            temp = float(temp)
        except:
            return
        self.recipe.add_herb(self.IMed.text(),self.IDeal.text(),temp)
        self.update()
    def delete(self):
        id = self.TContent.currentIndex().row()
        if id == -1:
            return
        self.recipe.delete_herb(id)
        self.update()
    def clear(self):
        self.recipe.clear()
        self.update()
    def reset(self):
        self.__init__()
    def setdata(self,ilist):
        self.IName.setText(ilist[0][0])
        self.IUsage.setPlainText(ilist[0][1])
        self.IAdeal.setPlainText(ilist[0][2])
        self.IUse.setPlainText(ilist[0][3])
        compose = list(ilist[1])
        for i in range(len(compose)):
            compose[i] = list(compose[i])
            compose[i][0] = self.db.get_herb_name(compose[i][0])
        self.recipe.set_herb(compose)
        self.update()