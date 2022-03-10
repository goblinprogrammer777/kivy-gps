from kivy.properties import NumericProperty
from kivy.uix.screenmanager import Screen
from kivy_garden.mapview import MapView


class LocationScreen(Screen):
    latitude = NumericProperty()
    longitude = NumericProperty()
    friend_id = NumericProperty
