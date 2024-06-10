import logging
import time

from selenium.webdriver.support.events import AbstractEventListener

from utils.test_utils import is_page_load, check_url_status

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class MonitoringListener(AbstractEventListener):
    """
    Класс для мониторинга событий Selenium WebDriver.

    Этот класс наследует AbstractEventListener и переопределяет методы для мониторинга событий,
    связанных с навигацией по страницам, включая проверку статуса URL и времени загрузки страницы.

    Атрибуты:
    ----------
    start_time : float
        Время начала навигации.
    load_time : float
        Время загрузки страницы.
    """

    def __init__(self):
        """
        Инициализирует MonitoringListener, устанавливая начальные значения для времени начала и загрузки.
        """
        self.start_time = 0.0
        self.load_time = 0.0

    def before_navigate_to(self, url: str, driver) -> None:
        """
        Выполняется перед навигацией к новому URL.

        Параметры:
        ----------
        url : str
            URL, к которому осуществляется навигация.
        driver : WebDriver
            Экземпляр Selenium WebDriver.

        Действия:
        ----------
        - Проверяет статус URL с помощью check_url_status.
        - Записывает время начала навигации.
        - Логгирует начало навигации.
        """
        check_url_status(url)
        self.start_time = time.time()
        logging.info(f"Starting navigation to {url}")

    def after_navigate_to(self, url: str, driver) -> None:
        """
        Выполняется после навигации к новому URL.

        Параметры:
        ----------
        url : str
            URL, к которому была осуществлена навигация.
        driver : WebDriver
            Экземпляр Selenium WebDriver.

        Действия:
        ----------
        - Проверяет, загружена ли страница с помощью is_page_load.
        - Записывает время окончания загрузки.
        - Вычисляет и логгирует время загрузки страницы.
        """
        is_page_load(driver)
        end_time = time.time()
        self.load_time = end_time - self.start_time
        logging.info(f"Page loaded in {self.load_time:.2f} seconds")
