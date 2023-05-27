import json
import time

import myfun as mf

from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.Qt import *
from PyQt5.QtMultimedia import *

import learn_log
#引入界面ui
import learn_form

class Learn(QWidget,learn_form.Ui_Form):
    back_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height());

        self.user_name = ''
        self.user_id = 0
        self.user_data = []
        self.history = {}
        self.learnlog = learn_log.Learn_log()
        self.isplay = False

        self.browser = QWebEngineView(self.scrollAreaWidgetContents_2)
        self.browser.setGeometry(QRect(0, 0, 709, 649))
        self.browser.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.browser.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.content.setWidget(self.scrollAreaWidgetContents_2)
        self.browser.load(QUrl(QFileInfo("./html/first.html").absoluteFilePath()))

        self.audio = QMediaPlayer(self)
        self.audio.setVolume(self.SVolume.value())
        self.video = QVideoWidget(self.scrollAreaWidgetContents_2)
        self.video.setGeometry(QRect(0, 0, 709, 605))
        self.video.setStyleSheet("background-color:grey")
        self.video.hide()
        self.audio.setVideoOutput(self.video)
        
        f = open('./data/learn_list.json',encoding='utf-8')
        self.init_list = json.load(f)
        f.close()
        self.learn_list_model = QStringListModel()
        self.learn_list_data = []
        for i in self.init_list:
            self.learn_list_data.append(i.get('name'))
        self.learn_list_model.setStringList(self.learn_list_data)
        self.learnlist.setModel(self.learn_list_model)

        self.looking = self.learn_list_data[0]

        self.connecter()

    def count_time(self):#记录学习内容以及时间
        Ntime = time.strftime("%Y-%m-%d-%H-%M-%S")
        ptime = self.user_data[self.user_id].get('last_begin_time')
        ntime = Ntime.split('-')
        ptime = ptime.split('-')
        ctime = (int(ntime[3])-int(ptime[3]))*86400+(int(ntime[3])-int(ptime[3]))*3600+(int(ntime[4])-int(ptime[4]))*60+(int(ntime[5])-int(ptime[5]))
        for i in range(len(self.history)):
            if self.history[i].get('name')==self.looking:
                self.history[i]['time']+=ctime
                self.user_data[self.user_id]['last_begin_time']=Ntime
                f = open('./data/user.json','w',encoding="utf-8")
                json.dump(self.user_data,f,ensure_ascii=False)
                f.close()
                return
        new_history = {'name':self.looking,'time':ctime}
        self.user_data[self.user_id]['history'].append(new_history)
        self.user_data[self.user_id]['last_begin_time']=Ntime
        self.history = self.user_data[self.user_id]['history']
        f = open('./data/user.json','w',encoding="utf-8")
        json.dump(self.user_data,f,ensure_ascii=False)
        f.close()
        return

    def learn_list_clicked(self,item):#切换内容
        self.count_time()
        name = self.learn_list_data[item.row()]
        self.looking = name
        for i in self.init_list:
            if i.get('name') == name:
                if i['html'][-3:]=="mp4":
                    self.switch_p(0)
                    url = "./video/"+i.get('html')
                    self.audio.setMedia(QMediaContent(QUrl.fromLocalFile(url)))
                    return
                self.switch_p(1)
                self.browser.show()
                url = "./html/"+i.get('html')
                self.browser.load(QUrl(QFileInfo(url).absoluteFilePath()))

    def find(self):
        inp = self.IFind.text()
        self.learn_list_data = mf.sort_list(self.learn_list_data,inp)
        self.learn_list_model.setStringList(self.learn_list_data)
        self.learnlist.setModel(self.learn_list_model)

    def see_log(self):
        self.hide()
        self.learnlog.initload()
        self.learnlog.exec()
        self.show()

    def closeEvent(self, event):
        self.count_time()
        self.back_signal.emit()
        event.accept()
        
    def switch_p(self,m):
        if m:
            self.BPlay.setText(">")
            self.audio.stop()
            self.video.hide()
            self.GPlays.hide()
            self.browser.show()
            self.isplay = False
            self.BPlay.setText(">")
            return
        self.video.show()
        self.GPlays.show()
        self.browser.hide()

    def cvideo(self):
        if self.isplay:
            self.BPlay.setText(">")
            self.audio.pause()
            self.isplay = False
            return
        self.BPlay.setText("||")
        self.audio.play()
        self.isplay = True

    def changevolume(self,value):
        self.audio.setVolume(value)

    def initprogress(self,d):
        self.SProgess.setRange(0,d)
        self.SProgess.setValue(0)
        self.get_time_func(d,self.TAll)
        self.get_time_func(0,self.TNow)
    
    def getprogress(self,p):
        self.SProgess.setValue(p)
        self.get_time_func(p,self.TNow)

    def changeprogress(self,v):
        self.audio.setPosition(v)
        d = self.SProgess.maximum() - v
        self.get_time_func(d,self.TNow)

    def get_time_func(self, d, label):
        seconds = int(d / 1000)
        minutes = int(seconds / 60)
        seconds -= minutes * 60
        label.setText("{:02d}:{:02d}".format(minutes,seconds))

    def connecter(self):
        self.learnlist.clicked.connect(self.learn_list_clicked)
        self.BFind.clicked.connect(self.find)
        self.BLog.clicked.connect(self.see_log)
        self.BPlay.clicked.connect(self.cvideo)
        self.SVolume.sliderMoved.connect(self.changevolume)
        self.audio.durationChanged.connect(self.initprogress)
        self.audio.positionChanged.connect(self.getprogress)
        self.SProgess.sliderMoved.connect(self.changeprogress)


