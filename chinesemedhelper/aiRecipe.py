import jieba
import numpy as np
import re
import time
import json
import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

import my_database as md
import recipe_model

class wordDict:
    def __init__(self):
        self.vo_dict = {" ":0}
        self.len = 32
    def ReBuildSentance(self,inp):
        my_inverted_dict = dict(map(reversed, self.vo_dict.items()))
        rt = ""
        for i in inp:
            rt += my_inverted_dict[i]
        return rt
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
    def UseCutSentence(self,inp):
        output = []
        for i in inp:
            if i in self.vo_dict.keys():
                output.append(self.vo_dict[i])
        if len(output)<self.len:
            for i in range(self.len-len(output)):
                output.append(0)
        if len(output)>self.len:
            output = output[0:self.len]
        return output
    def max(self):
        return len(self.vo_dict.keys())
    def save(self,url):
        with open(url,'w',encoding="utf8") as f:
            json.dump(self.vo_dict,f)
    def load(self,url):
        with open(url,'r',encoding="utf8") as f:
            self.vo_dict = json.load(f)
def get_herb_name(id,db):
    uuid = herbs[id]
    return db.get_herb_name(uuid)
            
db = md.herb_db('./model/meddb.json')
db.update()
herbs = 0
with open('./model/ai_herb_list.json','r',encoding='utf8') as f:
    herbs = json.load(f)
herb_len = len(herbs)
wd = wordDict()
wd.load("./model/ai_word_dict.json")

def aiFind(inp):
    inp = wd.UseCutSentence(inp)
    inpa = torch.tensor([[inp]])
    
    net = recipe_model.ResNet50(herb_len,wd.max())
    net.load_state_dict(torch.load('./model/recipe_resnet50V2_epoch_30.ckpt'))
    net.eval()

    outputs = net(inpa)
    for i in range(len(outputs)):
        out_list = []
        for j in range(len(outputs[i])):
            if outputs[i][j] > 0:
                outputs[i][j] = 1
                out_list.append(get_herb_name(j,db))
            else:
                outputs[i][j] = 0
    return out_list


if __name__ == "__main__":
    print(torch.cuda.get_device_name(0))
    db = md.herb_db('./model/meddb.json')
    db.update()
    herbs = 0
    with open('./model/ai_herb_list.json','r',encoding='utf8') as f:
        herbs = json.load(f)
    herb_len = len(herbs)
    wd = wordDict()
    wd.load("./model/ai_word_dict.json")

    inp = input("输入症状")
    inp = wd.UseCutSentence(inp)
    #print(inp)
    inpa = torch.tensor([[inp]])
    
    net = recipe_model.ResNet50(herb_len,wd.max())
    net.load_state_dict(torch.load('./model/recipe_resnet50V2_epoch_30.ckpt'))
    net.eval()

    outputs = net(inpa)
    for i in range(len(outputs)):
        out_list = []
        for j in range(len(outputs[i])):
            if outputs[i][j] > 0:
                outputs[i][j] = 1
                out_list.append(get_herb_name(j,db))
            else:
                outputs[i][j] = 0
        print(out_list)
        print("=====")
    
