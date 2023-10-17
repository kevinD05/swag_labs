Feature: Validamos agregar y eliminar productos

@carro_de_compras
Scenario: Ingresamos al modulo products
    Given Ingresamos a la url 'swag_laps'
    When damos click en el campo username y Ingresamos 'standard_user'
    And damos click en el campo password y Ingresamos 'secret_sauce'
    And damos click en el boton login
    And damos click add to cart a 3 productos 
    And damos click en el boton con forma de carro de compras
    And damos click en boton checkout
    And rellenamos el formulario
    And damos en el boton continue
    And damos click en el boton finish
    Then Validamos mensaje de exito 

    