from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#引入界面ui
import match_detail_form

class Detail(QDialog,match_detail_form.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.LContentin_data = []
        self.LContentin_model = QStringListModel()
        self.LContentout_data = []
        self.LContentout_model = QStringListModel()

        self.connecter()

    def change(self):
        self.LContentin_model.setStringList(self.LContentin_data)
        self.LContentin.setModel(self.LContentin_model)
        self.LContentout_model.setStringList(self.LContentout_data)
        self.LContentout.setModel(self.LContentout_model)

    def connecter(self):
        pass
