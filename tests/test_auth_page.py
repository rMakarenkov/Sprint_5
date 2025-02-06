import credentials
import locators

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestAuthorization:
    def _authenticate_base_user(self, browser):
        WebDriverWait(browser, 3).until(ec.visibility_of_element_located(locators.AUTH_PAGE_TITTLE))
        browser.find_element(*locators.INPUT_EMAIL_IN_AUTH_PAGE).send_keys(credentials.BASE_EMAIL)
        browser.find_element(*locators.INPUT_PASSWORD_IN_AUTH_PAGE).send_keys(credentials.BASE_PASSWORD)
        browser.find_element(*locators.BUTTON_LOGIN).click()


    def test_authorization_user_via_base_page_success_auth(self, driver):
        driver.get(credentials.BASE_URL)
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(locators.BUTTON_LOGIN_IN_ACC)).click()
        self._authenticate_base_user(driver)

        assert WebDriverWait(driver, 3).until(
            ec.visibility_of_element_located(locators.LABEL_COLLECT_BURGER)).text == 'Соберите бургер'

    def test_authorization_user_through_personal_account_success_auth(self, driver):
        driver.get(credentials.BASE_URL)
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(locators.BUTTON_PERS_ACC)).click()
        self._authenticate_base_user(driver)

        assert WebDriverWait(driver, 3).until(
            ec.visibility_of_element_located(locators.LABEL_COLLECT_BURGER)).text == 'Соберите бургер'

    def test_authorization_user_through_registration_page_success_auth(self, driver):
        driver.get(credentials.REGISTER_URL)
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(locators.BUTTON_LINK_LOGIN)).click()
        self._authenticate_base_user(driver)

        assert WebDriverWait(driver, 3).until(
            ec.visibility_of_element_located(locators.LABEL_COLLECT_BURGER)).text == 'Соберите бургер'

    def test_authorization_user_through_forgot_password_page_success_auth(self, driver):
        driver.get(credentials.FORG_PASSWORD_URL)
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(locators.BUTTON_LINK_LOGIN)).click()
        self._authenticate_base_user(driver)

        assert WebDriverWait(driver, 3).until(
            ec.visibility_of_element_located(locators.LABEL_COLLECT_BURGER)).text == 'Соберите бургер'
