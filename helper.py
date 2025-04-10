import credentials
import locators

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Helper:
    @staticmethod
    def authenticate_base_user(browser):
        WebDriverWait(browser, 3).until(ec.visibility_of_element_located(locators.AUTH_PAGE_TITTLE))
        browser.find_element(*locators.INPUT_EMAIL_IN_AUTH_PAGE).send_keys(credentials.BASE_EMAIL)
        browser.find_element(*locators.INPUT_PASSWORD_IN_AUTH_PAGE).send_keys(credentials.BASE_PASSWORD)
        browser.find_element(*locators.BUTTON_LOGIN).click()
