import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()


@pytest.fixture
def user_credentials():
        """Передаём логин и пароль из .env"""
        return  {
        "email": os.getenv("EXC_EMAIL"),
        "password": os.getenv("EXC_PASSWORD"),
        "base_url": os.getenv("BASE_URL"),
        }
@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


