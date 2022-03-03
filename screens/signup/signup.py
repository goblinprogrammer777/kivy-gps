from kivy.network.urlrequest import UrlRequest
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast

class SignupScreen(Screen):
    def signup(self):
        screen = self.root.get_screen("signup")
        username = screen.ids["username_field"].text
        password = screen.ids["password_field"].text
        r = UrlRequest(f"https://goblinprogrammer777.pythonanywhere.com/signup?username={username}&password={password}",
                       on_success=self.signup_OK, on_failure=self.signup_FAILED)

    def signup_OK(self, *args):
        self.root.current = "login"
        toast("signuped!")

    def signup_FAILED(self, *args):
        toast("You writed already exsisting username ")


