import time
from selenium.webdriver.common.by import By
import re

class AddCart:
    # URL
    
    URL = "https://www.reserved.com/ro/ro/balerini-cu-funda-7439l-30x"

    ACCEPT_COOKIES_BUTTON = (By.ID, 'cookiebotDialogOkButton')
    ADD_CART = (By.CSS_SELECTOR, '.add-to-cart-text')
    NEXT_CLICK = (By.CSS_SELECTOR, '.control__ControlComponent-sc-1abuwne-0.ffTJtx.control.right-control')
    COLOR_CLICK = (By.CSS_SELECTOR, 'button[value="7439L-30X"]')


    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)
        self.browser.find_element(*self.ACCEPT_COOKIES_BUTTON).click()

    def get_sneakers(self):
        self.browser.find_element(*self.ADD_CART).click()
        time.sleep(2)

    def get_next(self):
        self.browser.find_element(*self.NEXT_CLICK)
        time.sleep(2)

    def get_color(self):
        self.browser.find_element(*self.COLOR_CLICK)
        time.sleep(2)

    def validate_mail(self, sir_validare):
        sablon = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+.[a-z]{1,3}$"
        if re.match(sablon, sir_validare):
            return True
        return False
