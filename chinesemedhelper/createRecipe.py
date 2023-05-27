import json
import my_database as md

import sys
#引入pyqt5库
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QStringListModel

import createRecipe_form

tag = ["君","臣","佐","使"]
turnNum = {
    "一":1,
    "二":1,
    "三":1,
    "四":1,
    "五":1,
    "六":1,
    "七":1,
    "八":1,
    "九":1,
    "十":1,
    "半":1,
    "0":0,
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9
    }
turnUnit = {
    "分":0.5,
    "钱":5,
    "两":50,
    "斤":500,
    "合":180,
    "升":1000,
    "个":10,
    "枚":20,
    "片":1,
    "字":1,
    "条":5,
    "铢":1,
    "盏":10,
    "碗":10,
    "粒":0.15,
    "文":0.3,
    "斗":6250
    }

def fundBody(inp):
    before = "<html>\n<head>\n<link rel=\"stylesheet\" href=\"./first.css\">\n</head>\n<body>\n<table>\n"
    after = "\n</table>\n</body>\n</html>"
    return before+inp+after
def fundLine(title,content):
    if content == "":
        content = "无。"
    return "<tr>\n<th>"+title+"</th>\n<td>"+content+"</td>\n</tr>"
def getNumber(inp,name):
    rt = ""
    for i in inp:
        if i in ["0","1","2","3","4","5","6","7","8","9","."]:
            rt+=i
        else:
            if i!="克":
                rt = str(input(name+" 检测到错误："+rt+i+" 请输入对应克数"))
            return rt
    return rt
def turnNumber(inp):
    try:
        i = 2
        mode = 0
        new = ""
        offset = 0
        inp = inp.replace("g","克")
        inp = inp.replace("ml","克")
        inp = inp.replace(",","，")
        while(i<len(inp)):
            if inp[i] == "（":
                mode = 1
            elif inp[i] == "）":
                mode = 0
                if len(new):
                    inp = inp[0:i]+"，"+new[1:-1]+inp[i:]
                    i+=offset-1
                    new = ""
                    offset = 0
            elif mode and inp[i] == "，":
                inp = inp[0:i]+"、"+inp[i+1:]
            elif inp[i] == "，":
                if len(new):
                    inp = inp[0:i]+new+inp[i:]
                    i+=offset
                    new = ""
                    offset = 0
            elif inp[i] in turnUnit.keys() and inp[i-1] in turnNum.keys() and inp[i-2] != "各":
                hashead = 0
                hasTail = 0
                h = 0
                muti = 0
                while i-h-1>0 and inp[i-h-1] in turnNum.keys():
                    h += 1
                    muti += turnNum[inp[i-h]]*10**(h-1)
                base = turnUnit[inp[i]]
                temp = base*muti
                if(i+1<len(inp) and inp[i+1] == "半"):
                    temp += base/2.0
                    hasTail = 1
                new = "（"+str(temp)+"克）"
                offset = len(new)
                inp = inp[0:i-h]+inp[i+1+hasTail:]
                i-=h
                continue
            elif inp[i] == "克":
                h = 0
                while i-h-1>0 and (inp[i-h-1] in turnNum.keys() or inp[i-h-1] == "."):
                    h += 1
                if i-h-1>0 and (inp[i-h-1] == "各" or inp[i-h-1] == "千"or inp[i-h-1] == "毫"):
                    pass
                elif (i+1<len(inp) and inp[i+1] == "，") or i+1 == len(inp):
                    jup = 1
                    inp = inp[0:i+1]+"）"+inp[i+1:]
                    if i-h-1>0 and inp[i-h-1] == "）":
                        inp = inp[0:i-h-1]+"，"+inp[i-h:]
                    else:
                        inp = inp[0:i-h]+"（"+inp[i-h:]
                        jup += 1
                    i+=jup
            i+=1
        if len(new):
            inp = inp[0:i]+new+inp[i:]
            i+=offset
            new = ""
            offset = 0
        inp = inp.replace("）（","，")
        
    except:
        print("转换错误")
    return inp
            

'''
        self.name = ""
        self.provenance = ""
        self.recipe = ""
        self.cook = ""
        self.use = ""
        self.symptom = ""
        self.reason = ""
        self.ban = ""
        self.alter = ""
        return
'''

class recipe:
    def __init__(self):
        self.name = ""
        self.provenance = ""
        self.recipe = ""
        self.cook = ""
        self.use = ""
        self.symptom = ""
        self.reason = ""
        self.ban = ""
        self.alter = ""
        return
    def createHtml(self):
        self.dealReason()
        self.dealRecipe()
        if self.cook == "":
            self.cook = "水煎服。"
        content = ""
        content += fundLine("方名",self.name)
        content += fundLine("来源",self.provenance)
        content += fundLine("处方",self.recipe)
        content += fundLine("制法",self.cook)
        content += fundLine("效用",self.use)
        content += fundLine("主治",self.symptom)
        content += fundLine("方解",self.reason)
        content += fundLine("禁忌",self.ban)
        content += fundLine("增减",self.alter)
        content = fundBody(content)
        return content
    def dealRecipe(self):
        if self.recipe.find('（')!=-1:
            return
        tempList = self.recipe.split('，')
        for i in range(len(tempList)):
            tempList[i]+="（6克）"
        self.recipe = '，'.join(tempList)
    def dealReason(self):
        i = -1
        while i<len(self.reason)-2:
            i+=1
            if self.reason[i] in tag:
                if self.reason[i]=="使" and self.reason[i+1]!="药" and self.reason[i-1]!="为":
                    continue
                #self.reason = self.reason[0:i]+"<b>"+self.reason[i]+"</b>"+self.reason[i+1:]
                i += self.reason[i:].find("。")
                self.reason = self.reason[0:i+1]+"</br></br>"+self.reason[i+1:]
                i+=10
        self.reason = self.reason.replace("君药","<b>君</b>药")
        self.reason = self.reason.replace("为君","为<b>君</b>")
        self.reason = self.reason.replace("君以","<b>君</b>以")
        self.reason = self.reason.replace("君用","<b>君</b>用")
        self.reason = self.reason.replace("臣药","<b>臣</b>药")
        self.reason = self.reason.replace("为臣","为<b>臣</b>")
        self.reason = self.reason.replace("臣以","<b>臣</b>以")
        self.reason = self.reason.replace("臣用","<b>臣</b>用")
        self.reason = self.reason.replace("佐药","<b>佐</b>药")
        self.reason = self.reason.replace("为佐","为<b>佐</b>")
        self.reason = self.reason.replace("佐以","<b>佐</b>以")
        self.reason = self.reason.replace("佐用","<b>佐</b>用")
        self.reason = self.reason.replace("使药","<b>使</b>药")
        self.reason = self.reason.replace("为使","为<b>使</b>")
        self.reason = self.reason.replace("使以","<b>使</b>以")
        self.reason = self.reason.replace("使用","<b>使</b>用")
    def fundRecipeDB(self):
        rih = md.recipe_input_helper()
        rih.set_name(self.name)
        rih.set_usage(self.symptom)
        rih.set_dipose("无")
        rih.set_use(self.cook)
        temp = self.recipe.split("），")
        for i in range(len(temp)):
            temp[i] = temp[i].split("（")
            tname = temp[i][0]
            temp[i][1] = temp[i][1].split("，")
            if len(temp[i][1])==1:
                tdipose = "无"
                tcount = float(getNumber(temp[i][1][0],tname))
            else:
                tdipose = temp[i][1][0]
                tcount = float(getNumber(temp[i][1][1],tname))
            rih.add_herb(tname,tdipose,tcount)
        return rih.output()
def createRecipe(new):
    f = open("./data/learn_list.json",encoding="utf-8")
    list = json.load(f)
    htmlName = new.name+str(len(list))+".html"
    list.append({"name":new.name,"html":htmlName})
    f.close()

    f = open("./html/"+htmlName,"w+",encoding="utf-8")
    f.write(new.createHtml())
    f.close()

    db = md.herb_db('./data/meddb.json')
    db.update()
    inRecipe = new.fundRecipeDB()
    db.add_recipe(inRecipe)
    db.save()

    f = open("./data/learn_list.json","w",encoding="utf-8")
    json.dump(list,f,ensure_ascii=False)
    f.close()

class Start(QWidget, createRecipe_form.Ui_Form):
    def __init__(self):
        super(Start, self).__init__()
        self.setupUi(self)
        self.connecter()
        self.show()

        self.num = 3001

        self.load()
    def connecter(self):
        self.pushButton.clicked.connect(self.next)
        self.BJ.clicked.connect(self.jump)
    def load(self):
        try:
            root = "./inputs/data2/"
            tail = ".json"
            f = open(root+str(self.num)+tail,encoding="utf-8")
            data = json.load(f)
            f.close()
            self.name.setText(data["name"])
            self.provenance.setText(data["provenance"])
            #self.recipe.setPlainText(data["recipe"])
            self.recipe.setPlainText(turnNumber(data["recipe"]))
            self.cook.setText(data["cook"])
            self.use.setText(data["use"])
            self.symptom.setPlainText(data["symptom"])
            self.reason.setPlainText(data["reason"])
            self.ban.setPlainText(data["ban"])
            self.alter.setPlainText(data["alter"])
            pass
        except:
            print("不存在",self.num)
            self.jump()
    def next(self):
        new = recipe()
        new.name = self.name.text()
        new.provenance = self.provenance.text()
        new.recipe = self.recipe.toPlainText()
        new.cook = self.cook.text()
        new.use = self.use.text()
        new.symptom = self.symptom.toPlainText()
        new.reason = self.reason.toPlainText()
        new.ban = self.ban.toPlainText()
        new.alter = self.alter.toPlainText()
        createRecipe(new)
        self.num += 1
        print(self.num)
        self.load()
    def jump(self):
        self.num += 1
        print(self.num)
        self.load()
if __name__ == '__main__':
    argvs = sys.argv
    argvs.append('--ppapi-flash-path=./support/pepflashplayer.dll')
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(argvs)
    Start = Start()
    sys.exit(app.exec_())

'''
new = recipe()
createRecipe(new)
'''

