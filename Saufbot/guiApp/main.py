from functools import partial
import json
from kivy.app import App
from kivy.clock import mainthread
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.slider import Slider
from kivy.uix.stacklayout import StackLayout
from kivy.uix.screenmanager import ScreenManager,Screen


class MenuScreen(Screen):
    buchstabe = StringProperty('A')
    titel = StringProperty('')
    alkgehalt = StringProperty('')
    zutaten = StringProperty('')


    vorne = {'A':'B','B':'C','C':'D','D':'E','E':'F','F':'G','G':'H','H':'I','I':'J','J':'K','K':'L','L':'M','M':'N','N':'O','O':'P','P':'Q','Q':'R','R':'S','S':'T','T':'U','U':'V','V':'W','W':'X','X':'Y','Y':'Z','Z':'A'}
    zuruck = {'A':'Z','B':'A','C':'B','D':'C','E':'D','F':'E','G':'F','H':'G','I':'H','J':'I','K':'J','L':'K','M':'L','N':'M','O':'N','P':'O','Q':'P','R':'Q','S':'R','T':'S','U':'T','V':'U','W':'V','X':'W','Y':'X','Z':'Y'}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def on_button_click(self,widget):
        if widget.text == '<-':
            self.buchstabe = self.zuruck[self.buchstabe]
        elif widget.text == '->':
            self.buchstabe = self.vorne[self.buchstabe]
        DrinkStack.buildpage(self, self.buchstabe)

    def change_text(self, titel, alkgehalt, zutaten):
        self.titel = titel
        self.zutaten = zutaten
        self.alkgehalt = alkgehalt

class DrinkStack(StackLayout):
    rezepte = {}
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        list2 = list()
        with open('karte.json', 'r') as f:
            listn = json.load(f)


        search = 'A'
        for i in listn:
            if str(i).startswith(search):
                list2.append(i)
            f.close()
        for i in list2:
            self.add_widget(Button(text=str(i) ,size_hint=(1, None), on_press=partial(DrinkStack.change_content,self)))



    def buildpage(self ,value):

        self.ids.ds1.clear_widgets()
        with open('karte.json', 'r') as f:
            listn = json.load(f)
        list2 = list()

        search = value
        for i in listn:
            if str(i).startswith(search):
                list2.append(i)
        for i in list2:
            btn = Button(text=str(i),size_hint=(1, None), on_press=partial(DrinkStack.change_content,self))
            self.ids.ds1.add_widget(btn)


    def change_content(self, instance):
        with open('rezepte_.json', 'r') as f2:
            rezepte = json.load(f2)

        print(rezepte[instance.text]['AlkGehalt'])
        s = ''
        for i in container_rezepte.rezepte[instance.text]['Zutaten']:
            s += container_rezepte.rezepte[instance.text]['Zutaten'][i] + '\n'
        MenuScreen.change_text(self, titel=instance.text, alkgehalt=container_rezepte.rezepte[instance.text]['AlkGehalt'], zutaten=s)


class MixerScreen(Screen):
    pass
class LuckyScreen(Screen):
    pass
class KonfiScreen(Screen):
    pass
class ManagerScreen(Screen):
    pass
class StartScreen(Screen):
    pass

class Contaier():
    rezepte = {}
    def __init__(self):
        with open('rezepte_.json', 'r') as f:
            self.rezepte = json.load(f)
        f.close()


sm = ScreenManager()
sm.add_widget(StartScreen(name='start'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(MixerScreen(name='mixer'))
sm.add_widget(LuckyScreen(name='lucky'))
sm.add_widget(KonfiScreen(name='konfi'))
sm.add_widget(ManagerScreen(name='manager'))

class guiApp(App):
    def build(self):
        pass

if __name__ == '__main__' :
    container_rezepte = Contaier()
    guiApp().run()