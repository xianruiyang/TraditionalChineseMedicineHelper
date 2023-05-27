import json

import myfun as mf

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#引入界面ui
import learn_log_form

class Learn_log(QDialog,learn_log_form.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height());
        self.ltime_model = QStringListModel()

        self.history = {}

        self.initload()

        self.connecter()

    def initload(self):
        f = open('./data/user.json',encoding="utf-8")
        self.init_list = json.load(f)
        f.close()
        self.lname_model = QStringListModel()
        self.lname_data = []
        for i in self.init_list:
            self.lname_data.append(i.get('name'))
        self.lname_model.setStringList(self.lname_data)
        self.LName.setModel(self.lname_model)

    def load_history(self):
        self.ltime_data = []
        for i in self.history:
            self.ltime_data.append("观看 "+i['name']+" "+str(int(i['time']/60)+1)+" 分钟")
        if len(self.ltime_data) == 0:
            self.ltime_data.append("暂无观看记录")
        else:
            self.ltime_data.sort()
        self.ltime_model.setStringList(self.ltime_data)
        self.LTime.setModel(self.ltime_model)

    def find(self):
        inp = self.IFind.text()
        self.lname_data = mf.sort_list(self.lname_data,inp)
        self.lname_model.setStringList(self.lname_data)
        self.LName.setModel(self.lname_model)

    def select_name(self,item):
        name = self.lname_data[item.row()]
        for i in range(len(self.init_list)):
            if self.init_list[i]["name"] == name:
                self.history = self.init_list[i]["history"]
                self.load_history()

    def connecter(self):
        self.BFind.clicked.connect(self.find)
        self.LName.clicked.connect(self.select_name)
