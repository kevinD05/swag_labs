from behave import step
import time
import os
from selenium.webdriver.common.by import By

@step(u'damos click en el campo username y dejamos vacio el campo')
def step_impl(context):
    driver = context.browser
    username = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    username.click()
    time.sleep(2)

@step(u'damos click en el campo password y dejamos vacio el campo')
def step_impl(context):
    driver = context.browser
    password = driver.find_element(By.XPATH, '//input[@id="password"]')
    password.click()
    time.sleep(2)