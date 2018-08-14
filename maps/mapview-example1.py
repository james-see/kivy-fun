from kivy.garden.mapview import MapView
from kivy.app import App
import geocoder
g = geocoder.ip('me')

class MapViewApp(App):
    def build(self):
        mapview = MapView(zoom=11, lat=g.latlng[0], lon=g.latlng[1])
        return mapview

MapViewApp().run()
