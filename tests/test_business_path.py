from selenium import webdriver

from base.base_class import Base
from pages.cart_page import CartPage
from pages.welcome_page import WelcomePage
from pages.main_page import MainPage
from pages.whisky_page import WhiskyPage


# @pytest.mark.run(order=1)
def test_filters(set_up):
    driver = webdriver.Firefox()

    welcome = WelcomePage(driver)
    welcome.enter_to_service()

    main_page = MainPage(driver)
    main_page.open_page_whisky_via_menu()

    whisky_page = WhiskyPage(driver)
    whisky_page.open_filters_brand()
    whisky_page.select_different_filters()

    driver.quit()


# @pytest.mark.run(order=1)
def test_business_path(set_up):
    driver = webdriver.Firefox()

    welcome = WelcomePage(driver)
    welcome.enter_to_service()

    main_page = MainPage(driver)
    main_page.open_page_whisky_via_menu()

    whisky_page = WhiskyPage(driver)
    whisky_page.add_to_cart_products()
    whisky_page.open_cart_page()

    cart_page = CartPage(driver)
    cart_page.select_products_in_cart()
    cart_page.users_info()
    base = Base(driver)
    base.get_screenshot()

    driver.quit()

# python -m pytest -sv tests\test_business_path.py
