import jieba
import numpy as np
import re
import json
import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
import torch.nn as nn

import my_database as md
import recipe_model

def FoundLoader(alist,blist):
    batch_size = 64
    num_workers = 4
    pin_memory = False
    a = torch.tensor(alist)
    b = torch.tensor(blist,dtype = torch.float32)
    dataset = TensorDataset(a,b)

    loader = torch.utils.data.DataLoader(dataset=dataset,batch_size = batch_size,shuffle=True,num_workers = num_workers,pin_memory = pin_memory)
    return loader
class wordDict:
    def __init__(self):
        self.vo_dict = {" ":0}
        self.len = 32
    def CutSentence(self,inp):
        inp = re.sub(r'[,\.，。\(\)（）、]','',inp)
        #inp = list(jieba.cut(inp))
        inp = list(inp)
        for i in range(len(inp)):
            if not inp[i] in self.vo_dict.keys():
                self.vo_dict[inp[i]] = len(self.vo_dict.keys())
            inp[i] = self.vo_dict[inp[i]]
        if len(inp)<self.len:
            for i in range(self.len-len(inp)):
                inp.append(0)
        if len(inp)>self.len:
            inp = inp[0:self.len]
        return inp
    def max(self):
        return len(self.vo_dict.keys())
    def save(self,url):
        with open(url,'w',encoding="utf8") as f:
            json.dump(self.vo_dict,f)
    def load(self,url):
        with open(url,'r',encoding="utf8") as f:
            self.vo_dict = json.load(f)
def train(net,train_loader,num_epoches,useCuda = False):
    show = 1
    criterion = nn.BCEWithLogitsLoss()
    optimizer = torch.optim.NAdam(net.parameters(),lr=1e-2)
    #optimizer = torch.optim.SGD(net.parameters(),lr=0.01,momentum=0.9)
    scaler = ""
    if useCuda:
        criterion = criterion.cuda()
        scaler = torch.cuda.amp.GradScaler()
    print("预加载完成")
    for epoch in range(num_epoches):
        train_loss = 0
        train_loss_total = 0
        log_times = 0
        for batch_idx,data in enumerate(train_loader,0):
            images,labels = data
            if useCuda:
                images = images.cuda()
                labels = labels.cuda()
                #with torch.cuda.amp.autocast():
            outputs = net(images)
            loss = criterion(outputs,labels)
            if not useCuda:
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
            else:
                scaler.scale(loss).backward()
                scaler.step(optimizer)
                scaler.update()
            train_loss += loss.item()
            train_loss_total += loss.item()
            log_times += 1
            if batch_idx%show==show-1:
                print("[%d,%5d] 损失:%.3f"%(epoch+1,batch_idx+1,train_loss/show))
                train_loss = 0
        print("[%d] 损失:%.3f"%(epoch+1,train_loss_total/(show*log_times)))
        print("保存%d代模型"%(epoch+1))
        torch.save(net.state_dict(),'./checkpoint/recipe_resnet50V2_epoch_%d.ckpt'%(epoch+1))
def get_herb_name(id,db,herb_list):
    uuid = herbs[id]
    return db.get_herb_name(uuid)
            

if __name__ == "__main__":
    print(torch.cuda.get_device_name(0))
    db = md.herb_db('./data/meddb.json')
    db.update()
    herbs = list(db.data["herb"].keys())
    with open('./data/ai_herb_list.json','w',encoding='utf8') as f:
        json.dump(herbs,f)
    herb_len = len(herbs)
    herb_list = []
    for i in range(len(herbs)):
        herb_list.append(0)
    wd = wordDict()

    recipes = list(db.data["recipe"].items())
    data = [[],[]]
    for i in recipes:
        i = i[1]
        data[0].append([wd.CutSentence(i[0][1])])
        tempList = list(herb_list)
        i = i[1]
        for j in i:
            tempList[herbs.index(j[0])] = 1
        data[1].append(tempList)
    loader = FoundLoader(data[0],data[1])
    wd.save("./data/ai_word_dict.json")

    net = recipe_model.ResNet50(herb_len,wd.max())
    net.load_state_dict(torch.load('./checkpoint/recipe_resnet50V2_epoch_30.ckpt'))
    #net = net.cuda()

    train(net,loader,50,False)
    print("end")
    
