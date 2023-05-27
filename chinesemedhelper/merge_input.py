#引入pyqt5库
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#引入其他窗口

#引入界面ui
import merge_input_form

class merge_input(QDialog, merge_input_form.Ui_Form):
    def __init__(self):
        super(merge_input, self).__init__()
        self.setupUi(self)
        self.connecter()

        self.confirm = False
    def connecter(self):
        self.BY.clicked.connect(self.write)
        self.BN.clicked.connect(self.close)
    def write(self):
        self.confirm = True
        self.close()
    def reset(self):
        self.__init__()
