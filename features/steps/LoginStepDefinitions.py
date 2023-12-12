from behave import given, when, then
from screenpy import AnActor, See, ReadsExactly
from screenpy_selenium import BrowseTheWeb, Open

from models.GlobalData import GlobalData
from questions.TextOf import TextOf
from tasks.LoginTask import LoginTask
from hooks.driver_manager import CustomDriver
from user_interfaces.MainPage import THE_DASHBOARD_TITLE


class LoginStepDefinitions:

    def __init__(self, context):
        self.context = context
        self.actor = None

    @given(u'that the user is on the login "{url}" with "{browser}"')
    def step_impl(self, url, browser):
        self.actor = AnActor.named(GlobalData.actor).who_can(BrowseTheWeb.using(CustomDriver.get_driver(browser)))
        self.actor.was_able_to(Open.browser_on(url))

    @when(u'he types login data "{username}" "{password}"')
    def step_impl(self, username, password):
        self.actor.attempts_to(LoginTask.with_credentials(username, password))

    @then(u'will see the "{text}" page')
    def step_impl(self, text):
        self.actor.should(See.the(TextOf(THE_DASHBOARD_TITLE), ReadsExactly(text)))
