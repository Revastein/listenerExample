import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver

from tests.listener import MonitoringListener


@pytest.fixture(params=["chrome"], scope="function")
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_experimental_option("prefs", {'profile.managed_default_content_settings.images': 2})

    driver = webdriver.Chrome(options)
    event_listener = MonitoringListener()
    e_driver = EventFiringWebDriver(driver, event_listener)

    yield e_driver
    e_driver.quit()
