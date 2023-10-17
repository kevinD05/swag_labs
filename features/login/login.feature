Feature: Validamos hacer inicio de sesion

@login_successful
Scenario: Ingresamos al modulo swags labs
    Given Ingresamos a la url 'swag_laps'
    When damos click en el campo username y Ingresamos 'standard_user'
    And damos click en el campo password y Ingresamos 'secret_sauce'
    And damos click en el boton login
    Then Validamos que Ingresamos a la web 

@login_fail
Scenario: Ingresamos al modulo swags labs
    Given Ingresamos a la url 'swag_laps'
    When damos click en el campo username y Ingresamos 'chester'
    And damos click en el campo password y Ingresamos '12345'
    And damos click en el boton login
    Then Validamos el mensaje de error

@login_empty
Scenario: Ingresamos al modulo swags labs
    Given Ingresamos a la url 'swag_laps'
    When damos click en el campo username y dejamos vacio el campo
    And damos click en el campo password y dejamos vacio el campo
    And damos click en el boton login
    Then Validamos el mensaje de error
