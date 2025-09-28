import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    """Создаём и закрываем браузер для каждого теста"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_open_example(driver):
    driver.get("http://www.example.com")
    assert "Example Domain" in driver.title

def test_h1_example(driver):
    driver.get("http://www.example.com")
    h1 = driver.find_element("tag name","h1")
    assert "Example Domain" in h1.text