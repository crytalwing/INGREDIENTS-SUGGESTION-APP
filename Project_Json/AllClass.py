import numpy as np
import random
import json

class BMR:
    def __init__(self, weight, height, age, gender):
        self.weight=weight
        self.height = height
        self.age = age
        self.gender = gender
    def calc_B(self):
        if self.gender==0:
            bmr = round(self.weight*13.397+10**(-2*6),2) + round(self.height*4.799+10**(-2*6),2) - round(self.age*5.677+10**(-2*6),2) + 88.36
            return int(round(bmr+10**(-2*6),0))
        elif self.gender==1:
            bmr = round(self.weight*9.247+10**(-2*6),2) + round(self.height*3.098+10**(-2*6),2) - round(self.age*4.33+10**(-2*6),2) + 447.59
            return int(round(bmr+10**(-2*6),0))
    def calc_Calorie(self,bmr,choice):
        tmp =1
        if choice == 1:
            tmp = 1.2
        elif choice == 2:
            tmp = 1.375
        elif choice == 3:
            tmp = 1.465
        elif choice == 4:
            tmp = 1.55
        elif choice == 5:
            tmp= 1.725
        elif choice == 6:
            tmp = 1.9
        return int(np.round(tmp*bmr))
    def calc_dailyCalo(self,calo,choice):
        if choice == 0:
            return int(np.ceil(calo*1.26))
        elif choice == 1:
            return calo
        elif choice == 2:
            return int(np.floor(calo*0.74))

class Current:
    def __init__(self, choice):
        self.choice = choice

class Collect:
    def __init__(self,food, calo):
        self.food = food
        self.collection =()
        self.calo = calo
    def findSubsets(self) :
        x = pow(2, len(self.food))
        tmp=[]
        for i in range(1, x) :
            if len(tmp) == 50: 
                return tuple(tmp)
            if (self.sumSubsets(self.food, i, self.calo)) != None:
                tmp.append(self.sumSubsets(self.food, i, self.calo))
        return tuple(tmp)
    def sumSubsets(self,sets, n, target) :
        tmp = []
        x = [0]*len(sets)
        j = len(sets) - 1
        while (n > 0) :
     
            x[j] = n % 2
            n = n // 2
            j -= 1
     
        toSum = 0;
 
        for i in range(len(sets)) :
            if (x[i] == 1) :
                toSum += (sets[i])["calories"]

 
        if toSum in range(target-10,target+10):
            for i in range(len(sets)):
                if (x[i] == 1):
                    tmp.append(sets[i])
            return tmp
    def collect(self):
        tmp = self.findSubsets()
        self.collection = tmp
        return tmp


class Storage:
    def __init__(self):
        self.fi = 'data.json'
        self.fo = 'rec.json'
        self.out =[]
        self.rec=[]
        self.data = {}
    def export_data(self,content):
        with open(self.fo, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False, indent=4)
    def import_data(self, file):
        with open(file) as json_file:
            tmp = json.load(json_file)
        return tmp
    def toList(self,content):
        name =[]
        for i in range(0,len(content)):
            name.append((((content)[i])["Name"],((content)[i])["calories"]))
        return name
    def Randomizer(self,content):
        if len(content) > 1:
            choice = random.randint(0,len(content)-1)
            return content[choice]
        else: return content[0]
if __name__ == "__main__" :
    new_store = Storage()
    data = new_store.import_data(new_store.fi)
    b = 1920 # calorie total
    new_collect = Collect(data["Food"],b)
    t = new_collect.collect()
    print(new_store.toList(new_store.Randomizer(t)))