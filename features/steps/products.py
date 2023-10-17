from behave import step
import time
import os
from helper.pages.products_page import pageproducts
from helper.services.actions_basic import Basepage

@step(u'damos click add to cart a 3 productos')
def step_impl(context):
    Basepage.click_button(context, pageproducts.btn_add1)
    time.sleep(1)    
    Basepage.click_button(context, pageproducts.btn_add2)
    time.sleep(1)
    Basepage.click_button(context, pageproducts.btn_add3)
    time.sleep(2)

@step(u'damos click para ordernar los productos de la A a la Z')
def step_impl(context):
    Basepage.click_button(context, pageproducts.selecion)
    time.sleep(2)
    Basepage.click_button(context, pageproducts.opciones)
    time.sleep(2)

@step(u'damos click en el boton remove a 1 producto')
def step_impl(context):
    Basepage.click_button(context, pageproducts.btn_remove)
    time.sleep(2)

@step(u'Validamos que los productos se hayan agregado al carrito de compras')
def step_impl(context):
    Basepage.click_button(context, pageproducts.carrito)
    time.sleep(2)