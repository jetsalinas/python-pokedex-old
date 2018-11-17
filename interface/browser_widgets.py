import glooey
from .widgets import *

class LeftBrowser(Widget):
    custom_alignment = "left"
    custom_size_hint = 800, 900

    def __init__(self, interface):
        super().__init__()
        self.interface = interface
        self.vbox = glooey.VBox()
        self.vbox.add(glooey.Placeholder())
        self.vbox.add(glooey.Placeholder())
        self._attach_child(self.vbox)

class RightBrowser(Widget):

    custom_alignment = "center"
    custom_size_hint = 400, 900

    def __init__(self, interface):
        super().__init__() 
        self.interface = interface
        self.vbox = glooey.VBox()
        self.vbox.add(glooey.Placeholder())
        self.vbox.add(glooey.Placeholder())
        self._attach_child(self.vbox)