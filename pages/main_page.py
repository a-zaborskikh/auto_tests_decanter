import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages.welcome_page import WelcomePage


class MainPage(Base):
    """Инициализируем атрибуты"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    nav_menu_whisky = '//ul[@class="head-nav__list "]/li/a[@href="/whisky"]'
    nav_menu_whisky_select_all = '(//a[@class="head-nav__btn-more"])[@href="/whisky"]'
    assert_word_nav_menu_whisky = '(//li[@class="head-nav__cat-title"])[1]'
    assert_word_nav_menu_whisky_select_all = '//div[@class="b-title__group"]/h1'

    # Assert words
    value_assert_word_nav_menu_whisky = 'Бренды'.lower()
    value_assert_word_nav_menu_whisky_select_all = 'Виски'.lower()

    # Getters
    def get_nav_menu_whisky(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.nav_menu_whisky)))

    def get_nav_menu_whisky_select_all(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.nav_menu_whisky_select_all)))

    def get_assert_word_nav_menu_whisky(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.assert_word_nav_menu_whisky)))

    def get_assert_word_nav_menu_whisky_select_all(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.assert_word_nav_menu_whisky_select_all)))

    # Actions
    def click_nav_menu_whisky(self):
        self.get_nav_menu_whisky().click()
        print('Click nav_menu_whisky')

    def click_nav_menu_whisky_all(self):
        self.get_nav_menu_whisky_select_all().click()
        print('Click nav_menu_whisky_all')

    # Methods
    def open_page_whisky_via_menu(self):
        with allure.step('open_page_whisky_via_menu'):
            self.click_nav_menu_whisky()
            self.assert_word(self.get_assert_word_nav_menu_whisky(), self.value_assert_word_nav_menu_whisky)
            self.click_nav_menu_whisky_all()
            self.get_current_url()
            self.assert_word(self.get_assert_word_nav_menu_whisky_select_all(),
                             self.value_assert_word_nav_menu_whisky_select_all)
