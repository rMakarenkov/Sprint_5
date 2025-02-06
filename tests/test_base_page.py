import credentials
import locators

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestConstructor:
    def test_clickability_constructor_elements_success_operations(self, driver):
        driver.get(credentials.BASE_URL)
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(locators.FILLINGS_LINK_IN_CONSTR)).click()
        assert WebDriverWait(driver,3).until(
            ec.visibility_of_element_located(locators.LABEL_FILLINGS)).text == 'Начинки'

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(locators.SAUCES_LINK_IN_CONSTR)).click()
        assert WebDriverWait(driver,3).until(
            ec.visibility_of_element_located(locators.LABEL_SAUCES)).text == 'Соусы'

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(locators.ROLLS_LINK_IN_CONSTR)).click()
        assert WebDriverWait(driver,3).until(
            ec.visibility_of_element_located(locators.LABEL_ROLLS)).text == 'Булки'
