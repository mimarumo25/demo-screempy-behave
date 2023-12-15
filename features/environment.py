# before all
from screenpy import AnActor
from screenpy_selenium import BrowseTheWeb

from hooks.driver_manager import CustomDriver
from models.GlobalData import GlobalData


def before_all(context):
    print("hook working")
    context.actor = AnActor.named(GlobalData.actorName).who_can(BrowseTheWeb.using(CustomDriver.get_driver("chrome")))


def after_all(context):
    if hasattr(context, 'driver'):
        context.driver.quit()
        print("hook worked")
