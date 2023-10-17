from behave import step
import time
import os
from selenium.webdriver.common.by import By

@step(u'damos click en el campo username y Ingresamos \'chester\'')
def step_impl(context):
    driver = context.browser
    username = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    username.click()
    username.send_keys('chester')
    time.sleep(2)


@step(u'damos click en el campo password y Ingresamos \'12345\'')
def step_impl(context):
    driver = context.browser
    password = driver.find_element(By.XPATH, '//input[@id="password"]')
    password.click()
    password.send_keys('12345')
    time.sleep(2)


@step(u'Validamos el mensaje de error')
def step_impl(context):
    time.sleep(3)