Feature: Validamos agregar y eliminar productos

@products
Scenario: Ingresamos al modulo products
    Given Ingresamos a la url 'swag_laps'
    When damos click en el campo username y Ingresamos 'standard_user'
    And damos click en el campo password y Ingresamos 'secret_sauce'
    And damos click en el boton login
    And damos click add to cart a 3 productos 
    And damos click para ordernar los productos de la A a la Z
    And damos click en el boton remove a 1 producto
    Then Validamos que los productos se hayan agregado al carrito de compras