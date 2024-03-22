import random
import re

from selenium.common import TimeoutException

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker


class CartPage(Base):
    """Инициализируем атрибуты"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.faker = Faker('ru_RU')

    # Locators
    plus_quant_to_first_product = '(//a[@class="cart-item__quant-plus"])[1]'
    total_quantity_products = '//div[@class="cart-total__quantity"]/span'
    price_product_1 = '(//div[@class="cart-item__price"])[1]/div[1]'
    price_product_2 = '(//div[@class="cart-item__price"])[2]/div[1]'
    total_price_products = '//div[@class="cart-total__price"]'
    delete_second_products = '(//a[@class="cart-item__delete"])[2]'
    input_user_phone = '//input[@class="phone js-cart-phone"]'
    input_user_name = '//input[@id="name"]'
    radiobutton_store = '(//label[@class="js-radio-receiving"])[2]'
    selectors_menu_store = '(//p[@class="CaptionCont SelectBox"])[1]'
    selectors_menu_store_3 = '//div/div[2]/div/ul/li[3]/label'
    quantity_product_1 = '(//span[@class="cart-item__quant-num js-cart-quant-num"]/input)[1]'
    quantity_product_2 = '(//span[@class="cart-item__quant-num js-cart-quant-num"]/input)[2]'

    # Assert words
    url_cart_page = 'https://decanter.ru/cart'

    # Getters
    def get_plus_quant_to_first_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.plus_quant_to_first_product)))

    def get_total_quantity_products(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.total_quantity_products)))

    def get_price_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.price_product_1)))

    def get_price_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.price_product_2)))

    def get_total_price_products(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.total_price_products)))

    def get_delete_second_products(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.delete_second_products)))

    def get_input_user_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.input_user_phone)))

    def get_input_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.input_user_name)))

    def get_radiobutton_store(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.radiobutton_store)))

    def get_selectors_menu_store(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.selectors_menu_store)))

    def get_selectors_menu_store_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.selectors_menu_store_3)))

    def get_quantity_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.quantity_product_1)))

    def get_quantity_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.quantity_product_2)))

    # Actions
    def click_plus_quant_to_first_product(self):
        self.get_plus_quant_to_first_product().click()
        print('Click plus_quant_to_first_product')

    def assert_quantity_products(self, quantity_product_1, quantity_product_2, total_quantity_products):
        value_quantity_product_1 = int(quantity_product_1.get_attribute('value'))
        print(f'value_quantity_product_1: {value_quantity_product_1}')
        value_quantity_product_2 = int(quantity_product_2.get_attribute('value'))
        print(f'value_quantity_product_2: {value_quantity_product_2}')
        value_total_quantity_products = value_quantity_product_1 + value_quantity_product_2
        print(f'value_total_quantity_products: {value_total_quantity_products}')
        total_quantity_products = total_quantity_products.text
        total_quantity_products_lst = re.findall(r'\b\d+\b', total_quantity_products)
        total_quantity_products_int = int(str(total_quantity_products_lst[0]))
        print(f'value_total_quantity_products_int: {total_quantity_products_int}')
        assert value_total_quantity_products == total_quantity_products_int
        print(f'Success test! value_total_quantity_products:{value_total_quantity_products} '
              f'== value_total_quantity_products_int:{total_quantity_products_int}')

    def assert_sum_price_products(self, price_product_1, price_product_2, total_sum_price):
        value_price_product_1 = int(price_product_1.text.replace(' ', ''))
        print(f'value_price_product_1:{value_price_product_1}')
        value_price_product_2 = int(price_product_2.text.replace(' ', ''))
        print(f'value_price_product_2:{value_price_product_2}')
        value_total_sum_price = int(total_sum_price.text.replace(' ', ''))
        print(f'value_total_sum_price:{value_total_sum_price}')
        value_sum_price_products = value_price_product_1 + value_price_product_2
        print(f'value_sum_price_products:{value_sum_price_products}')
        assert value_sum_price_products == value_total_sum_price
        print(f'Success test! value_sum_price_products:{value_sum_price_products}'
              f' == value_total_sum_price:{value_total_sum_price}')

    def click_delete_products(self):
        self.get_delete_second_products().click()
        print('Click delete_second_products')

    def assert_total_price_products(self, price_product_1, total_sum_price):
        value_price_product_1 = int(price_product_1.text.replace(' ', ''))
        print(f'value_price_product_1:{value_price_product_1}')
        value_total_sum_price = int(total_sum_price.text.replace(' ', ''))
        print(f'value_total_sum_price:{value_total_sum_price}')
        assert value_price_product_1 == value_total_sum_price
        print(f'Success test! value_sum_price_products:{value_price_product_1}'
              f' == value_total_sum_price:{value_total_sum_price}')

    def fill_input_user_phone(self):
        code_phone = '900'
        num = []
        n = 7
        for i in range(n):
            num.append(random.randint(1, 9))
        print(num)
        number_phone = ''
        for i in num:
            number_phone += str(i)
        print(number_phone)
        self.get_input_user_phone().send_keys(code_phone + number_phone)
        print(f'Fill input_user_phone: {code_phone}{number_phone}')

    def fill_input_user_name(self):
        self.get_input_user_name().send_keys(self.faker.first_name() + '_' + str(self.faker.random_int()))
        print('Fill input_user_name')

    def click_radiobutton_store(self):
        self.get_radiobutton_store().click()
        print('Click radiobutton_store')

    def click_selectors_menu_store(self):
        self.get_selectors_menu_store().click()
        print('Click selectors_menu_store')

    def click_selectors_menu_store_3(self):
        self.get_selectors_menu_store_3().click()
        print('Click selectors_menu_store_3')

    # Methods
    def select_products_in_cart(self):
        self.assert_url(self.url_cart_page)
        self.assert_quantity_products(self.get_quantity_product_1(), self.get_quantity_product_2(),
                                      self.get_total_quantity_products())
        self.click_plus_quant_to_first_product()
        self.assert_quantity_products(self.get_quantity_product_1(), self.get_quantity_product_2(),
                                      self.get_total_quantity_products())
        self.assert_sum_price_products(self.get_price_product_1(), self.get_price_product_2(),
                                       self.get_total_price_products())
        self.click_delete_products()

        try:
            self.assert_quantity_products(self.get_quantity_product_1(), self.get_quantity_product_2(),
                                          self.get_total_quantity_products())
        except TimeoutException as exception:
            print(str(exception) + 'Test "click_delete_products" is success! ')
        self.assert_total_price_products(self.get_price_product_1(), self.get_total_price_products())

    def users_info(self):
        self.fill_input_user_name()
        self.fill_input_user_phone()
        self.click_radiobutton_store()
        self.click_selectors_menu_store()
        self.click_selectors_menu_store_3()
        # self.get_screenshot()
