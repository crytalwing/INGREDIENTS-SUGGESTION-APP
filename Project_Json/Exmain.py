from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
import json
from kivy.core.window import Window
from AllClass import  BMR, Collect, Storage
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.anchorlayout import AnchorLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import datetime as dtime
Window.size = (414, 736)
class MainScreen(Screen):
    def get_acc(self):
        with open("data.json","r") as f:
            data=json.load(f)
        for item in data['User']:
            if (item['current'] ==1):
                self.ids.txtphone.text=item['phone']
                self.ids.txtname.text=item['name']
                self.ids.txtweight.text=str(item['weight'])
                self.ids.txtheight.text=str(item['height'])
                self.ids.txtage.text=str(item['age'])
                self.ids.txtgender.text=item['gender']
                f.close()
                return item
    def fix_acc(self):
        with open("data.json","r") as f:
            data=json.load(f)
        for item in data['User']:
            if (item['phone'] ==self.ids.txtphone.text):
                item['name']=self.ids.txtname.text
                item['weight']=int(self.ids.txtweight.text)
                item['height']=int(self.ids.txtheight.text)
                item['age']=int(self.ids.txtage.text)
                item['gender']=self.ids.txtgender.text
                with open('data.json', 'w', encoding='utf-8') as f:
                    json.dump(data,f, ensure_ascii=False, indent=4)
                f.close()
                return item
    def logout(self):
        with open("data.json","r") as f:
            data=json.load(f)
        for item in data['User']:
            if (item['current'] ==1):
                item['current']=0
                with open('data.json', 'w', encoding='utf-8') as f:
                    json.dump(data,f, ensure_ascii=False, indent=4)
                f.close()
                return item

    def bmr_cal(self):
        with open("data.json","r") as f:
            data=json.load(f)
        for item in data['User']:
            if item['current'] == 1:
                w = int(item['weight'])
                h = int(item['height'])
                age = int(item['age'])
                if item['gender'] == 'male':
                    gend = 0
                elif item['gender']=='female':
                    gend = 1
                bmr = BMR(w,h,age,gend)
                item['weekly']
                self.ids.bmrtext.text=str(bmr.calc_B())
                self.ids.calotext.text=str(bmr.calc_Calorie(bmr.calc_B(),1))
                f.close()
                return item

    def activity_level(self, value):
        self.ids.spinner_id = value
        with open("data.json","r") as f:
            data=json.load(f)
        for item in data['User']:
            if item['current'] == 1:
                if value == "Little or no excercise":
                    item['activity'] = 1
                elif value == "Excercise 1-3 times/week":
                    item['activity'] = 2
                elif value == "Excercise 1-3 times/week":
                    item['activity'] = 3
                elif value == "Excercise 1-3 times/week":
                    item['activity'] = 4
                elif value == "Excercise 1-3 times/week":
                    item['activity'] = 5
                elif value == "Excercise 1-3 times/week":
                    item['activity'] = 6
                with open('data.json', 'w', encoding='utf-8') as f:
                    json.dump(data,f, ensure_ascii=False, indent=4)
                f.close()
                return item
    def update (self,w,h):
        with open("data.json","r") as f:
            data=json.load(f)
        for item in data['User']:
            if item['current']==1:
                age=item['age']
                if item['gender'] == 'male':
                    gend = 0
                elif item['gender']=='female':
                    gend = 1
                bmr = BMR(int(w),int(h),int(age),gend)
                item['weekly'].append(bmr.calc_B())
                item['height']=int(self.ids.txtheight_up.text)
                item['weight']=int(self.ids.txtweight_up.text)
                item['date'].append(str(dtime.date.today()))

                with open('data.json', 'w', encoding='utf-8') as f:
                    json.dump(data,f, ensure_ascii=False, indent=4)
                    print(bmr)
                return str(bmr)
    def BMR_acc (self):
        with open("data.json","r") as f:
            data=json.load(f)
        for item in data['User']:
            if item['current']==1:
                age=item['age']
                w=item['weight']
                h=item['height']
                if item['gender'] == 'male':
                    gend = 0
                elif item['gender']=='female':
                    gend = 1
                bmr = BMR(int(w),int(h),int(age),gend)
                if (len((item['weekly']))==0):
                    item['weekly'].append(bmr.calc_B())
                (item['weekly'])[0]=(bmr.calc_B())
                with open('data.json', 'w', encoding='utf-8') as f:
                    json.dump(data,f, ensure_ascii=False, indent=4)
                break    
    
    pass
class AccountScreen(Screen):
    def check_ac(self,phone, password):
        with open("data.json","r") as f:
            data=json.load(f)
        for item in data['User']:
            if (item['phone'] ==phone) and (item['password'] == password):
                item['current'] =1
                w = int(item['weight'])
                h = int(item['height'])
                age = int(item['age'])
                if item['gender'] == 'male':
                    gend = 0
                elif item['gender']=='female':
                    gend = 1
                if (len(item['date'])==0):
                    item['date'].append(str(dtime.date.today()))
                if (len(item['weekly'])==0):
                    item['weekly'].append(int(BMR(w,h,age,gend).calc_B()))
                with open('data.json', 'w', encoding='utf-8') as f:
                    json.dump(data,f, ensure_ascii=False, indent=4)
                f.close()
                return 'True'
        f.close()
        return 'False'
    def create_ac(self,n,pa,ph,w,h,a,g):
        new_ac={
            "name": n,
            "password":pa,
            "phone": ph,
            "weight": int(w),
            "height": int(h),
            "age": int(a),
            "gender": g,
            "weekly": [],
            "current":0,
            "activity": 1,
            "date":[]
            }
        with open("data.json","r") as f:
            data=json.load(f)
            data['User'].append(new_ac)
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data,f, ensure_ascii=False, indent=4)
        f.close()
    pass

class SuggestScreen(Screen):

    def gain_weight(self):
        with open("data.json","r") as f:
            data=json.load(f)
        for item in data['User']:
            if item['current'] == 1:
                w = int(item['weight'])
                h = int(item['height'])
                age = int(item['age'])
                activity = int(item['activity'])
                if item['gender'] == 'male':
                    gend = 0
                elif item['gender']=='female':
                    gend = 1
                bmr = BMR(w,h,age,gend)
                Bmr = bmr.calc_B()
                self.ids.gaintext.text = str(bmr.calc_dailyCalo(bmr.calc_Calorie(Bmr,activity),0))
                f.close()
        new_store = Storage()
        new_collect = Collect(data["Food"],Bmr)
        t = new_collect.collect()
        listitem = new_store.toList(new_store.Randomizer(t))
        self.ids.gaincontainer.clear_widgets()
        for food in listitem:
            name = food[0]
            cal = food[1]
            self.ids.gaincontainer.add_widget(
                TwoLineListItem(text=f"{name}",secondary_text=f"{cal} Cal") 
            )  

    def keep_weight(self):
        with open("data.json","r") as f:
            data=json.load(f)
        for item in data['User']:
            if item['current'] == 1:
                w = int(item['weight'])
                h = int(item['height'])
                age = int(item['age'])
                activity = int(item['activity'])
                if item['gender'] == 'male':
                    gend = 0
                elif item['gender']=='female':
                    gend = 1
                bmr = BMR(w,h,age,gend)
                Bmr = bmr.calc_B()
                self.ids.keeptext.text = str(bmr.calc_dailyCalo(bmr.calc_Calorie(Bmr,activity),1))
                f.close()
        new_store = Storage()
        new_collect = Collect(data["Food"],Bmr)
        t = new_collect.collect()
        listitem = new_store.toList(new_store.Randomizer(t))
        self.ids.keepcontainer.clear_widgets()
        for food in listitem:
            name = food[0]
            cal = food[1]
            self.ids.keepcontainer.add_widget(
                TwoLineListItem(text=f"{name}",secondary_text=f"{cal} Cal") 
            )  
        

    def loss_weight(self):
        with open("data.json","r") as f:
            data=json.load(f)
        for item in data['User']:
            if item['current'] == 1:
                w = int(item['weight'])
                h = int(item['height'])
                age = int(item['age'])
                activity = int(item['activity'])
                if item['gender'] == 'male':
                    gend = 0
                elif item['gender']=='female':
                    gend = 1
                bmr = BMR(w,h,age,gend)
                Bmr = bmr.calc_B()
                self.ids.losstext.text = str(bmr.calc_dailyCalo(bmr.calc_Calorie(Bmr,activity),2))
                f.close()
                #return item
        new_store = Storage()
        new_collect = Collect(data["Food"],Bmr)
        t = new_collect.collect()
        listitem = new_store.toList(new_store.Randomizer(t))
        self.ids.losscontainer.clear_widgets()
        for food in listitem:
            name = food[0]
            cal = food[1]
            self.ids.losscontainer.add_widget(
                TwoLineListItem(text=f"{name}",secondary_text=f"{cal} Cal") 
            )  
            
class DrawPlot(AnchorLayout):
    def __init__(self, **kwargs):
        super(DrawPlot, self).__init__(**kwargs)
        with open("data.json","r") as f:
            data=json.load(f)
        for item in data['User']:
            if (item['current'] ==1):
                y=(item['weekly'])
                x=(item['date'])
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
    with open("data.json","r") as f:
        data=json.load(f)
    # for item in data['User']:
    #     if (item['current'] ==1):
    #         item['current']=0
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data,f, ensure_ascii=False, indent=4)
    f.close()
    ExLapApp().run()