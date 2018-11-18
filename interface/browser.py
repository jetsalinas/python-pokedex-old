import glooey

from .browser_widgets import LeftBrowser, RightBrowser
from .widgets import Widget

class Browser(Widget):

    def __init__(self, interface):
        super().__init__()
        self.interface = interface

        self.hbox = glooey.HBox(0)
        self.hbox.add(LeftBrowser(self.interface))
        self.hbox.add(RightBrowser(self.interface))
        self._attach_child(self.hbox)
