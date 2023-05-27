import json
import random

class Med_database:
    def __init__(self):
        f=open('./data/med.json')
        df = json.load(f)
        self.med_data = df['med']
        self.match_data = df['match']
        f.close()

    def find(self,med):
        return self.med_data.get(med)

    def show(self,med):
        if self.find(med):
            return self.med_data[med]
        return []

    def get_all_med(self):
        return list(self.med_data.keys())

    def sublist(self,list):
        rt = []
        for i in list:
            mt = self.match_data[i]
            rt.append(mt)
        return rt

    def list_all(self):
        ids = set()
        for key,values in self.med_data.items():
            ids.update(values)
        ids = list(ids)
        return self.sublist(ids)

    def log(self):
        f=open('./data/med.json','w')
        df = {'med':self.med_data,'match':self.match_data}
        json.dump(df,f)
        f.close()

    def add(self,med1,med2,int,reverse=0):
        if not self.find(med1):
            new_med = []
            self.med_data[med1] = new_med
        if not self.find(med2):
            new_med = []
            self.med_data[med2] = new_med
        if reverse:
            temp = med1
            med1 = med2
            med2 = temp
        for i in range(10000):
            self.id = "".join(random.sample('zyxwvutsrqponmlkjihgfedcba9876543210',8))
            if not self.match_data.get(self.id):
                break
        else:
            return false
        new_mt = [med1,med2,int,self.id]
        self.med_data[med1].append(self.id)
        if not med1 == med2:
            self.med_data[med2].append(self.id)
        self.match_data[self.id]=new_mt
        self.log()
        return True

    def delete(self,id):
        if self.match_data.get(id):
            med1 = self.match_data[id][0]
            med2 = self.match_data[id][1]
            self.med_data[med1].remove(id)
            if not med1 == med2:
                self.med_data[med2].remove(id)
            self.match_data.pop(id)
            self.log()
            return True
        return False

    def del_med(self,med):
        if self.find(med):
            ids = list(self.med_data[med])
            for i in ids:
                self.delete(i)
            self.med_data.pop(med)
            self.log()
            return True
        return False

    def show_med_match(self,med1,med2):
        rt = []
        mt_nums = set(self.med_data[med1]).intersection(set(self.med_data[med2]))
        return mt_nums

    def show_meds_match(self,med_list):
        id_out = set()
        id_in = set()
        for i in med_list:
            id_out.update(self.med_data[i])
        for i in range(len(med_list)-1):
            for j in range(i+1,len(med_list)):
                id_in.update(self.show_med_match(med_list[i],med_list[j]))
        id_out.difference_update(id_in)
        return [self.sublist(list(id_in)),self.sublist(list(id_out))]
