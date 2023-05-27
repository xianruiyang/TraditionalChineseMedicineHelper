import my_database as md
#引入pyqt5库
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#引入其他窗口
import herb_input
import relation_input
import recipe_input
import merge_input
import adFind
import minePage
#引入界面ui
import med_data_user_form

class medMain(QWidget, med_data_user_form.Ui_Form):
    back_signal = pyqtSignal()
    def closeEvent(self, event):
        self.back_signal.emit()
        event.accept()
    def __init__(self):
        super(medMain, self).__init__()
        self.setupUi(self)
        self.connecter()

        self.herb_data = []
        self.relation_data = []
        self.recipe_data = []
        self.herb_model = QStandardItemModel(0,2)
        self.herb_model.setHorizontalHeaderLabels(["名称","别名"])
        self.relation_model = QStandardItemModel(0,3)
        self.relation_model.setHorizontalHeaderLabels(["药材1","关系","药材2"])
        self.recipe_model = QStandardItemModel(0,2)
        self.recipe_model.setHorizontalHeaderLabels(["名称","疗效"])
        self.Tcontent.setModel(self.herb_model)
        self.Tcontent.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Tcontent.setColumnWidth(0,100)
        self.Tcontent.setColumnWidth(1,700)

        self.db = md.herb_db('./data/meddb.json')
        self.herb_input = herb_input.herb_input()
        self.relation_input = relation_input.relation_input()
        self.recipe_input = recipe_input.recipe_input()
        self.merge_input = merge_input.merge_input()
        self.advance_find = adFind.Find()
        self.mine = minePage.Mine()

        self.db.update()
        self.update_content()
    def connecter(self):
        self.BAdd.clicked.connect(self.show_input)
        self.BDelete.clicked.connect(self.delete)
        self.CType.currentIndexChanged.connect(self.update_content)
        self.BFind.clicked.connect(self.update_content)
        self.BChange.clicked.connect(self.show_change)
        self.BAdvanced.clicked.connect(self.show_advance)

    def set_herb_table(self,table,data):
        table.setRowCount(len(data))
        for i in range(len(data)):
            table.setItem(i,0,QStandardItem(data[i][1][0]))
            table.setItem(i,1,QStandardItem(','.join(data[i][1][1])))
    def set_relation_table(self,table,data):
        table.setRowCount(len(data))
        for i in range(len(data)):
            table.setItem(i,0,QStandardItem(self.db.get_herb_name(data[i][1][0])))
            table.setItem(i,1,QStandardItem(md.RELATION_LIST[data[i][1][2]]))
            table.setItem(i,2,QStandardItem(self.db.get_herb_name(data[i][1][1])))
    def set_recipe_table(self,table,data):
        table.setRowCount(len(data))
        for i in range(len(data)):
            table.setItem(i,0,QStandardItem(data[i][1][0][0]))
            table.setItem(i,1,QStandardItem(data[i][1][0][1]))
    def update_content(self,no_use=0):
        if self.CType.currentIndex() == 0:
            self.BAdvanced.setText("合并药材")
            temp = self.db.get_herbs(self.IFind.text())
            for i in range(len(temp)):
                temp[i][1] = [temp[i][1]['name'],temp[i][1]['all_name'],temp[i][1]['intro'],temp[i][1]['compose']]
            self.herb_data = temp
            self.set_herb_table(self.herb_model,self.herb_data)
            self.Tcontent.setModel(self.herb_model)
            self.Tcontent.setColumnWidth(0,100)
            self.Tcontent.setColumnWidth(1,700)
        elif self.CType.currentIndex() == 1:
            self.BAdvanced.setText("高级配伍查询")
            self.relation_data = self.db.get_relations(self.IFind.text())
            self.set_relation_table(self.relation_model,self.relation_data)
            self.Tcontent.setModel(self.relation_model)
            self.Tcontent.setColumnWidth(0,200)
            self.Tcontent.setColumnWidth(1,100)
            self.Tcontent.setColumnWidth(2,200)
        else:
            self.BAdvanced.setText("配伍挖掘")
            self.recipe_data = self.db.get_recipes(self.IFind.text())
            self.set_recipe_table(self.recipe_model,self.recipe_data)
            self.Tcontent.setModel(self.recipe_model)
            self.Tcontent.setColumnWidth(0,100)
            self.Tcontent.setColumnWidth(1,700)
    def show_input(self):
        self.hide()
        if self.CType.currentIndex() == 0:
            self.herb_input.reset()
            self.herb_input.exec_()
            if self.herb_input.confirm:
                self.db.add_herb(self.herb_input.IName.text(),self.herb_input.compose_data,self.herb_input.IIntro.toPlainText())
                self.db.save()
                self.herb_input.confirm = 0
        elif self.CType.currentIndex() == 1:
            self.relation_input.reset()
            self.relation_input.exec_()
            if self.relation_input.confirm:
                self.db.add_relation(self.relation_input.IMed1.text(),self.relation_input.IMed2.text(),self.relation_input.CRelation.currentIndex())
                self.db.save()
                self.relation_input.confirm = 0
        else:
            self.recipe_input.reset()
            self.recipe_input.exec_()
            if self.recipe_input.confirm:
                self.db.add_recipe(self.recipe_input.output)
                self.db.save()
                self.recipe_input.confirm = 0
        self.update_content()
        self.show()
    def show_change(self):
        id = self.Tcontent.currentIndex().row()
        if id==-1:
            return
        self.hide()
        if self.CType.currentIndex() == 0:
            self.herb_input.reset()
            self.herb_input.setdata(self.herb_data[id][1])
            id = self.herb_data[id][0]
            self.herb_input.exec_()
            if self.herb_input.confirm:
                self.db.change_realherb(id,self.herb_input.IName.text().split(','),self.herb_input.compose_data,self.herb_input.IIntro.toPlainText())
                self.db.save()
                self.herb_input.confirm = 0
        elif self.CType.currentIndex() == 1:
            pass
        else:
            self.recipe_input.reset()
            self.recipe_input.setdata(self.recipe_data[id][1])
            id = self.recipe_data[id][0]
            self.recipe_input.exec_()
            if self.recipe_input.confirm:
                self.db.change_recipe(id,self.recipe_input.output)
                self.db.save()
                self.recipe_input.confirm = 0
        self.update_content()
        self.show()
    def delete(self):
        id = self.Tcontent.currentIndex().row()
        if id==-1:
            return
        if self.CType.currentIndex() == 0:
            self.db.del_realherb(self.herb_data[id][0])
        elif self.CType.currentIndex() == 1:
            self.db.del_relation(self.relation_data[id][0])
        else:
            self.db.del_recipe(self.recipe_data[id][0])
        self.db.save()
        self.update_content()
    def show_advance(self):
        self.hide()
        if self.CType.currentIndex() == 0:
            self.merge_input.reset()
            self.merge_input.exec()
            if self.merge_input.confirm:
                self.db.merge_herb(self.merge_input.IMed2.text(),self.merge_input.IMed1.text())
                self.db.save()
                self.merge_input.confirm = 0
        elif self.CType.currentIndex() == 1:
            self.advance_find.reset()
            self.advance_find.exec()
        else:
            self.mine.exec()
        self.update_content()
        self.show()
