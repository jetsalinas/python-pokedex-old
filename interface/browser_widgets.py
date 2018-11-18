import glooey
import pyglet
from .widgets import *

class LeftBrowserWrapper(Widget, glooey.Frame):
    custom_alignment = "left"
    custom_size_hint = 800, 900

    def __init__(self, interface):
        super().__init__()
        self.interface = interface
        self.left_browser = LeftBrowser(self.interface)
        self.add(self.left_browser)

    class Decoration(glooey.Background):
        custom_center = pyglet.image.SolidColorImagePattern((86,185,73,255)).create_image(256, 256)

class LeftBrowser(Widget):

    def __init__(self, interface):
        super().__init__()
        self.interface = interface
        self.vbox = glooey.VBox()
        self.vbox.add(LabelWhite("Hello world"))
        self.vbox.add(glooey.Placeholder())
        self._attach_child(self.vbox)

class RightBrowserWrapper(Widget, glooey.Frame):
    custom_alignment = "center"
    custom_size_hint = 400, 900

    def __init__(self, interface):
        super().__init__()
        self.interface = interface
        self.left_browser = RightBrowser(self.interface)
        self.add(self.left_browser)

    class Decoration(glooey.Background):
        custom_center = pyglet.image.SolidColorImagePattern((255,255,255,255)).create_image(256, 256)

class RightBrowser(Widget):

    def __init__(self, interface):
        super().__init__() 
        self.interface = interface
        self.vbox = glooey.VBox()
        self.vbox.add(LabelWhite("Hello world"))
        self.vbox.add(glooey.Placeholder())
        self.vbox.add(glooey.Placeholder())
        self._attach_child(self.vbox)