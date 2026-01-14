import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def driver(request):
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()