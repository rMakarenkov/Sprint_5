import pytest
import string
import random

from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    except Exception as e:
        print(f"Error type: {type(e).__name__}")


@pytest.fixture(scope="function")
def generate_email_and_password() -> dict:
    characters = string.ascii_letters + string.digits + string.punctuation
    name_and_password = {
        'email': ''.join(random.choice(characters) for _ in range(6)) + '@gmail.com',
        'password': ''.join(random.choice(characters) for _ in range(6))
    }
    return name_and_password
