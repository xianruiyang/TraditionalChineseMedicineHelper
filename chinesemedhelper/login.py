import json
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import learn
#引入界面ui
import login_form

class Login(QWidget,login_form.Ui_Form):
    back_signal = pyqtSignal()
    def closeEvent(self, event):
        self.back_signal.emit()
        event.accept()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("./icon/first_background.png")))
        self.setPalette(self.palette)

        self.learn = learn.Learn()

        f = open('./data/user.json',encoding="utf-8")
        self.user_data = json.load(f)
        f.close()

        self.connecter()
    def log(self):#记录状态并进入系统
        f = open('./data/user.json','w',encoding="utf-8")
        json.dump(self.user_data,f,ensure_ascii=False)
        f.close()
        self.learn.user_name = self.IName.text()
        self.learn.welcome.setText("欢迎！"+self.learn.user_name)
        self.learn.user_data = self.user_data
        self.learn.history = self.learn.user_data[self.learn.user_id]['history']
        self.hide()
        self.learn.show()
        self.learn.back_signal.connect(self.close)

    def check(self):#检查输入正误
        if self.IName.text()=='':
            self.tip.setText("用户名为空")
            return True
        if self.IPassword.text()=='':
            self.tip.setText("密码为空")
            return True
        return False

    def regis(self):#注册
        if self.check():
            return
        for i in range(len(self.user_data)):
            if self.IName.text() == self.user_data[i].get('name'):
                self.tip.setText("该名称已被注册")
                return
        new_user = {'name':self.IName.text(), 'password':self.IPassword.text(), 'last_begin_time':time.strftime("%Y-%m-%d-%H-%M-%S"), 'history':[]}
        self.user_data.append(new_user)
        self.learn.user_id = len(self.user_data)-1
        self.log()

    def login(self):#登录
        if self.check():
            return
        for i in range(len(self.user_data)):
            if self.IName.text() == self.user_data[i].get('name'):
                if self.IPassword.text() == self.user_data[i].get('password'):
                    self.user_data[i]["last_begin_time"] = time.strftime("%Y-%m-%d-%H-%M-%S")
                    self.learn.user_id = i
                    self.log()
                    return
                else:
                    self.tip.setText("密码错误")
                    return
        self.tip.setText("用户不存在")
        
    def connecter(self):
        self.BRegis.clicked.connect(self.regis)
        self.BLogin.clicked.connect(self.login)
