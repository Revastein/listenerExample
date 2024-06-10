import logging
import time

from selenium.webdriver.support.events import AbstractEventListener

from utils.test_utils import is_page_load, check_url_status

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class MonitoringListener(AbstractEventListener):
    def __init__(self):
        self.start_time = 0.0
        self.load_time = 0.0

    def before_navigate_to(self, url: str, driver) -> None:
        check_url_status(url)
        self.start_time = time.time()
        logging.info(f"Starting navigation to {url}")

    def after_navigate_to(self, url: str, driver) -> None:
        is_page_load(driver)
        end_time = time.time()
        self.load_time = end_time - self.start_time
        logging.info(f"Page loaded in {self.load_time:.2f} seconds")
