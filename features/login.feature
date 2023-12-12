Feature: demo de behave con screenpy

  Scenario Outline: demo de behave con screenpy
    Given that the user is on the login "<url>" with "<browser>"
    When he types login data "<username>" "<password>"
    Then will see the "<text>" page
    Examples:
      | browser | url                                                   | username | password | text      |
      | chrome  | https://demo.serenity.is/Account/Login/?ReturnUrl=%2F | admin    | serenity | Dashboard |



