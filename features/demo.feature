#Feature: Realizar login y crear una reunión en Serenity Demo


 # Scenario Outline: Crear una reunión en Serenity Demo
  #  Given miguel ingresa al aplicativo de Serenity Demo "<url>"
  #  And diligencia el formulario de inicio de sesion "<username>" "<password>"
  #  When el usuario completa los detalles de la reunión
   # Then la reunión debería ser creada exitosamente
   # Examples:
    #  | url                                                   | username | password |
     # | https://demo.serenity.is/Account/Login/?ReturnUrl=%2F | admin    | serenity |
Feature: demo de behave con screenpy

  Scenario Outline: demo de behave con screenpy
    Given ingresa al aplicativo demo
    When se ejecutan las acciones del demo <username> <password>
    Then valida que el demo sea exitoso
    Examples:
      | username | password |
      | admin    | serenity |

