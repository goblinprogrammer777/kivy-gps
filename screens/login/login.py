from kivy.network.urlrequest import UrlRequest
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast




class LoginScreen(Screen):
    def login_OK(self, *args):
        self.parent.current = "home"
        toast("successefuly logined!")
        

    def login_FAILED(self, *args):
        toast("incorrect username or password! will try again!")

    def login(self):
        username = self.ids["username_field"].text
        password = self.ids["password_field"].text
        if username == "":
            self.parent.current = "home"
            return
        self.username = username
        r = UrlRequest(
            f"https://goblinprogrammer777.pythonanywhere.com/login?username={username}&password={password}", on_success=self.login_OK, on_failure=self.login_FAILED)
