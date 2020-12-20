import kivy
#from kivyMD.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.theming import ThemeManager


kv = Builder.load_file("kv files/main.kv")
#Window.size = (360, 760) #s10+ scaled down
Window.size = (1440,3040)


class HomeTab(Screen):
    def changeScreen(self):
        sm = ScreenManager()
        sm.add_widget(HomeTab(name='hometab'))
        sm.add_widget(WorkoutTab(name='workouttab'))
        sm.add_widget(SettingsTab(name='settingstab'))
        sm.next()
        
        
    pass

class WorkoutTab(Screen):
    pass

class SettingsTab(Screen):
    pass


class Tracker(MDApp):
    def build(self):
        theme_cls = ThemeManager
        self.theme_cls.theme_style = "Dark"
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(HomeTab(name='hometab'))
        sm.add_widget(WorkoutTab(name='workouttab'))
        sm.add_widget(SettingsTab(name='settingstab'))
        return sm

if __name__ == "__main__":
	Tracker().run()