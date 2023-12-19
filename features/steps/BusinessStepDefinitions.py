import time

from behave import when, then
from screenpy import AnActor
from screenpy_selenium import BrowseTheWeb

from hooks import driver_manager
from hooks.driver_manager import CustomDriver
from tasks import CreateBusiness
from tasks.CreateBusiness import CreateBusiness


class BusinessStepDefinitions(CustomDriver):

    def __init__(self):
        self.actor = None

    @when(u'actor creates a new unit bussiness')
    def step_impl(self):
        self.actor.attempts_to(CreateBusiness.on_the_site())
        time.sleep(10)

    @then(u'actor will see the unit created')
    def step_impl(self):
        pass
