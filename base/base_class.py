from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ex_con
from selenium.webdriver.support.ui import WebDriverWait


class BaseClass:
    """
    Базовый класс для работы с Selenium WebDriver, предоставляющий методы для ожидания элементов.

    Атрибуты:
    ----------
    driver : WebDriver
        Объект Selenium WebDriver, используемый для взаимодействия с браузером.
    __wait : WebDriverWait
        Объект WebDriverWait, используемый для ожидания определенных условий в течение заданного времени.
    """

    def __init__(self, driver):
        """
        Инициализирует BaseClass с заданным WebDriver и настраивает WebDriverWait.

        Параметры:
        ----------
        driver : WebDriver
            Объект Selenium WebDriver, используемый для взаимодействия с браузером.
        """
        self.driver = driver
        self.__wait = WebDriverWait(driver, 20, 1)

    @staticmethod
    def __get_selenium_by(find_by: str) -> str:
        """
        Возвращает метод поиска Selenium по строковому представлению.

        Параметры:
        ----------
        find_by : str
            Строковое представление метода поиска (например, 'css', 'xpath').

        Возвращает:
        ----------
        str
            Соответствующий метод поиска Selenium.
        """
        find_by = find_by.lower()
        locating = {'css': By.CSS_SELECTOR,
                    'xpath': By.XPATH,
                    'class_name': By.CLASS_NAME,
                    'id': By.ID,
                    'link_text': By.LINK_TEXT,
                    'name': By.NAME,
                    'partial_link_text': By.PARTIAL_LINK_TEXT,
                    'tag_name': By.TAG_NAME}
        return locating[find_by]

    def is_visible(self, find_by: str, locator: str, error_message: str = None) -> WebElement:
        """
        Ожидает, пока элемент не станет видимым на странице.

        Параметры:
        ----------
        find_by : str
            Метод поиска элемента (например, 'css', 'xpath').
        locator : str
            Локатор элемента.
        error_message : str
            Сообщение об ошибке, если элемент не найден (по умолчанию None).

        Возвращает:
        ----------
        WebElement
            Найденный WebElement.
        """
        return self.__wait.until(
            ex_con.visibility_of_element_located((self.__get_selenium_by(find_by), locator)),
            error_message)

    def is_clickable(self, find_by: str, locator: str, error_message: str = None) -> WebElement:
        """
        Ожидает, пока элемент не станет кликабельным на странице.

        Параметры:
        ----------
        find_by : str
            Метод поиска элемента (например, 'css', 'xpath').
        locator : str
            Локатор элемента.
        error_message : str, optional
            Сообщение об ошибке, если элемент не найден (по умолчанию None).

        Возвращает:
        ----------
            Найденный WebElement.
        """
        return self.__wait.until(
            ex_con.element_to_be_clickable((self.__get_selenium_by(find_by), locator)),
            error_message)
