from selenium.webdriver.common.by import By
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from utils.driver import get_driver
from pages.home_page import HomePage
from utils.config import BASE_URL
from utils.config import REG_URL

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_home_page_banner(driver):
    home_page = HomePage(driver)
    home_page.open_url(BASE_URL)
    assert driver.find_element(By.XPATH, home_page.training_banner).is_displayed(), "Training banner is not displayed"

def test_training_banner_redirect(driver):
    home_page = HomePage(driver)
    home_page.open_url(BASE_URL)
    home_page.click_training_banner()

    window_handles = driver.window_handles
    assert len(window_handles) > 1, "New window did not open after clicking the banner"

    driver.switch_to.window(window_handles[1])
    expected_url = REG_URL
    assert driver.current_url == expected_url, f"Expected URL to be {expected_url}, but got {driver.current_url}"

    driver.close()
    driver.switch_to.window(window_handles[0])
