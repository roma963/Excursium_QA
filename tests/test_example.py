from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dummy():
    assert True
def test_open_main_page(user_credentials):
    assert "http" in user_credentials["base_url"]

def test_open_site_title(driver, user_credentials):
    driver.get(user_credentials["base_url"])
    WebDriverWait(driver, 10).until(lambda d: d.title != "")
    assert "ЭкскурсиУм" in driver.title

