from behave import step
import time
import os
from selenium.webdriver.common.by import By


@step(u'Ingresamos a la url \'swag_laps\'')
def step_impl(context):
    url = os.getenv('swag_laps')
    context.browser.get(url)
    time.sleep(2)

@step(u'damos click en el campo username y Ingresamos \'standard_user\'')
def step_impl(context):
    driver = context.browser
    username = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    username.click()
    username.send_keys('standard_user')
    time.sleep(2)

@step(u'damos click en el campo password y Ingresamos \'secret_sauce\'')
def step_impl(context):
    driver = context.browser
    password = driver.find_element(By.XPATH, '//input[@id="password"]')
    password.click()
    password.send_keys('secret_sauce')
    time.sleep(2)

@step(u'damos click en el boton login')
def step_impl(context):
    driver = context.browser
    btn_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    btn_login.click()
    time.sleep(2)

@step(u'Validamos que Ingresamos a la web')
def step_impl(context):
    time.sleep(2)