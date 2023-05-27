import numpy as np
import jieba

matchnum = ['单行','须','使','畏','恶','反']

def compare_str(str,list):#计算符合度
    c = 0
    for i in list:
        c+=str.count(i)
    return c

def compare_splist(str,list):#专用于配伍查询
    c = 0
    for i in list:
        c+=str[0].count(i)
        c+=str[1].count(i)
        c+=matchnum[str[2]].count(i)
    return c

def compare_strs(str,list,num = 2):
    c = 0
    for i in list:
        for j in range(num):
            c+=str[j].count(i)
    return c

def sort_list(list,inp,fun = compare_str):#关键词搜索排序
    count = []
    inp = jieba.cut(inp,cut_all = True)
    inp = '.'.join(inp)
    inp = inp.split('.')
    for i in list:
        count.append(fun(i,inp))
    return sorted(list,key = lambda x:-count[list.index(x)])

