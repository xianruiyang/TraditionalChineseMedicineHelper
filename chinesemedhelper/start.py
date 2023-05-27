import sys
#引入pyqt5库
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#引入其他窗口
from login import *
#from match_database import *
from decide import *
from med_data_user import *
#引入界面ui
import start_form

class Start(QWidget, start_form.Ui_Form):
    def __init__(self):
        super(Start, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height());
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("./icon/first_background.png")))
        self.setPalette(self.palette)
        self.connecter()

        self.login = Login()
        #self.Database = Database()
        self.Database = medMain()
        self.decide = Decide()

        self.show()
    def connecter(self):
        self.BLearn.clicked.connect(self.learn)
        self.BFind.clicked.connect(self.Database)
        self.BDecide.clicked.connect(self.decide)
    def learn(self):
        self.hide()
        self.login.show()
        self.login.back_signal.connect(self.reshow)
    def Database(self):
        self.hide()
        self.Database.show()
        self.Database.back_signal.connect(self.reshow)
    def decide(self):
        self.hide()
        self.decide.show()
        self.decide.back_signal.connect(self.reshow)
    def reshow(self):
        self.show()
if __name__ == '__main__':
    argvs = sys.argv
    argvs.append('--ppapi-flash-path=./support/pepflashplayer.dll')
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(argvs)
    Start = Start()
    sys.exit(app.exec_())
