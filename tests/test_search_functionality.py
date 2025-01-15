import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from utils.driver import get_driver
from pages.search_page import Book_Search
from utils.config import BOOK_URL
import data_for_testing

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.mark.parametrize(
    "search_query",
    [
        data_for_testing.author1,
        data_for_testing.author2,
        data_for_testing.author3,
        data_for_testing.publisher1,
        data_for_testing.publisher2,
        data_for_testing.title1,
        data_for_testing.title2,
        data_for_testing.title3,
    ]
)
def test_search_functionality(driver, search_query):
    search_page = Book_Search(driver)
    search_page.open_url(BOOK_URL)
    search_page.enter_search_query(search_query)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.rt-tr-group .rt-tr'))
    )
    rows = driver.find_elements(By.CSS_SELECTOR, '.rt-tr-group .rt-tr')
    for i, row in enumerate(rows, start=1):
        row_text = row.text.strip()
        if not row_text:
            # print(f"Рядок {i} є порожнім і був пропущений.")
            continue
        assert search_query in row_text

    driver.close()
