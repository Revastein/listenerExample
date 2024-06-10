from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.color import Color

from base.base_class import BaseClass


class HomePageLocators(BaseClass):
    """
    Класс, содержащий локаторы и методы для взаимодействия с элементами домашней страницы.

    Атрибуты:
    ----------
    __choose_delivery_address_button : str
        CSS селектор кнопки выбора адреса доставки.
    __map : str
        Идентификатор элемента карты.
    """

    __choose_delivery_address_button = "[test='body_header-main_buttons_container-delivery_address_selector']"
    __map = "myMap"

    def get_delivery_address_button(self, expected_color: str = '#000000') -> WebElement:
        """
        Возвращает элемент кнопки выбора адреса доставки и проверяет его цвет.

        Параметры:
        ----------
        expected_color : str, optional
            Ожидаемый цвет фона кнопки в шестнадцатеричном формате (по умолчанию '#000000').

        Возвращает:
        ----------
        WebElement
            Найденный WebElement кнопки выбора адреса доставки.

        Исключения:
        -----------
        AssertionError
            Если фактический цвет кнопки не совпадает с ожидаемым цветом.
        """
        delivery_button = self.is_clickable("css", self.__choose_delivery_address_button)

        actual_color = delivery_button.value_of_css_property("background-color")
        actual_color_hex = Color.from_string(actual_color).hex
        assert actual_color_hex == expected_color, f"Expected color {expected_color}, but got {actual_color_hex}"

        return delivery_button

    def get_map(self):
        """
        Проверяет видимость элемента карты на странице.

        Возвращает:
        ----------
        WebElement
            Найденный WebElement карты.
        """
        self.is_visible("id", self.__map)
