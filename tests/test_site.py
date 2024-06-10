from config.links import *
from pages.base_pages import BasePage


class Test(BasePage):
    def test_monitoring(self, driver):
        driver.get(home_page_url)

        self.home_page.get_delivery_address_button().click()
        self.home_page.get_map()
