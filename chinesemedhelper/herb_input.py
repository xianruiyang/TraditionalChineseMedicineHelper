import my_database as md
#引入pyqt5库
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#引入其他窗口

#引入界面ui
import herb_input_form

class herb_input(QDialog, herb_input_form.Ui_Dialog):
    def __init__(self):
        super(herb_input, self).__init__()
        self.setupUi(self)
        self.connecter()

        self.confirm = False

        self.compose_data = []
        self.compose_model = QStringListModel()
        self.compose_model.setStringList(self.compose_data)
        self.LCom.setModel(self.compose_model)
    def connecter(self):
        self.BAdd.clicked.connect(self.add)
        self.BDelete.clicked.connect(self.delete)
        self.BY.clicked.connect(self.write)
        self.BN.clicked.connect(self.close)

    def add(self):
        name = self.ICom.text()
        if name in self.compose_data:
            return
        self.compose_data.append(name)
        self.compose_data.sort()
        self.compose_model.setStringList(self.compose_data)
    def delete(self):
        id = self.LCom.currentIndex().row()
        if id==-1:
            return
        self.compose_data.pop(id)
        self.compose_model.setStringList(self.compose_data)
    def write(self):
        self.confirm = True
        self.close()
    def reset(self):
        self.__init__()
    def setdata(self,ilist):
        self.IName.setText(",".join(ilist[1]))
        self.IIntro.setPlainText(ilist[2])
        self.compose_data = list(ilist[3])
        self.compose_model.setStringList(self.compose_data)
