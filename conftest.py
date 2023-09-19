import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def open_browzer():
    print("Открыть браузер и гугл")
    browser.open("https://www.google.com/")
    browser.config.window_width = 2880
    browser.config.window_height = 1800

    yield browser
    print("Закрыть все")
    browser.quit()
