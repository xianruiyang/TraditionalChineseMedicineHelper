import json

class DB:
    def __init__(self,url = ""):
        self.data = {}
        self.url = url
        return
    def __del__(self):
        self.save_json()
    def load_json(self,url):
        self.save_json()
        f = open(url,'r')
        self.url = url
        self.data = json.load(f)
        f.close()
    def save_json(self,url = self.url):
        if url == "":
            return
        f = open(url,'w')
        json.dump(self.data,f)
        f.close()
    def add_herb(self,name):
        if name not in self.data['herb']:
            self.data['herb'][name] = []
            return True
        return False
    def del_herb(self,name):
        if name not in self.data['herb']:
            return False
