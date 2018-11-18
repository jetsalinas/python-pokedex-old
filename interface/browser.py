import glooey

from .browser_widgets import LeftBrowserWrapper, RightBrowserWrapper
from .widgets import Widget

class Browser(Widget):

    def __init__(self, interface):
        super().__init__()
        self.interface = interface

        self.hbox = glooey.HBox(0)
        self.hbox.add(LeftBrowserWrapper(self.interface))
        self.hbox.add(RightBrowserWrapper(self.interface))
        self._attach_child(self.hbox)
