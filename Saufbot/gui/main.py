from kivy.app import App
import json
from kivy.metrics import dp
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
class DrinkStack(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with open('rezepte_.json', 'r') as f:
            list1 = json.load(f)
        k = 0
        for i in list1:
            k += 1
            if k <= 10:
                self.add_widget(Button(text=str(i), size_hint=(1, None)))
            else:
                continue

    def on_button_click(self):
        
        pass


class ScreenManager(Screen):
    def __init__(self, **kwargs):
        super(ScreenManager, self).__init__(**kwargs)

class StartScreen(Screen):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

class MenuScreen(Screen):
    pass
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

class Interfaze(App):
    def build(self):
        pass

if __name__ == '__main__' :
    Interfaze().run()