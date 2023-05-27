from meddb import *

import myfun as mf

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import match_detail
#引入界面ui
import find_form

class Find(QWidget,find_form.Ui_Form):
    def reshow(self):
        self.back_signal.emit()

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

        self.db = Med_database()

        self.LMed_data = self.db.get_all_med()
        self.LMed_model = QStringListModel()
        self.LMed_model.setStringList(self.LMed_data)
        self.LMed.setModel(self.LMed_model)

        self.connecter()

    def load_selected(self):
        self.LSelected_model.setStringList(self.LSelected_data)
        self.LSelected.setModel(self.LSelected_model)

    def find(self):
        inp = self.IFind.text()
        self.LMed_data = mf.sort_list(self.LMed_data,inp)
        self.LMed_model.setStringList(self.LMed_data)
        self.LMed.setModel(self.LMed_model)

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
        result = self.db.show_meds_match(self.LSelected_data)
        cov1 = []
        cov2 = []
        for i in result[0]:
            if i[2] == 0:
                cov1.append(i[0]+" "+self.matchnum[i[2]])
            else:
                cov1.append(i[0]+" "+self.matchnum[i[2]]+" "+i[1])
        for i in result[1]:
            if i[2] == 0:
                cov1.append(i[0]+" "+self.matchnum[i[2]])
            else:
                cov2.append(i[0]+" "+self.matchnum[i[2]]+" "+i[1])
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