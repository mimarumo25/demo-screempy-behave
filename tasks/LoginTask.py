import time

from screenpy_selenium import Enter, Click, Clear, Wait

from user_interfaces.LoginPage import THE_USERNAME_FIELD, THE_PASSWORD_FIELD, LOGIN_BUTTON


class LoginTask:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def perform_as(self, actor) -> None:
        actor.attempts_to(
            Clear.the_text_from(THE_USERNAME_FIELD),
            Enter.the_text(self.username).into(THE_USERNAME_FIELD),
            Clear.the_text_from(THE_PASSWORD_FIELD),
            Enter.the_text(self.password).into(THE_PASSWORD_FIELD),
            Click.on(LOGIN_BUTTON),
            Wait.for_the("//h1").to_appear(),
            #time.sleep(600)
            # Puedes continuar con más acciones según sea necesario
        )
    @staticmethod
    def with_credentials(username, password):
        return LoginTask(username, password)
