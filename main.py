import kivy
#from kivyMD.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.theming import ThemeManager


kv = Builder.load_file("my.kv")
Window.size = (360, 760) #s10+ scaled down


class HomeTab(Screen):
    pass

class WorkoutTab(Screen):
    pass

class SettingsTab(Screen):
    pass

#class WindowManager(ScreenManager):
   # pass

class Tracker(MDApp):
    def build(self):
        theme_cls = ThemeManager
        self.theme_cls.theme_style = "Dark"
        sm = ScreenManager()
        sm.add_widget(HomeTab(name='hometab'))
        sm.add_widget(WorkoutTab(name='workouttab'))
        return sm

if __name__ == "__main__":
	Tracker().run()