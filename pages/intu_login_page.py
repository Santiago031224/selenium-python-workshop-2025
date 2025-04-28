from selenium.webdriver.common.by import By
from .base_page import BasePage

class IntuLogin(BasePage):
    USERNAME_FIELD = (By.ID, 'username')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'loginbtn')
    ERROR_MESSAGE = (By.XPATH, '/html/body/div[6]/div/div/section/div/div/div/div/div/div/div[2]/div')  # Adjust the locator as needed

    def login(self, username, password):
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
    def isElementPresent(self):
        element = self.find_element(self.ERROR_MESSAGE)
        texto = element.text
        return texto
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False