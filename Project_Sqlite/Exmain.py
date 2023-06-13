from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.core.window import Window
from AllClass import  BMR, Collect, XuLy
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np
import datetime as dtime
from kivymd.uix.list import TwoLineListItem
Window.size = (414, 736)
def get_bmr ():
    user =list(XuLy.GetUserCurrent())
    w=user[0][5]
    h=user[0][4]
    age=user[0][6]
    gender=user[0][7]
    active= user[0][8]
    if  (gender == 'male' ):
        gend=0
    else:
        gend=1
    bmr = BMR(float(w),int(h),int(age),gend)
    return bmr,int(active)

def add_weekly():
    user =list(XuLy.GetUserCurrent())
    w=user[0][5]
    h=user[0][4]
    age=user[0][6]
    gender=user[0][7]
    iduser=user[0][0]
    date= str(dtime.date.today())
    if  (gender == 'male' ):
        gend=0
    else:
        gend=1
    bmr = BMR(float(w),int(h),int(age),gend).calc_B()
    XuLy.Insert_Weekly(str(iduser),str(bmr),str(date))
    return str(bmr)

class MainScreen(Screen):
    def get_acc(self):
        item=XuLy.GetUserCurrent()
        self.ids.txtphone.text=str(item[0][1])
        self.ids.txtname.text=str(item[0][3])
        self.ids.txtweight.text=str(item[0][5])
        self.ids.txtheight.text=str(item[0][4])
        self.ids.txtage.text=str(item[0][6])
        self.ids.txtgender.text=str(item[0][7])
    def fix_acc(self):
        XuLy.Update_User(self.ids.txtphone.text,self.ids.txtname.text,self.ids.txtheight.text,self.ids.txtweight.text,self.ids.txtage.text,self.ids.txtgender.text)
    def logout(self):
        XuLy.Logout()

    def bmr_cal(self):
        bmr,active=get_bmr()
        bmr_cur=bmr.calc_B()
        calo_cur=bmr.calc_Calorie(int(bmr_cur),active)
        self.ids.bmrtext.text=str(bmr_cur)
        self.ids.calotext.text=str(calo_cur)


    def activity_level(self):
        value=self.ids.spinner_id.text
        if value == "Little or no excercise":
            XuLy.Update_Active("1")
        elif value == "Excercise 1-3 times/week":
            XuLy.Update_Active("2")
        elif value == "Excercise 4-5 times/week":
            XuLy.Update_Active("3")
        elif value == "Daily or intense excercise 3-4 times/week":
            XuLy.Update_Active("4")
        elif value == "Intense excercise 6-7 times/week":
            XuLy.Update_Active("5")
        elif value == "Very intense excercise daily or physical job":
            XuLy.Update_Active("6")

    def update (self):
        XuLy.Update_Index(self.ids.txtheight_up.text,self.ids.txtweight_up.text)
        bmr=add_weekly()
        return str(bmr)
class AccountScreen(Screen):
    def check_ac(self,phone, password):
        t=(XuLy.Check_User(str(phone),str(password)))
        if t==True:
            XuLy.Logout()
            XuLy.UserCurrent(phone,"1")
            if len(XuLy.Get_Weekly())== 0:
                bmr,active= get_bmr()
                bmr_cur=bmr.calc_B()
                idUser=(XuLy.GetUserCurrent())[0][0]
                date= str(dtime.date.today())
                XuLy.Insert_Weekly(str(idUser),str(bmr_cur),date)
        return str(t)
    def create_ac(self,n,pa,ph,w,h,a,g):
       XuLy.Insert_User(XuLy,ph,pa,n,h,w,a,g,"0","0")
    pass

class SuggestScreen(Screen):

    def gain_weight(self):
        bmr,active= get_bmr()
        bmr_cur=bmr.calc_B()
        self.ids.gaintext.text = str(bmr.calc_dailyCalo(bmr.calc_Calorie(int(bmr_cur),active),0))

        new_collect = Collect(XuLy.Get_Food(),bmr_cur)
        t = new_collect.collect()
        listitem = new_collect.Randomizer(t)
        self.ids.gaincontainer.clear_widgets()
        for food in listitem:
            name = food[0]
            cal = food[4]
            self.ids.gaincontainer.add_widget(
                TwoLineListItem(text=f"{name}",secondary_text=f"{cal} Cal") 
            )  
    
    def keep_weight(self):
        bmr,active= get_bmr()
        bmr_cur=bmr.calc_B()
        self.ids.keeptext.text = str(bmr.calc_dailyCalo(bmr.calc_Calorie(bmr_cur,active),1))
        new_collect = Collect(XuLy.Get_Food(),bmr_cur)
        t = new_collect.collect()
        listitem = new_collect.Randomizer(t)
        self.ids.keepcontainer.clear_widgets()
        for food in listitem:
            name = food[0]
            cal = food[4]
            self.ids.keepcontainer.add_widget(
                TwoLineListItem(text=f"{name}",secondary_text=f"{cal} Cal") 
            )  
    
    def loss_weight(self):
        bmr,active= get_bmr()
        bmr_cur=bmr.calc_B()
        self.ids.losstext.text = str(bmr.calc_dailyCalo(bmr.calc_Calorie(bmr_cur,active),2))
        new_collect = Collect(XuLy.Get_Food(),bmr_cur)
        t = new_collect.collect()
        listitem = new_collect.Randomizer(t)
        self.ids.losscontainer.clear_widgets()
        for food in listitem:
            name = food[0]
            cal = food[4]
            self.ids.losscontainer.add_widget(
                TwoLineListItem(text=f"{name}",secondary_text=f"{cal} Cal") 
            )  
              
class DrawPlot(MDBoxLayout):
    def __init__(self, **kwargs):
        super(DrawPlot, self).__init__(**kwargs)
        l=XuLy.Get_Chart()
        x=[]
        y=[]
        for i in range(0,len(l)):
            y.append(l[i][0])
            x.append(l[i][1])   
            plt.plot(x,y,c = '#4CAF50')
            plt.xlabel('Date')
            plt.ylabel('BMR')
            plt.grid(linestyle = '--', linewidth = 0.5)
        box=self.ids.box
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
    pass

class ExLapApp(MDApp):
    def build (self):
        sm=ScreenManager()
        sm.add_widget(AccountScreen(name='AccountScreen'))
        sm.add_widget(MainScreen(name='MainScreen'))
        sm.add_widget(SuggestScreen(name='SuggestScreen'))
        
        return sm
    pass
if __name__ == "__main__":
    XuLy.Logout()
    ExLapApp().run()