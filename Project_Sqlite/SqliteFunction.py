import sqlite3
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
