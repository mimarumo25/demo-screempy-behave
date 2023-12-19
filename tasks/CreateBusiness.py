from screenpy_selenium import Click, Wait, Enter, Select
from faker import Faker
import pdb
from interactions.ChooseFromList import ChooseFromList
from user_interfaces.BusinessPage import TXT_BUSINESS_NAME, LST_BUSINESS_UNIT, TXT_BUSINESS_UNIT, BTN_SAVE_UNIT
from user_interfaces.MainPage import BTN_ORGANIZATION, BTN_BUSINESS_UNIT, BTN_NEW_BUSINESS


class CreateBusiness:

    def __init__(self):
        self.fake = Faker()
        self.name = self.fake.name()
        self.text = "Administration"

    def perform_as(self, actor):
        choose_from_list_instance = ChooseFromList(actor, LST_BUSINESS_UNIT, self.text)
        actor.attempts_to(
            Wait.for_the(BTN_ORGANIZATION).to_appear(),
            Click.on(BTN_ORGANIZATION),
            Wait.for_the(BTN_BUSINESS_UNIT).to_be_clickable(),
            Click.on(BTN_BUSINESS_UNIT),
            Wait.for_the(BTN_NEW_BUSINESS).to_appear(),
            Click.on(BTN_NEW_BUSINESS),
            Wait.for_the(TXT_BUSINESS_NAME).to_appear(),
            Enter.the_text(self.name).into(TXT_BUSINESS_NAME),
            Click.on(TXT_BUSINESS_UNIT),
            choose_from_list_instance.choose_from_list(),
            Click.on(BTN_SAVE_UNIT)

        )

    @staticmethod
    def on_the_site():
        return CreateBusiness()
