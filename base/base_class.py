import datetime

import allure


class Base:
    def __init__(self, driver):
        self.driver = driver

    """Method GET current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current_url: " + get_url)

    """Method assert word"""

    @staticmethod
    def assert_word(word, result):
        value_word = word.text.lower()
        print(f'Value_word: "{value_word}"')
        print()
        assert value_word == result
        print(f'Success test! Value word "{value_word}" == result "{result}"')

    """Method screenshot"""

    def get_screenshot(self):
        with allure.step('get_screenshot'):
            # создать скриншот с датой в директории screen, не перезаписываемый
            now_date = datetime.datetime.now().strftime('%Y.%m.%d-%H.%M')
            name_screenshot = 'screenshot_' + now_date + '.png'
            print(name_screenshot)
            self.driver.save_screenshot('C:\\pythonProject\\pythonProject1\\pythonProject\\wb_project\\screen\\' + name_screenshot)

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print(f'Success test! Current url "{get_url}" == result "{result}"')

    """Method assert word"""

    def scroll_page(self, scroll_px_y):
        self.driver.execute_script(f'window.scrollTo(0, {scroll_px_y})')
        print(f'Scroll page to {scroll_px_y}px')
