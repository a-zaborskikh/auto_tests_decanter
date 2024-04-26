import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class WelcomePage(Base):
    url = 'https://decanter.ru/'

    """Инициализируем атрибуты"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    popup_18_yes = '//a[@onclick="return confirm18();"]'
    main_word = '(//div[@class="tt_top_about"])[1]'
    assert_word_welcome = '(//span[@itemprop="email"])[1]'

    # Assert words
    value_assert_word_welcome = 'sales@decanter.ru'.lower()

    # Getters
    def get_value_assert_word_welcome(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.assert_word_welcome)))

    def get_popup_18_yes(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.popup_18_yes)))

    # Methods
    def enter_to_service(self):
        with allure.step('enter_to_service'):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.get_popup_18_yes().click()
            self.assert_word(self.get_value_assert_word_welcome(), self.value_assert_word_welcome)
