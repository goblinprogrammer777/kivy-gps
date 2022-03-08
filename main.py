from kivy.lang import Builder
from kivymd.app import MDApp
from screens.login import login
from screens.signup import signup
from screens.home import home
from screens.location import location


class MainApp(MDApp):
    def build(self):
        self.load_kv('screens/login/login.kv')
        self.load_kv('screens/signup/signup.kv')
        self.load_kv('screens/home/home.kv')
        self.load_kv('screens/location/location.kv')
        return Builder.load_file('main.kv')


MainApp().run()
