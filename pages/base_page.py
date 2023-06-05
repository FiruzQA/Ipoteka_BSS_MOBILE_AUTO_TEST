from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait
from appium.webdriver.common.touch_action import TouchAction


class BasePage:
    def __init__(self, driver):
        self._driver = driver

    def open_messages(self):
        wait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "LOCATOR"))).click()

    def element_is_visible(self, locator, timeout=30):
        return wait(self._driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_are_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=10):
        return wait(self._driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        return wait(self._driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView;", element)

    def touch_action_scroll_down(self, element):
        actions = TouchAction(self._driver)
        actions.press(element).move_to(x=0, y=10).release().perform()

    def scroll_down(self):
        # Получение размеров экрана
        size = self._driver.get_window_size()
        width = size['width']
        height = size['height']
        # Определение координат прокрутки
        start_x = width // 2
        start_y = int(height * 0.5)
        end_y = int(height * 0.2)
        # Выполнение прокрутки вниз
        action = TouchAction(self._driver)
        action.press(x=start_x, y=start_y).move_to(x=start_x, y=end_y).release().perform()
