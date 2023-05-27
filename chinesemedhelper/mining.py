import my_database as md

class treePoint:
    def __init__(self,name,father): #节点创建
        self.name = name
        self.num = 1
        if father:
            self.chainLen = father.chainLen+1
        else:
            self.chainLen = 0
        self.father = father
        self.children = []
        self.recipes = []
    def bornChild(self,name):   #生成孩子节点
        child = treePoint(name,self)
        self.children.append(child)
        return child
    def getChain(self): #获取节点链
        if self.name == "root":
            return []
        out = [self.name]
        return self.father.getChain()+out

class fpTree:
    def __init__(self): #起始化树
        self.root = treePoint("root",None)
        self.nodeLink = {}
    def addLink(self,name,point):   #标记节点
        self.nodeLink.setdefault(name, []).append(point)
    def add(self,inlist):   #添加链
        id = inlist["id"]
        temp = self.root
        for name in inlist["recipe"]:
            for j in temp.children:
                if j.name == name:
                    temp = j
                    temp.num+=1
                    temp.recipes.append(id)
                    break
            else:
                temp = temp.bornChild(name)
                temp.recipes.append(id)
                self.addLink(name,temp)
    def read(self,minChainLen = 0,minNum = 0): #遍历链
        output=[]
        types = self.nodeLink.keys()
        for i in types:
            pointList = self.nodeLink[i]
            for point in pointList:
                if (not minChainLen or point.chainLen >= minChainLen) and (not minNum or point.num >= minNum):
                    output.append({
                        "chain":point.getChain(),
                        "num":point.num,
                        "recipes":list(point.recipes)
                        })
        return output

def justifyData(data,minNum):
    log = {}
    newData = []
    for i in data:
        id = i[0]
        herbs = []
        for j in i[1][1]:
            herbName = j[0]
            herbs.append(herbName)
            if herbName in log.keys():
                log[herbName] += 1
            else:
                log[herbName] = 1
        newData.append({
                "id":id,
                "recipe":herbs
            })
    for i in newData:
        idx = 0
        recipe = i["recipe"]
        while idx < len(recipe):
            if log[recipe[idx]] < minNum:
                recipe.pop(idx)
            else:
                idx += 1
        i["recipe"] = sorted(recipe,key = lambda x:-log[x])
    return newData

def mineUsing_fpTree(herbMinNum = 3,chainMinLen = 2,chainMinNum = 3):
    mdb = md.herb_db('./data/meddb.json')
    mdb.update()
    recipeData = mdb.get_recipes()
    data = justifyData(recipeData,herbMinNum)
    a = fpTree()
    for i in data:
        a.add(i)
    out = a.read(chainMinLen,chainMinNum)
    out = sorted(out,key = lambda x:-x["num"])
    for i in out:
        chain = i["chain"]
        for j in range(len(chain)):
            chain[j] = mdb.get_herb_name(chain[j])
        recipes = i["recipes"]
        for j in range(len(recipes)):
            recipes[j] = mdb.data["recipe"][recipes[j]][0][0]
    return out