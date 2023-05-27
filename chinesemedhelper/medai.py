import my_database as md
#引入pyqt5库
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#引入其他窗口

#引入界面ui
import medai_form
import aiRecipe

class medai(QDialog, medai_form.Ui_Form):
    def __init__(self):
        super(medai, self).__init__()
        self.setupUi(self)
        self.connecter()

        self.LHerbs_list = []
        self.LHerbs_model = QStringListModel()
        self.LHerbs_model.setStringList(self.LHerbs_list)
        self.LHerbs.setModel(self.LHerbs_model)

        self.confirm = False
    def connecter(self):
        self.BFind.clicked.connect(self.find)
        self.BConfirm.clicked.connect(self.write)
        self.BCancel.clicked.connect(self.close)
        return
    def find(self):
        inp = self.TInput.toPlainText()
        self.LHerbs_list = aiRecipe.aiFind(inp)
        self.LHerbs_model.setStringList(self.LHerbs_list)
        print(inp)
    def write(self):
        self.out = [["",self.TInput.toPlainText(),"",""],[]]
        for i in self.LHerbs_list:
            self.out[1].append([i,"无","6"])
        self.confirm = True
        self.close()
    def reset(self):
        self.__init__()
    def select(self):
        return
