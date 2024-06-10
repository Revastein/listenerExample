import requests
from selenium.webdriver.support.ui import WebDriverWait


def is_page_load(driver):
    """
    Ожидает завершения загрузки страницы.

    Параметры:
    ----------
    driver : WebDriver
        Экземпляр Selenium WebDriver.

    Возвращает:
    ----------
    bool
        True, если документ готов к взаимодействию (состояние 'complete').
    """
    return WebDriverWait(driver, 20, 0.5).until(lambda d: d.execute_script('return document.readyState') == 'complete')


def check_url_status(url: str) -> None:
    """
    Проверяет статус ответа для заданного URL.

    Параметры:
    ----------
    url : str
        URL, который необходимо проверить.

    Исключения:
    -----------
    AssertionError
        Если статус-код ответа не равен 200.

    Действия:
    ----------
    - Отправляет GET-запрос к заданному URL с заголовком User-Agent.
    - Проверяет, что статус-код ответа равен 200.
    """
    headers = {
        'User-Agent': 'PostmanRuntime/7.39.0'
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Resource status code: {response.status_code}"
