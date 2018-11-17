import pyglet
import glooey

from .browser import Browser

class Interface():
    
    def __init__(self, database):
        self.database = database
        self.window = pyglet.window.Window(width=1200, height=900)
        self.gui = glooey.Gui(self.window)

        self.gui.add(Browser(self))

    def start(self):
        pyglet.app.run()