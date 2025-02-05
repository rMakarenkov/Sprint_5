import credentials
import locators

from selenium import webdriver



def test_registration_new_user_success_operation():
    driver = webdriver.Chrome()
    driver.get(credentials.BASE_URL)
    driver.find_element(*locators.BUTTON_LOGIN_IN_ACC).click()
    driver.find_element(*locators.BUTTON_REGISTRATION).click()
    driver.find_element(*locators.REG_PAGE_TITTLE)