import json

from kivy.network.urlrequest import UrlRequest
from kivy.uix.screenmanager import Screen
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget, IconRightWidget, OneLineIconListItem
from kivymd.uix.tab import MDTabsBase, MDTabs
from kivymd.uix.textfield import MDTextField


class Tab(MDFloatLayout, MDTabsBase):
    pass


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
            item = OneLineAvatarIconListItem()
            item.add_widget(IconLeftWidget(icon="check"))
            item.add_widget(IconRightWidget(icon="close"))
            item.text = req["username"]
            scroll_list.add_widget(item)

    def load_friendlist(self):
        print("i_am_fish_on_the_grill")
        UrlRequest(f'https://goblinprogrammer777.pythonanywhere.com/api/get_friendlist?user_id={1}',
                   on_success=self.show_friendlist)

    def show_friendlist(self, *args):
        print(args)
        friends = json.loads(args[1])
        scroll_list = self.ids.friendlist
        scroll_list.clear_widgets()
        for friend in friends:
            item = OneLineAvatarIconListItem()
            item.add_widget(IconLeftWidget(icon="trash-can"))
            item.add_widget(IconRightWidget(icon="map-marker-radius"))
            item.text = friend["username"]
            scroll_list.add_widget(item)