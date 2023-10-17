from selenium.webdriver.common.by import By

class pagecarro():

    btn_carro = (By.XPATH, '//a[@class="shopping_cart_link"]')
    bth_checkout = (By.XPATH, '//button[@id="checkout"]')
    btn_continue = (By.XPATH, '//input[@id="continue"]')
    btn_finish = (By.XPATH, '//button[@id="finish"]')
