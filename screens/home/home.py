import json

from kivy.network.urlrequest import UrlRequest
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivy.animation import Animation


class HomeScreen(Screen):

    def send_friend_request(self):
        UrlRequest(
            f"https://goblinprogrammer777.pythonanywhere.com/api/send_friend_request?user_from={self.user_id}",
            on_success=self.update_friendlist, on_failure=self.signup_FAILED)

    def on_enter(self):
        self.load_friendlist()
        self.load_friend_requests()

    def load_friend_requests(self):
        UrlRequest(f'https://goblinprogrammer777.pythonanywhere.com/api/get_friend_requests?user_to={1}',
                   on_success=self.show_friend_requests)

    def show_friend_requests(self, *args):
        friend_reqs = json.loads(args[1])
        scroll_list = self.ids.friend_requests
        for req in friend_reqs:
            item = FriendReqItem()
            scroll_list.add_widget(item)

    def load_friendlist(self):
        UrlRequest(f'https://goblinprogrammer777.pythonanywhere.com/api/get_friendlist?user_id={1}',
                   on_success=self.show_friendlist)

    def show_friendlist(self, *args):
        friends = json.loads(args[1])
        scroll_list = self.ids.friendlist
        scroll_list.clear_widgets()
        for friend in friends:
            item = FriendItem(name=friend['username'])
            scroll_list.add_widget(item)


class FriendItem(MDCard, RoundedRectangularElevationBehavior):
    id = NumericProperty()
    name = StringProperty()


class FriendReqItem(MDCard, RoundedRectangularElevationBehavior):
    id = NumericProperty()
    name = StringProperty()

    def accept(self):
        anim = Animation(x=1000, duration=0.2)
        anim.bind(on_complete=self.delete_from_db)
        anim.start(self)

    def delete_from_db(self, *args):
        self.parent.remove_widget(self)

