import time

from selenium.webdriver.common.by import By


class LoginPage:

    #URL
    URL = "https://demo.nopcommerce.com/"

    #locators
    REGISTER_CLICK = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a')
    FIRSTNAME = (By.NAME, 'FirstName')
    LASTNAME = (By.NAME, 'LastName')
    EMAIL_REG = (By.NAME, 'Email')
    PASS_REG = (By.XPATH, '//*[@id="Password"]')
    PASS_CONFIRM = (By.XPATH, '//*[@id="ConfirmPassword"]')
    REGISTER_BUTTON = (By.XPATH, '//*[@id="register-button"]')
    LOGOUT = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a')

    LOGIN_FIRST = (By.CSS_SELECTOR, '.ico-login')
    EMAIL_FIELD = (By.NAME, 'Email')
    PASSW_FIELD = (By.NAME, 'Password')
    LOGIN_FIELD = (By.XPATH, '//button[@class="button-1 login-button"]')
    LOGOUT_FIELD = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a')



    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def register0(self):
        self.browser.find_element(*self.REGISTER_CLICK).click()

    def register1(self, firstname):
        self.browser.find_element(*self.FIRSTNAME).send_keys(firstname)

    def register2(self, lastname):
        self.browser.find_element(*self.LASTNAME).send_keys(lastname)

    def register3(self, email):
        self.browser.find_element(*self.EMAIL_REG).send_keys(email)

    def register4(self, passw):
        self.browser.find_element(*self.PASS_REG).send_keys(passw)

    def register5(self, confirm):
        self.browser.find_element(*self.PASS_CONFIRM).send_keys(confirm)

    def register6(self):
        self.browser.find_element(*self.REGISTER_BUTTON).click()

    def logout(self):
        self.browser.find_element(*self.LOGOUT).click()


    def click_signin(self):
        self.browser.find_element(*self.LOGIN_FIRST).click()

    def type_email(self, email):
        self.browser.find_element(*self.EMAIL_FIELD).send_keys(email)

    def type_password(self, password):
        self.browser.find_element(*self.PASSW_FIELD).send_keys(password)
        time.sleep(2)

    def click_login(self):
        self.browser.find_element(*self.LOGIN_FIELD).click()
        time.sleep(3)

    def click_logout(self):
        self.browser.find_element(*self.LOGOUT_FIELD).click()
