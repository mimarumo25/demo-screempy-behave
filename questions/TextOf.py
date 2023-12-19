from screenpy import Actor, See
from screenpy_selenium import Text


class TextOf:

    def __init__(self, element):
        self.element = element

    @staticmethod
    def text(element):
        return TextOf(element)

    def answered_by(self, actor: Actor) -> str:
        # return actor.uses_ability_to(See.the("Welcome message").displayed_on(Target.the("Homepage")))
        return Text.of(self.element).answered_by(actor)
