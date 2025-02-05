from selenium.webdriver.common.by import By


# base_page
BUTTON_LOGIN_IN_ACC = (By.XPATH, '//button[text()="Войти в аккаунт"]')
LABEL_COLLECT_BURGER = (By.XPATH, '//h1[text()="Соберите бургер"]')


# auth_page
AUTH_PAGE_TITTLE = (By.XPATH, '//h2[text()="Вход"]')
BUTTON_LINK_REGISTRATION_ACC = (By.XPATH, '//a[text()="Зарегистрироваться"]')
INPUT_EMAIL_IN_AUTH_PAGE = (By.XPATH, '//*[@id="root"]//fieldset[1]/div/div/input')
INPUT_PASSWORD_IN_AUTH_PAGE = (By.XPATH, '//*[@id="root"]//fieldset[2]/div/div/input')
BUTTON_LOGIN = (By.XPATH, '//button[text()="Войти"]')

# registration_page
REG_PAGE_TITTLE = (By.XPATH, '//h2[text()="Регистрация"]')
BUTTON_REGISTRATION = (By.XPATH, '//button[text()="Зарегистрироваться"]')
INPUT_NAME_IN_REG_PAGE = (By.XPATH, '//*[@id="root"]//fieldset[1]/div/div/input')
INPUT_EMAIL_IN_REG_PAGE = (By.XPATH, '//*[@id="root"]//fieldset[2]/div/div/input')
INPUT_PASSWORD_IN_REG_PAGE = (By.XPATH, '//*[@id="root"]//fieldset[3]/div/div/input')
LABEL_INVALID_PASSWORD = (By.XPATH, '//p[text()="Некорректный пароль"]')
