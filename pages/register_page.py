import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC    # for explicit wait
from selenium.webdriver.support.wait import WebDriverWait           # for explicit wait
import random
import string

class RegisterPage:
    # URL
    URL = "https://www.reserved.com/ro/ro/customer/account/login/#register"

    # locators
    EMAIL_FIELD = (By.ID, "email_id")
    FIRSTNAME_FIELD = (By.ID, "firstname_id")
    LASTNAME_FIELD = (By.ID, "lastname_id")
    PASSWORD_FIELD = (By.ID, "password_id")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-selen='create-account-submit']")
    ACCEPT_COOKIES_BUTTON = (By.ID, 'cookiebotDialogOkButton')
    ERROR_TEXT = (By.CSS_SELECTOR, '.text-field__ErrorMessage-sc-1vll61a-4.WGIUj')


    def __init__(self, browser):        # constructor, sets the initial state of an object and it is called every time a new object is created
        self.browser = browser          # instance attributes

    # Instance Interaction methods
    def load_page(self):
        self.browser.get(self.URL)
        self.browser.find_element(*self.ACCEPT_COOKIES_BUTTON).click()

    def type_email(self, email):
        self.browser.find_element(*self.EMAIL_FIELD).send_keys(email)

    def type_firstname(self, firstname):
        self.browser.find_element(*self.FIRSTNAME_FIELD).send_keys(firstname)

    def type_lastname(self, lastname):
        self.browser.find_element(*self.LASTNAME_FIELD).send_keys(lastname)

    def type_password(self, password):
        self.browser.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_create_account_button(self):
        self.browser.find_element(*self.CREATE_ACCOUNT_BUTTON).click()
        time.sleep(15)

    def get_flash_message(self):
        return self.browser.find_element(*self.ERROR_TEXT).text

    def get_random_mail(self, mail_length):
        letters = string.ascii_lowercase + string.digits
        result_str = ''.join(random.choice(letters) for i in range(mail_length))
        e_mail = result_str + '@yahoo.com'
        self.browser.find_element(*self.EMAIL_FIELD).send_keys(e_mail)

    def get_random_string(self, length_firstname, length_lastname, length_password):
        l_firstname = string.ascii_lowercase
        result_firstname = ''.join(random.choice(l_firstname) for i in range(length_firstname))
        self.browser.find_element(*self.FIRSTNAME_FIELD).send_keys(result_firstname)

        l_lastname = string.ascii_lowercase
        result_lastname = ''.join(random.choice(l_lastname) for i in range(length_lastname))
        self.browser.find_element(*self.LASTNAME_FIELD).send_keys(result_lastname)

        l_password = string.ascii_letters + string.digits + string.punctuation
        result_password = ''.join(random.choice(l_password) for i in range(length_password))
        self.browser.find_element(*self.PASSWORD_FIELD).send_keys(result_password)

        CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-selen='create-account-submit']")
        wait = WebDriverWait(self.browser, 7)
        element = wait.until((EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)))
        element.click()

        time.sleep(2)


