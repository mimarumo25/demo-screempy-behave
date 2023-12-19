from screenpy_selenium import BrowseTheWeb, Target


class UnorderedList(Target):

    def __init__(self, element):
        self.element = element

    def resolve_for(self, actor):
        return actor.uses_ability_to(BrowseTheWeb).find_all(self.element)
