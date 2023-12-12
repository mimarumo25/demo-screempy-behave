from screenpy_selenium import Text


class TextOf:

    def __init__(self, element):
        self.element = element

    @staticmethod
    def text(element):
        return TextOf(element)

    def answered_by(self, actor):
        return Text.of(self.element).answered_by(actor)
