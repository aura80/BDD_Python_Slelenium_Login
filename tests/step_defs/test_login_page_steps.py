from pytest_bdd import scenarios, when, then, given, parsers
from pages.login_page import LoginPage

# Scenarios

scenarios('../features/test_login_page.feature')

#steps
@given('open the nopcommerce homepage')
def open_page(browser):
    open = LoginPage(browser)
    open.load_page()

@when(parsers.cfparse('click on register button'))
def register_0(browser):
    open = LoginPage(browser)
    open.register0()

@when(parsers.cfparse('enter firstname "{firstname}"'))
def register_1(browser, firstname):
    open = LoginPage(browser)
    open.register1(firstname)

@when(parsers.cfparse('enter lastname "{lastname}"'))
def register_2(browser, lastname):
    open = LoginPage(browser)
    open.register2(lastname)

@when(parsers.cfparse('enter email "{email}"'))
def register_3(browser, email):
    open = LoginPage(browser)
    open.register3(email)

@when(parsers.cfparse('enter password "{password}"'))
def register_4(browser, password):
    open = LoginPage(browser)
    open.register4(password)

@when(parsers.cfparse('confirm passwordconf "{passwordconf}"'))
def register_5(browser, passwordconf):
    open = LoginPage(browser)
    open.register5(passwordconf)

@when('register on the page')
def register_6(browser):
    open = LoginPage(browser)
    open.register6()

@when('logout')
def out(browser):
    open = LoginPage(browser)
    open.logout()

@when('click on sign in button')
def click_signin(browser):
    open = LoginPage(browser)
    open.click_signin()

@when(parsers.cfparse('enter email "{email}"'))
def type_email(browser, email):
    open = LoginPage(browser)
    open.type_email(email)

@when(parsers.cfparse('enter password "{password}"'))
def type_password(browser, password):
    open = LoginPage(browser)
    open.type_password(password)

@when('click on login button')
def click_login(browser):
    open = LoginPage(browser)
    open.click_login()

@then('logout from the page')
def click_logout(browser):
    open = LoginPage(browser)
    open.click_logout()






