import credentials
import locators

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestPersonalAccount:
    def _authenticate_base_user(self, browser):
        browser.get(credentials.AUTH_URL)
        WebDriverWait(browser, 3).until(ec.visibility_of_element_located(locators.AUTH_PAGE_TITTLE))
        browser.find_element(*locators.INPUT_EMAIL_IN_AUTH_PAGE).send_keys(credentials.BASE_EMAIL)
        browser.find_element(*locators.INPUT_PASSWORD_IN_AUTH_PAGE).send_keys(credentials.BASE_PASSWORD)
        browser.find_element(*locators.BUTTON_LOGIN).click()

    def test_transition_to_the_personal_account_authorized_user_success_operation(self, driver):
        self._authenticate_base_user(driver)
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(locators.BUTTON_PERS_ACC)).click()

        assert WebDriverWait(driver, 3).until(
            ec.visibility_of_element_located(locators.BUTTON_LABEL_PROFILE)).text == 'Профиль'

    def test_transition_from_personal_account_to_constructor_success_operation(self, driver):
        self._authenticate_base_user(driver)
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(locators.BUTTON_PERS_ACC)).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(locators.BUTTON_LABEL_PROFILE))
        driver.find_element(*locators.BUTTON_LABEL_IN_HEADER_CONSTRUCT).click()

        assert WebDriverWait(driver, 3).until(
            ec.visibility_of_element_located(locators.ROLLS_LINK_IN_CONSTR)).text == 'Булки'

    def test_logout_from_personal_account_success_operation(self, driver):
        self._authenticate_base_user(driver)
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(locators.BUTTON_PERS_ACC)).click()
        WebDriverWait(driver,3).until(ec.element_to_be_clickable(locators.BUTTON_LABEL_EXIT)).click()

        assert WebDriverWait(driver, 3).until(
            ec.visibility_of_element_located(locators.AUTH_PAGE_TITTLE)).text == 'Вход'
