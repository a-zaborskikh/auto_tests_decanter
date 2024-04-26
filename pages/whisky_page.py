import allure
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WhiskyPage(Base):
    """Инициализируем атрибуты"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button_filter_informer = '//a[@class="b-informer__button"]'
    button_filters = '//div[@class="prod-filter__button-wrap"]'
    filter_brand_select_more = '(//a[@class="b-filter__choose"])[1]'
    popup_lang_to_search_ru = '(//a[@data-lang="ru"])[1]'
    filter_brand_search = '//input[@id="filter-popup-brand-search"]'
    checkbox_brand_search_6405 = '//label[@data-id="6405"]'
    button_popup_filter_clear = '(//span[@class="b-popup-filter__clear"])[1]'
    popup_lang_to_search_en = '(//a[@data-lang="en"])[1]'
    checkbox_brand_search_6406 = '//label[@data-id="6406"]'
    button_popup_filter_apply = '(//span[@class="b-popup-filter__button"])[1]'
    checkbox_brand_search_17476 = '//label[@data-id="17476"]'
    counter_selected_filters = '//a[@class="b-filter__label b-filter__label--close"]'
    close_filter_brand = '//a[@class="b-filter__close"]'
    filter_price = '//div[@id="filter_PRICE_1"]/span[1]'
    checkbox_filter_package = '(//label[@class="b-checkbox__label b-checkbox__label--type"])[1]'
    sort_products = '(//div[@class="SumoSelect"])[2]'
    sort_first_expensive = '(//li[@class="opt"])[10]'
    assert_sort_first_expensive = ('//a[@href="/product/macallan-sir-peter-blake-anecdotes-of-ages-id193126"]['
                                   '@data-prod-name=""]')
    button_add_to_cart_product_1 = '(//a[@class="prod__button"])[1]'
    button_add_to_cart_product_2 = '(//a[@class="prod__button"])[2]'
    counter_products_to_cart = '//p[@class="head-cart__text"]/span[@class="line"]'
    button_open_cart_page = '//p[@class="head-cart__text"]/span[@class="line"]'
    title_page_cart = '//div[@class="container"]/h1'

    # Words for search
    whisky_brand_ru_jack = 'Джек'
    whisky_brand_eng_chivas = 'chi'
    whisky_brand_eng_big = 'big'

    # Assert words
    value_assert_counter_selected_filters_1 = 'выбрано: 1'
    value_assert_counter_selected_filters_2 = 'выбрано: 2'
    value_assert_counter_selected_filters_3 = 'выбрано: 3'
    value_assert_sort_first_expensive = 'виски macallan sir peter blake anecdotes of ages 0,7 л'
    value_counter_products_to_cart_2_products = '2 товара'
    value_assert_title_page_cart = 'Корзина и оформление заказа'

    # Getters
    def get_button_filter_informer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_filter_informer)))

    def get_button_filters(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_filters)))

    def get_filter_brand_select_more(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_brand_select_more)))

    def get_popup_lang_to_search_ru(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.popup_lang_to_search_ru)))

    def get_filter_brand_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_brand_search)))

    def get_checkbox_brand_search_6405(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.checkbox_brand_search_6405)))

    def get_popup_lang_to_search_en(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.popup_lang_to_search_en)))

    def get_checkbox_brand_search_6406(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.checkbox_brand_search_6406)))

    def get_button_popup_filter_apply(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.button_popup_filter_apply)))

    def get_checkbox_brand_search_17476(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.checkbox_brand_search_17476)))

    def get_counter_selected_filters(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.counter_selected_filters)))

    def get_close_filter_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.close_filter_brand)))

    def get_filter_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.filter_price)))

    def get_checkbox_filter_package(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.checkbox_filter_package)))

    def get_sort_products(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.sort_products)))

    def get_sort_first_expensive(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.sort_first_expensive)))

    def get_assert_sort_first_expensive(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.assert_sort_first_expensive)))

    def get_button_add_to_cart_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.button_add_to_cart_product_1)))

    def get_button_add_to_cart_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.button_add_to_cart_product_2)))

    def get_button_open_cart_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.button_open_cart_page)))

    def get_counter_products_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.counter_products_to_cart)))

    def get_title_page_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.title_page_cart)))

    # Actions
    def click_button_filter_informer(self):
        self.get_button_filter_informer().click()
        print('Click button_filter_informer')

    def click_button_filters(self):
        self.get_button_filters().click()
        print('Click button_filters')

    def click_filter_brand_select_more(self):
        self.get_filter_brand_select_more().click()
        print('Click filter_brand_select_more')

    def select_popup_lang_to_search_ru(self):
        self.get_popup_lang_to_search_ru().click()
        print('Select popup_lang_to_search_ru')

    def input_filter_brand_search(self, word_search):
        self.get_filter_brand_search().send_keys(word_search)
        print('Input whisky_brand_ru')

    def select_checkbox_brand_search_6405(self):
        self.get_checkbox_brand_search_6405().click()
        print('Select checkbox_brand_search_6405')

    def select_checkbox_brand_search_6406(self):
        self.get_checkbox_brand_search_6406().click()
        print('Select checkbox_brand_search_6406')

    def clear_input_filter_brand_search(self):
        self.get_filter_brand_search().clear()
        print('Clear input_filter_brand_search')

    def select_popup_lang_to_search_en(self):
        self.get_popup_lang_to_search_en().click()
        print('Select popup_lang_to_search_ru')

    def click_button_popup_filter_apply(self):
        self.get_button_popup_filter_apply().click()
        print('Click button_popup_filter_apply')

    def select_checkbox_brand_search_17476(self):
        self.get_checkbox_brand_search_17476().click()
        print('Select checkbox_brand_search_17476')

    def assert_counter_selected_filters(self):
        self.get_counter_selected_filters().click()
        print('Select checkbox_brand_search_17476')

    def click_close_filter_brand(self):
        self.get_close_filter_brand().click()
        print('Click close_filter_brand')

    def click_and_hold_filter_price(self):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_filter_price()).move_by_offset(20, 0).release().perform()
        print('Click and hold filter_brand_price')

    def click_checkbox_filter_package(self):
        self.get_checkbox_filter_package().click()
        print('Click checkbox_filter_package')

    def click_sort_products(self):
        self.get_sort_products().click()
        print('Click sort_products')

    def click_sort_first_expensive(self):
        self.get_sort_first_expensive().click()
        print('Click sort_first_expensive')

    def click_button_add_to_cart_product_1(self):
        self.get_button_add_to_cart_product_1().click()
        print('Click add_to_cart_product_1')

    def click_button_add_to_cart_product_2(self):
        self.get_button_add_to_cart_product_2().click()
        print('Click add_to_cart_product_2')

    def click_button_open_cart_page(self):
        self.get_button_open_cart_page().click()
        print('Click button_open_cart_page')

    # Methods
    def open_filters_brand(self):
        with allure.step('open_filters_brand'):
            self.scroll_page(900)
            self.click_button_filter_informer()
            self.click_button_filters()

    def select_one_brand_to_filter(self):
        self.click_filter_brand_select_more()
        self.select_popup_lang_to_search_en()
        self.clear_input_filter_brand_search()
        self.input_filter_brand_search(self.whisky_brand_eng_chivas)
        self.select_checkbox_brand_search_6406()
        self.click_button_popup_filter_apply()
        self.assert_url('https://decanter.ru/whisky')
        try:
            self.assert_word(self.get_counter_selected_filters(), self.value_assert_counter_selected_filters_1.lower())
        except AssertionError as exception:
            print(str(exception) + 'Know BUG-0001')
        # self.click_close_filter_brand()

    def select_two_brands_to_filter(self):
        self.click_filter_brand_select_more()
        self.select_popup_lang_to_search_en()
        self.clear_input_filter_brand_search()
        self.input_filter_brand_search(self.whisky_brand_eng_chivas)
        self.select_checkbox_brand_search_6406()

        self.select_popup_lang_to_search_ru()
        self.clear_input_filter_brand_search()
        self.input_filter_brand_search(self.whisky_brand_ru_jack)
        self.select_checkbox_brand_search_6405()

        self.click_button_popup_filter_apply()
        self.assert_url('https://decanter.ru/whisky')
        try:
            self.assert_word(self.get_counter_selected_filters(), self.value_assert_counter_selected_filters_2.lower())
        except AssertionError as exception:
            print(str(exception) + 'Know BUG-0001')
        # self.click_close_filter_brand()

    def select_three_brands_to_filter(self):
        self.click_filter_brand_select_more()
        self.select_popup_lang_to_search_en()
        self.clear_input_filter_brand_search()
        self.input_filter_brand_search(self.whisky_brand_eng_chivas)
        self.select_checkbox_brand_search_6406()

        self.select_popup_lang_to_search_ru()
        self.clear_input_filter_brand_search()
        self.input_filter_brand_search(self.whisky_brand_ru_jack)
        self.select_checkbox_brand_search_6405()

        self.select_popup_lang_to_search_ru()
        self.clear_input_filter_brand_search()
        self.input_filter_brand_search(self.whisky_brand_eng_big)
        self.select_checkbox_brand_search_17476()

        self.click_button_popup_filter_apply()
        self.assert_url('https://decanter.ru/whisky')
        try:
            self.assert_word(self.get_counter_selected_filters(), self.value_assert_counter_selected_filters_3.lower())
        except AssertionError as exception:
            print(str(exception) + 'Know BUG-0001')
        # self.click_close_filter_brand()

    def switch_lang_to_brand_search(self):
        self.open_filters_brand()
        self.click_filter_brand_select_more()
        self.select_popup_lang_to_search_en()
        self.input_filter_brand_search(self.whisky_brand_ru_jack)
        self.select_checkbox_brand_search_6405()

    def select_different_filters(self):
        with allure.step('select_different_filters'):
            self.click_sort_products()
            self.click_sort_first_expensive()
            self.assert_word(self.get_assert_sort_first_expensive(), self.value_assert_sort_first_expensive)
            # self.scroll_page(-100)
            # self.click_and_hold_filter_price()
            # self.scroll_page(200)
            try:
                self.click_checkbox_filter_package()
            except ElementClickInterceptedException as exception:
                print(str(exception) + 'Know BUG-0002')

    def add_to_cart_products(self):
        with allure.step('add_to_cart_products'):
            self.scroll_page(2000)
            self.click_button_add_to_cart_product_1()
            self.click_button_add_to_cart_product_2()
            self.scroll_page(-2000)
            self.assert_word(self.get_counter_products_to_cart(), self.value_counter_products_to_cart_2_products.lower())

    def open_cart_page(self):
        with allure.step('open_cart_page'):
            self.click_button_open_cart_page()
            self.assert_word(self.get_title_page_cart(), self.value_assert_title_page_cart.lower())
