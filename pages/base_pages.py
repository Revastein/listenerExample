import pytest

from pages.home_page import HomePageLocators


class BasePage:
    home_page: HomePageLocators

    @pytest.fixture(autouse=True)
    def pages(self, request, driver):
        request.cls.home_page = HomePageLocators(driver)
