import my_database as md

from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QStringListModel

import match_detail
#引入界面ui
import find_form

class Find(QDialog,find_form.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height());

        self.detail = match_detail.Detail()

        self.matchnum = ['单行','须','使','畏','恶','反']
        self.LSelected_data = []
        self.LSelected_model = QStringListModel()
        self.Med_index = -1
        self.Selected_index = -1

        self.db = md.herb_db('./data/meddb.json')
        self.db.update()

        self.row_data = self.db.get_herbs()
        self.LMed_data = []
        self.LMed_model = QStringListModel()
        self.LMed.setModel(self.LMed_model)

        self.find()

        self.connecter()

    def load_selected(self):
        self.LSelected_model.setStringList(self.LSelected_data)
        self.LSelected.setModel(self.LSelected_model)

    def find(self):
        inp = self.IFind.text()
        self.row_data = self.db.get_herbs(inp)
        self.LMed_data = []
        for i in self.row_data:
            self.LMed_data.append(i[1]['name'])
        self.LMed_model.setStringList(self.LMed_data)

    def cmed(self,item):
        self.Med_index = item.row()

    def csel(self,item):
        self.Selected_index = item.row()

    def ladd(self):
        if self.Med_index == -1:
            return
        if not self.LSelected_data.count(self.LMed_data[self.Med_index]):
            self.LSelected_data.append(self.LMed_data[self.Med_index])
        self.Med_index = -1
        self.load_selected()

    def ldelete(self):
        if self.Selected_index == -1:
            return
        self.LSelected_data.pop(self.Selected_index)
        self.Selected_index = -1
        self.load_selected()

    def lclear(self):
        self.LSelected_data = []
        self.Selected_index = -1
        self.load_selected()

    def med_search(self):
        result = self.db.find_relations(self.LSelected_data)
        cov1 = []
        cov2 = []
        for i in result[0]:
            if i[2] == 0:
                cov1.append(self.db.get_herb_name(i[0])+" "+self.matchnum[i[2]])
            else:
                cov1.append(self.db.get_herb_name(i[0])+" "+self.matchnum[i[2]]+" "+self.db.get_herb_name(i[1]))
        for i in result[1]:
            if i[2] == 0:
                cov1.append(self.db.get_herb_name(i[0])+" "+self.matchnum[i[2]])
            else:
                cov2.append(self.db.get_herb_name(i[0])+" "+self.matchnum[i[2]]+" "+self.db.get_herb_name(i[1]))
        self.detail.LContentin_data = cov1
        self.detail.LContentout_data = cov2
        self.detail.change()
        self.detail.exec()

    def connecter(self):
        self.BFind.clicked.connect(self.find)
        self.LMed.clicked.connect(self.cmed)
        self.LSelected.clicked.connect(self.csel)
        self.BAdd.clicked.connect(self.ladd)
        self.BDelete.clicked.connect(self.ldelete)
        self.BClear.clicked.connect(self.lclear)
        self.BRun.clicked.connect(self.med_search)

    def reset(self):
        self.__init__()