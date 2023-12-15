from behave import when, then
from screenpy import AnActor
from screenpy_selenium import BrowseTheWeb

from hooks import driver_manager
from hooks.driver_manager import CustomDriver
from tasks import BusinessTask


class BusinessStepDefinitions(CustomDriver):

    def __init__(self):
        self.actor = None

    @when(u'actor creates a new unit bussiness')
    def step_impl(self):
        # self.actor = AnActor.named("user").who_can(BrowseTheWeb.using(browser))
        self.actor.attempts_to(BusinessTask.on_the_site())

    @then(u'actor will see the unit created')
    def step_impl(self, context):
        raise NotImplementedError(u'STEP: Then actor will see the unit created')
