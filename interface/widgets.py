import glooey

class Widget(glooey.Widget):

    def start(self):
        raise NotImplementedError

    def refresh(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

class LabelWhite(glooey.Label):
    custom_color = "#ffffff"
    custom_font_name = "8BIT WONDER"
    custom_font_size = 10

class LabelBlack(glooey.Label):
    custom_color = "#888888"
    custom_font_name = "8BIT WONDER"
    custom_font_size = 10