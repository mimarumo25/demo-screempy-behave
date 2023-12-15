from screenpy_selenium import Click, Wait, Enter

from user_interfaces.MainPage import BTN_ORGANIZATION, BTN_BUSINESS_UNIT, BTN_BUSINESS


class MeetingTask:

    def __init__(self):
        pass

    def perform_as(self, actor):
        actor.attempts_to(
            Wait.for_the(BTN_ORGANIZATION).to_appear(),
            Click.on(BTN_ORGANIZATION),
            Click.on(BTN_BUSINESS_UNIT),
            Click.on(BTN_BUSINESS),
            # Click.on(BTN_NEW_BUSINESS_UNIT),
            # Enter.the_text(name).into(TXT_BUSSINESS_NAME),
            # Click.on(TXT_PARENT_UNIT),
            # ChooseFromList.index(LST_PARENT_UNIT, 0),
            # Click.on(BTN_SAVE_UNIT)
        )

    #@staticmethod
    #def on_the_site():
    #    return MeetingTask()


def on_the_site():
    return MeetingTask()