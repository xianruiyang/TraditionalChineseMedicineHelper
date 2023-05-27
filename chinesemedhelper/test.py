import json

def turn(name):
    root = "./data/"
    tail = ".json"
    f = open(root+name+tail,"r",encoding="utf-8")
    temp = json.load(f)
    f.close()
    f = open(root+name+tail,"w",encoding="utf-8")
    json.dump(temp,f,ensure_ascii=False)
    f.close()

turn_list=["learn_list","meddb","patient","user"]
for i in turn_list:
    turn(i)

