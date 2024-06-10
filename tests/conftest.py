import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver

from tests.listener import MonitoringListener


@pytest.fixture(params=["chrome"], scope="function")
def driver():
    """
    Фикстура для инициализации и завершения работы с Selenium WebDriver.

    Эта фикстура создает экземпляр WebDriver для браузера Chrome с заданными опциями,
    включая работу в режиме headless и отключение загрузки изображений. WebDriver
    обернут в EventFiringWebDriver для мониторинга событий с использованием MonitoringListener.

    Параметры:
    ----------
    params : list, optional
        Список браузеров для параметризации (по умолчанию включает только 'chrome').
    scope : str, optional
        Область действия фикстуры (по умолчанию 'function').

    Возвращает:
    ----------
    EventFiringWebDriver
        Объект WebDriver, обернутый в EventFiringWebDriver для мониторинга событий.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_experimental_option("prefs", {'profile.managed_default_content_settings.images': 2})

    driver = webdriver.Chrome(options)
    event_listener = MonitoringListener()
    e_driver = EventFiringWebDriver(driver, event_listener)

    yield e_driver
    e_driver.quit()
