from selenium.webdriver.common.by import By


class AllLocators:
    ENTER_OK = (By.CLASS_NAME, "android.widget.Button")
    NUMBER = (By.CLASS_NAME, "android.widget.EditText")
    PASSWORD = (By.XPATH, "//android.widget.EditText[@resource-id='br_pwd']")
    LOGIN = (By.CLASS_NAME, "android.widget.Button")
    CANCEL = (By.CSS_SELECTOR, "android.widget.Button[text='Отмена']")
    SET_PIN = (By.XPATH, "//android.widget.Button[@text='Установить вход по ПИН-коду']")
    SET_PIN_MENU = (By.XPATH, "//android.view.View[@bounds='[0,1330][1080,2201]']")
    CHOOSE_SEND = (By.XPATH, "//android.widget.EditText[@resource-id='br_smart_from']")
    UZCARD_SALARY = (By.XPATH, "//android.widget.TextView[@text='UZCARD CARD SALARY']")
    UZCARD_COBAGE = (By.XPATH, "//android.widget.TextView[@text='юнион']")
    UZCARD_OTHER = (By.CSS_SELECTOR, "android.widget.TextView[text='капитал']")
    UZCARD_OFB = (By.CSS_SELECTOR, "android.widget.TextView[text='офб']")
    HUMO_SALARY = (By.CSS_SELECTOR, "android.widget.TextView[text='HUMO CARD PHYSICAL']")
    HUMO_OTHER = (By.CSS_SELECTOR, "android.widget.TextView[text='тбс']")
    HUMO_ANOR = (By.CSS_SELECTOR, "android.widget.TextView[text='анор']")
    WALLET = (By.CSS_SELECTOR, "android.widget.TextView[text='Текущий счёт']")
    CHOOSE_TAKE = (By.XPATH, "//android.widget.EditText[@resource-id='br_smart_to']")
    SUMMA = (By.XPATH, "//android.widget.EditText[@resource-id='br_trans_amount']")
    NEXT_BUTTON = (By.XPATH, "//android.widget.Button[@text='Далее']")
    CONFIRM_BUTTON = (By.XPATH, "//android.widget.Button[@text='Подтверждаю']")
    BUTTON_CLOSE = (By.XPATH, "//android.widget.Button[@text='Закрыть']")
    TAB_BAR_ISTORIYA = (By.XPATH, "//android.widget.TextView[@text='История']")