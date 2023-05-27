import my_database as md
#引入pyqt5库
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#引入其他窗口

#引入界面ui
import med_db_form

class med_db(QDialog, med_db_form.Ui_Form):
    def __init__(self):
        super(med_db, self).__init__()
        self.setupUi(self)
        self.connecter()

        self.out = []
        self.db = md.herb_db('./data/meddb.json')
        self.db.update()

        self.recipe_data = self.db.get_recipes()
        self.recipe_model = QStandardItemModel(0,2)
        self.recipe_model.setHorizontalHeaderLabels(["名称","疗效"])
        self.TRecipe.setModel(self.recipe_model)
        self.TRecipe.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.find()

        self.confirm = False
    def connecter(self):
        self.BY.clicked.connect(self.write)
        self.BN.clicked.connect(self.close)
        self.BFind.clicked.connect(self.find)
        self.TRecipe.doubleClicked.connect(self.write)
    def find(self):
        self.recipe_data = self.db.get_recipes(self.IFind.toPlainText())
        self.recipe_model.setRowCount(len(self.recipe_data))
        for i in range(len(self.recipe_data)):
            self.recipe_model.setItem(i,0,QStandardItem(self.recipe_data[i][1][0][0]))
            self.recipe_model.setItem(i,1,QStandardItem(self.recipe_data[i][1][0][1]))
    def write(self):
        id = self.TRecipe.currentIndex().row()
        self.out = self.recipe_data[id][1]
        for i in range(len(self.out[1])):
            self.out[1][i][0] = self.db.get_herb_name(self.out[1][i][0])
            self.out[1][i][2] = str(self.out[1][i][2])
        self.confirm = True
        self.close()
    def reset(self):
        self.__init__()
    def select(self):
        return
