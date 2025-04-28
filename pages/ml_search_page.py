from selenium.webdriver.common.by import By
from .base_page import BasePage

class MLSearchPage(BasePage):
    SEARCH_FIELD = (By.ID, 'cb1-edit')
    SEARCH_BUTTON = (By.CLASS_NAME, 'nav-search-btn')
    SEARCH_RESULT = (By.XPATH, '/html/body/main/div/div[2]/aside/div[1]/ol/li[3]/a/span')

    def search(self, product):
        self.enter_text(self.SEARCH_FIELD, product)
        self.click(self.SEARCH_BUTTON)

    def isElementPresent(self): 
        element = self.find_element(self.SEARCH_RESULT)
        texto = element.text
        return texto
