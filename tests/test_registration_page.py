import credentials
import locators

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration:

    def test_registration_new_user_success_operation(self, driver, generate_email_and_password):
        driver.get(credentials.BASE_URL)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.BUTTON_LOGIN_IN_ACC)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.BUTTON_LINK_REGISTRATION_ACC)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.REG_PAGE_TITTLE))
        driver.find_element(*locators.INPUT_NAME_IN_REG_PAGE).send_keys(credentials.BASE_NAME)
        driver.find_element(*locators.INPUT_EMAIL_IN_REG_PAGE).send_keys(generate_email_and_password.get('email'))
        driver.find_element(*locators.INPUT_PASSWORD_IN_REG_PAGE).send_keys(generate_email_and_password.get('password'))
        driver.find_element(*locators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.AUTH_PAGE_TITTLE))
        driver.find_element(*locators.INPUT_EMAIL_IN_AUTH_PAGE).send_keys(credentials.BASE_EMAIL)
        driver.find_element(*locators.INPUT_PASSWORD_IN_AUTH_PAGE).send_keys(credentials.BASE_PASSWORD)
        driver.find_element(*locators.BUTTON_LOGIN).click()

        text_after_login = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(locators.LABEL_COLLECT_BURGER)).text

        assert text_after_login == 'Соберите бургер'


    def test_registration_new_user_invalid_password_failed_operation(self, driver, generate_email_and_password):
        driver.get(credentials.BASE_URL)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.BUTTON_LOGIN_IN_ACC)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.BUTTON_LINK_REGISTRATION_ACC)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.REG_PAGE_TITTLE))
        driver.find_element(*locators.INPUT_NAME_IN_REG_PAGE).send_keys(credentials.BASE_NAME)
        driver.find_element(*locators.INPUT_EMAIL_IN_REG_PAGE).send_keys(generate_email_and_password.get('email'))
        driver.find_element(*locators.INPUT_PASSWORD_IN_REG_PAGE).send_keys('123Qw')
        driver.find_element(*locators.BUTTON_REGISTRATION).click()

        message = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(locators.LABEL_INVALID_PASSWORD)).text

        assert message == 'Некорректный пароль'