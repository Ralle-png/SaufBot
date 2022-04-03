from kivy.app import App
import json
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




# class TestButton (Button):
#     def __init__(self,**kwargs):
#         super(TestButton, self).__init__(**kwargs)
class MenuScreen(Screen):
    buchstabe = StringProperty('A')
    vorne = {'A':'B','B':'C','C':'D','D':'E','E':'F','F':'G','G':'H','H':'I','I':'J','J':'K','K':'L','L':'M','M':'N','N':'O','O':'P','P':'Q','Q':'R','R':'S','S':'T','T':'U','U':'V','V':'W','W':'X','X':'Y','Y':'Z','Z':'A'}
    zuruck = {'A':'Z','B':'A','C':'B','D':'C','E':'D','F':'E','G':'F','H':'G','I':'H','J':'I','K':'J','L':'K','M':'L','N':'M','O':'N','P':'O','Q':'P','R':'Q','S':'R','T':'S','U':'T','V':'U','W':'V','X':'W','Y':'X','Z':'Y'}

    def on_button_click(self,widget):
        if widget.text == '<-':
            self.buchstabe = self.zuruck[self.buchstabe]
        elif widget.text == '->':
            self.buchstabe = self.vorne[self.buchstabe]

        DrinkStack.buildpage(self, self.buchstabe)





class DrinkStack(StackLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)



    def buildpage(self, value):
        with open('karte.json', 'r') as f:
            listn = json.load(f)
        list2 = list()

        search = value
        for i in listn:
            if str(i).startswith(search):
                list2.append(i)
        for i in list2:
            self.add_widget(Button(text=str(i), size_hint=(1, None)))


    def nextpage(self):
        pass



class ScreenManager(Screen):
    def __init__(self, **kwargs):
        super(ScreenManager, self).__init__(**kwargs)

class StartScreen(Screen):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
class MixerScreen(Screen):
    pass
class LuckyScreen(Screen):
    pass
class KonfiScreen(Screen):
    pass
class ManagerScreen(Screen):
    pass

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
    ds = DrinkStack()
    guiApp().run()