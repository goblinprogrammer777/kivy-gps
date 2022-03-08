from kivy.network.urlrequest import UrlRequest
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from kivymd.app import MDApp


class SignupScreen(Screen):
    def signup(self):
        screen = self.parent.get_screen("signup")
        username = screen.ids["username"].text
        password = screen.ids["password"].text
        r = UrlRequest(f"https://goblinprogrammer777.pythonanywhere.com/signup?username={username}&password={password}",
                       on_success=self.signup_success, on_failure=self.signup_fail)

    def signup_success(self, *args):
        self.parent.current = "login"
        toast("signuped!")

    def signup_fail(self, *args):
        toast("You writed already exsisting username ")
