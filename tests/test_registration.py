from selenium.webdriver.common.by import By
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from utils.driver import get_driver
from pages.registration_page import RegistrationPage

from utils.config import REG_URL

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_reg_button_present(driver):
    reg_page = RegistrationPage(driver)
    reg_page.open_url(REG_URL)
    assert driver.find_element(By.XPATH, reg_page.reg_button).is_displayed(), "Registration button is not displayed"

def test_registration_form_present(driver):
    reg_page = RegistrationPage(driver)
    reg_page.open_url(REG_URL)
    reg_page.click_reg_button()

    reg_page.verify_registration_form_fields()

    driver.close()
