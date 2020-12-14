import kivy
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

kv = Builder.load_file("my.kv")

class HomeTab(Screen):
    pass

class WorkoutTab(Screen):
    pass

class SettingsTab(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class Tracker(App):
	def build(self):
		return kv

if __name__ == "__main__":
	Tracker().run()