import pyglet
import glooey

class Interface():
    
    def __init__(self, database):
        self.database = database
        self.window = pyglet.window.Window(width=1200, height=900)
        self.gui = glooey.Gui(self.window)

    def start(self):
        pyglet.app.run()