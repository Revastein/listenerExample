from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.color import Color

from base.base_class import BaseClass


class HomePageLocators(BaseClass):
    __choose_delivery_address_button = "[test='body_header-main_buttons_container-delivery_address_selector']"
    __map = "myMap"

    def get_delivery_address_button(self, expected_color: str = '#000000') -> WebElement:
        delivery_button = self.is_clickable("css", self.__choose_delivery_address_button)

        actual_color = delivery_button.value_of_css_property("background-color")
        actual_color_hex = Color.from_string(actual_color).hex
        assert actual_color_hex == expected_color, f"Expected color {expected_color}, but got {actual_color_hex}"

        return delivery_button

    def get_map(self):
        self.is_visible("id", self.__map)
