import pytest

from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    try:
        print("\nStart browser chrome for test...")
        driver = webdriver.Chrome()
        yield driver
        print("\nQuit browser...")
        driver.quit()
    except Exception as e:
        print(f"Error type: {type(e).__name__}"
              f"\nMessage: {e}")