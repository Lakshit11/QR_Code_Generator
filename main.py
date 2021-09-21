import qrcode

from kivy.app import App
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.modalview import ModalView

Builder.load_file('main.kv')

class MainScreen(Screen):
    def createcode(self,link):
        self.img = qrcode.make(link)
        self.img.show()
        self.ids.link.text = ""

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.keyboard_anim_args = {"d": 0.2, "t": "linear"}
        Window.softinput_mode = "below_target"
        Window.size = (400, 700)

    def build(self):
        self.title = 'QR Code Generator'
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()