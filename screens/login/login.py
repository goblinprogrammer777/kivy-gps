from kivy.network.urlrequest import UrlRequest
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast


class LoginScreen(Screen):
    def login_success(self, *args):
        self.parent.current = "home"
        toast("successefuly logined!")

    def login_fail(self, *args):
        toast("incorrect username or password! will try again!")

    def login(self):
        username = self.ids["username"].text
        password = self.ids["password"].text
        if username == "":
            self.parent.current = "home"
            return
        r = UrlRequest(
            f"https://goblinprogrammer777.pythonanywhere.com/login?username={username}&password={password}",
            on_success=self.login_success, on_failure=self.login_fail)
