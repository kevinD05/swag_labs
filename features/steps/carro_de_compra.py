from behave import step
import time
import os
from helper.services.actions_basic import Basepage
from helper.pages.carro_page import pagecarro
from selenium.webdriver.common.by import By


@step(u'damos click en el boton con forma de carro de compras')
def step_impl(context):
    Basepage.click_button(context, pagecarro.btn_carro)
    time.sleep(2)


@step(u'damos click en boton checkout')
def step_impl(context):
    Basepage.click_button(context, pagecarro.bth_checkout)
    time.sleep(2)


@step(u'rellenamos el formulario')
def step_impl(context):
    driver = context.browser
    name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
    name.click()
    name.send_keys('kevin')
    time.sleep(2)
    last_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')
    last_name.click()
    last_name.send_keys('Diaz')
    time.sleep(1)
    zip_code = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
    zip_code.click()
    zip_code.send_keys(10080)
    time.sleep(2)


@step(u'damos en el boton continue')
def step_impl(context):
    Basepage.click_button(context, pagecarro.btn_continue)
    time.sleep(2)


@step(u'damos click en el boton finish')
def step_impl(context):
    driver = context.browser
    driver.execute_script('window.scrollTo(0,document.scrollHeight)')
    Basepage.click_button(context, pagecarro.btn_finish)

@step(u'Validamos mensaje de exito')
def step_impl(context):
    time.sleep(2)
