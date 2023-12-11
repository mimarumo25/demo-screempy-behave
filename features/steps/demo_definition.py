from behave import given, when, then
from screenpy import AnActor
from screenpy_selenium import BrowseTheWeb, Open, Enter, Click, Wait

from tasks import LoginTask
from user_interfaces.LoginPage import THE_USERNAME_FIELD, THE_PASSWORD_FIELD, LOGIN_BUTTON
from hooks.driver_manager import CustomDriver

# Importa tus preguntas o tareas de screenpy según sea necesario


@given(u'ingresa al aplicativo demo')
def step_impl(context):
    context.actor = AnActor.named("Miguel").who_can(BrowseTheWeb.using(CustomDriver.chrome()))
    context.actor.was_able_to(Open.their_browser_on("https://demo.serenity.is/Account/Login/?ReturnUrl=%2F"))

@when(u'se ejecutan las acciones del demo "{username}" "{username}"')
def step_impl(context,username, password):
    # Puedes realizar acciones de screenpy aquí, por ejemplo:
    """context.actor.attempts_to(
        Enter.the_text("tu_usuario").into(THE_USERNAME_FIELD),
        Enter.the_text("tu_contraseña").into(THE_PASSWORD_FIELD),
        Click.on(LOGIN_BUTTON),
        # Puedes continuar con más acciones según sea necesario
    )"""
    context.actor.was_able_to(LoginTask.with_credentials(username, password).perform_as(context.actor))

@then(u'valida que el demo sea exitoso')
def step_impl(context):
    # Puedes agregar verificaciones con screenpy aquí, por ejemplo:
    context.actor.should(
        Wait.for_the(THE_PASSWORD_FIELD).to_appear(),
        # Agrega más verificaciones según sea necesario
    )

    # También puedes imprimir mensajes de éxito o fracaso según tus validaciones
    print("¡El demo fue exitoso!")

# Agrega más definiciones de pasos según sea necesario
