from behave import given, when, then
from selenium import webdriver
from pages.ml_search_page import MLSearchPage

@given('el usuario se encuenta en la pagina principal de mercado libre')
def step_given_ml_search(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.mercadolibre.com.co/')
    context.ml_search_page = MLSearchPage(context.driver)
@when('el usuario escribe articulo a buscar')
def step_when_ml_seacrh(context):
    context.ml_search_page.search('Iphone 13')

@then('aparece el articulo buscado')
def step_then_ml_search(context): 
    assert "Iphone" in context.ml_search_page.isElementPresent()