import glooey

class Widget(glooey.Widget):

    def start(self):
        raise NotImplementedError

    def refresh(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError