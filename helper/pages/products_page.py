from selenium.webdriver.common.by import By

class pageproducts():

    btn_add1 = (By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
    btn_add2 = (By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]')
    btn_add3 = (By.XPATH, '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    selecion = (By.XPATH, '//span[@class="active_option"]')
    opciones = (By.XPATH, '//option[@value="az"]')
    btn_remove = (By.XPATH, '//button[@class="btn btn_secondary btn_small btn_inventory"]')
    carrito = (By.XPATH, '//a[@class="shopping_cart_link"]')