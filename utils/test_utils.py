import requests
from selenium.webdriver.support.ui import WebDriverWait


def is_page_load(driver):
    return WebDriverWait(driver, 20, 0.5).until(lambda d: d.execute_script('return document.readyState') == 'complete')


def check_url_status(url: str) -> None:
    headers = {
        'User-Agent': 'PostmanRuntime/7.39.0'
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Resource status code: {response.status_code}"
