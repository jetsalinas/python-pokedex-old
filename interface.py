import pyglet
import glooey

class Interface():
    
    def __init__(self):
        window = pyglet.window.Window()
        gui = glooey.Gui(window)

    def start(self):
        pyglet.app.run()