from behave import when, then

from tasks import BusinessTask


class BusinessStepDefinitions:

    def __init__(self):
        self.actor = None

    @when(u'actor creates a new unit bussiness')
    def step_impl(self):
        self.actor.attempts_to(BusinessTask.on_the_site())

    @then(u'actor will see the unit created')
    def step_impl(self, context):
        raise NotImplementedError(u'STEP: Then actor will see the unit created')
