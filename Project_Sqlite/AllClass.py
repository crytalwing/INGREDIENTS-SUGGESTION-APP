from sympy import public
import numpy as np
import random
import random
from kivy.app import App
import json
import sqlite3
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
     
        toSum = 0
 
        for i in range(len(sets)) :
            if (x[i] == 1) :
                toSum += (sets[i])[4]

 
        if toSum in range(target-10,target+10):
            for i in range(len(sets)):
                if (x[i] == 1):
                    tmp.append(sets[i])
            return tmp
    def collect(self):
        tmp = self.findSubsets()
        self.collection = tmp
        return tmp
    def Randomizer(self,content):
        if len(content) > 1:
            choice = random.randint(0,len(content))
            return content[choice]
        else: return content[0]
   
class XuLy:
    def Check_Phone(Phone):
        conn = sqlite3.connect('APP.db')
        cursor = conn.cursor()
        query = "select * from Users where Phone = '"+Phone+"' "
        a=cursor.execute(query).fetchall()
        if len(a)<=0:
            return False
        else:
            return True
    def Insert_User(self,Phone, Password, NameUser, Height, Weights, Age, Gender,Active,Currents):
        conn = sqlite3.connect('APP.db')
        cursor = conn.cursor()
        if self.Check_Phone(Phone) == False:
            query = "Insert into Users(Phone, Passwords, NameUser, Height, Weights, Age, Gender, Active, Currents) Values('" + Phone + "','" +  Password + "','" + NameUser + "'," + Height + "," + Weights + "," +  Age + ",' " +  Gender + "'," + Active + "," + Currents +")"
            cursor.execute(query)
            conn.commit()
        else:
            return False

    def Update_User(Phone, NameUser, Height, Weights, Age, Gender):
        conn = sqlite3.connect('APP.db')
        cursor = conn.cursor()
        query = "Update Users SET Phone ='" + Phone + "',"+"NameUser = '" + NameUser + "'," + "Height = " + Height + "," + "Weights = " + Weights + "," + "Age = " + Age + ", Gender = '" + Gender +"'" + "Where Currents=1" 
        cursor.execute(query)
        conn.commit()
    def Update_Index(Height, Weights):
        conn = sqlite3.connect('APP.db')
        cursor = conn.cursor()
        query = "Update Users SET Height = " + Height + "," + "Weights = " + Weights + " Where Currents=1" 
        cursor.execute(query)
        conn.commit()
    def Check_User(Phone, Password):
        conn = sqlite3.connect('APP.db')
        cursor = conn.cursor()
        query = "select * from Users where Phone = '"+Phone+"' and Passwords = '"+ Password +"' "
        a=cursor.execute(query).fetchall()
        if len(a)<=0:
            return False
        else:
            return True
    def UserCurrent(Phone,cur):
        conn = sqlite3.connect('APP.db')
        cursor = conn.cursor()
        query = "Update Users SET Currents='"+cur+"' where Phone='"+Phone+"'" 
        cursor.execute(query).fetchall()
        conn.commit()
    def GetUserCurrent():
        conn = sqlite3.connect('APP.db')
        cursor = conn.cursor()
        query = "select * from Users where currents = 1" 
        a=cursor.execute(query).fetchall()
        conn.commit()	
        return a	
    def Logout():
        conn = sqlite3.connect('APP.db')
        cursor = conn.cursor()
        query = "Update Users SET Currents=0 where Currents=1" 
        a=cursor.execute(query).fetchall()
        conn.commit()
    def Get_Phone():
        conn = sqlite3.connect('APP.db')
        cursor = conn.cursor()
        query= "select Phone from Users Where Currents=1"
        cursor.execute(query).fetchall()
    def Insert_Weekly(IdUser, Bmr, TimeUpdate):
        conn = sqlite3.connect('APP.db')
        cursor = conn.cursor()
        query = "Insert into Weekly(IdUser, Bmr, TimeUpdate) Values('" + IdUser + "','" +  Bmr + "','" + TimeUpdate + "')"
        cursor.execute(query)
        conn.commit()
    def Update_Active(active):
        conn = sqlite3.connect('APP.db')
        cursor = conn.cursor()
        query = "Update Users SET Active = " + active + " Where Currents = 1"
        cursor.execute(query)
        conn.commit()
    def Get_Weekly():
        conn = sqlite3.connect('APP.db')
        cursor = conn.cursor()
        query = "select * from Weekly,Users where Weekly.IdUser = Users.IdUser and Users.Currents=1 " 
        a=cursor.execute(query).fetchall()
        conn.commit()	
        return a
    def Get_Chart():
        conn = sqlite3.connect('APP.db')
        cursor = conn.cursor()
        query = "select Weekly.Bmr,Weekly.TimeUpdate from Weekly,Users where Weekly.IdUser = Users.IdUser and Users.Currents=1 " 
        a=cursor.execute(query).fetchall()
        conn.commit()	
        return a
    def Get_Food ():
        conn = sqlite3.connect('APP.db')
        cursor = conn.cursor()
        query = "select * from Foods" 
        a=cursor.execute(query).fetchall()
        return a

if __name__ == "__main__" :  
    data = XuLy.Get_Food()
    b = 1920 # calorie total
    new_collect = Collect(data,b)

    # new_collect = Collect(data["Food"],b)
    t = new_collect.collect()
    print(new_collect.Randomizer(t))