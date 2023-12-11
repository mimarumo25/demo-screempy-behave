from screenpy_selenium import Enter, Click

from user_interfaces.LoginPage import THE_USERNAME_FIELD, THE_PASSWORD_FIELD, LOGIN_BUTTON


class LoginTask:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def perform_as(self, actor) -> None:
        actor.attempts_to(
            Enter.the_text(self.username).into(THE_USERNAME_FIELD),
            Enter.the_text(self.password).into(THE_PASSWORD_FIELD),
            Click.on(LOGIN_BUTTON),
            # Puedes continuar con más acciones según sea necesario
        )
    @staticmethod
    def with_credentials(username, password):
        return LoginTask(username, password)
