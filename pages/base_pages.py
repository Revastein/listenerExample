import pytest

from pages.home_page import HomePageLocators


class BasePage:
    """
    Базовый класс для страниц, содержащий общие элементы и настройки для работы с ними.

    Атрибуты:
    ----------
    home_page : HomePageLocators
        Локаторы для элементов домашней страницы.
    """

    home_page: HomePageLocators

    @pytest.fixture(autouse=True)
    def pages(self, request, driver):
        """
        Фикстура для автоматического создания и настройки страниц с использованием локаторов.

        Параметры:
        ----------
        request : _pytest.fixtures.FixtureRequest
            Объект запроса, предоставляемый pytest для настройки тестовых классов.
        driver : WebDriver
            Объект Selenium WebDriver, используемый для взаимодействия с браузером.
        """
        request.cls.home_page = HomePageLocators(driver)
