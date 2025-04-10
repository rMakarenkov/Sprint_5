from selenium.webdriver.common.by import By


# base_page
BUTTON_LOGIN_IN_ACC = (By.XPATH, '//button[text()="Войти в аккаунт"]') # кнопка "Войти в аккаунт"
BUTTON_PERS_ACC = (By.XPATH, '//p[text()="Личный Кабинет"]') # кнопка "Личный кабинет"
BUTTON_LABEL_IN_HEADER_CONSTRUCT = (By.XPATH, '//p[text()="Конструктор"]') # пункт меню в хедере "Конструктор"
LABEL_COLLECT_BURGER = (By.XPATH, '//h1[text()="Соберите бургер"]') # заголовок "Соберите бургер"
FILLINGS_LINK_IN_CONSTR = (By.XPATH, '//span[text()="Начинки"]') # заголовок "Начинки"
LABEL_FILLINGS = (By.XPATH, '//h2[text()="Начинки"]') # подзаголовок "Начинки" в таблице
SAUCES_LINK_IN_CONSTR = (By.XPATH, '//span[text()="Соусы"]') # заголовок "Соусы"
LABEL_SAUCES = (By.XPATH, '//h2[text()="Соусы"]') # подзаголовок "Соусы" в таблице
ROLLS_LINK_IN_CONSTR = (By.XPATH, '//span[text()="Булки"]') # заголовок "Булки"
LABEL_ROLLS = (By.XPATH, '//h2[text()="Булки"]') # подзаголовок "Булки" в таблице

# auth_page
AUTH_PAGE_TITTLE = (By.XPATH, '//h2[text()="Вход"]') # заголовок страницы авторизации "Вход"
BUTTON_LINK_REGISTRATION_ACC = (By.XPATH, '//a[text()="Зарегистрироваться"]') # кнопка-ссылка "Зарегистрироваться"
INPUT_EMAIL_IN_AUTH_PAGE = (By.XPATH, '//*[@id="root"]//fieldset[1]/div/div/input') # инпут "Email"
INPUT_PASSWORD_IN_AUTH_PAGE = (By.XPATH, '//*[@id="root"]//fieldset[2]/div/div/input') # инпут "Пароль"
BUTTON_LOGIN = (By.XPATH, '//button[text()="Войти"]') # кнопка "Войти"

# registration_page
REG_PAGE_TITTLE = (By.XPATH, '//h2[text()="Регистрация"]') # заголовок "Регистрация"
BUTTON_REGISTRATION = (By.XPATH, '//button[text()="Зарегистрироваться"]') # кнопка "Зарегистрироваться"
BUTTON_LINK_LOGIN = (By.XPATH, '//a[text()="Войти"]') # кнопка-ссылка "Войти"
INPUT_NAME_IN_REG_PAGE = (By.XPATH, '//*[@id="root"]//fieldset[1]/div/div/input') # инпут "Имя"
INPUT_EMAIL_IN_REG_PAGE = (By.XPATH, '//*[@id="root"]//fieldset[2]/div/div/input') # инпут "Email"
INPUT_PASSWORD_IN_REG_PAGE = (By.XPATH, '//fieldset//input[@name="Пароль"]') # инпут "Пароль"
LABEL_INVALID_PASSWORD = (By.XPATH, '//p[text()="Некорректный пароль"]') # лейбл (сообщение) "Некорректный пароль"

# personal_account_page
BUTTON_LABEL_EXIT = (By.XPATH, '//button[text()="Выход"]') # лейбл-кнопка "Выход"
BUTTON_LABEL_PROFILE = (By.XPATH, '//a[text()="Профиль"]') # лейбл-кнопка "Профиль"
