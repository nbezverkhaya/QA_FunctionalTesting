from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Book_Search(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_input = "searchBox"

    def enter_search_query(self, query):
        self.driver.find_element(By.ID, self.search_input).send_keys(query)
        self.driver.find_element(By.ID, self.search_input).send_keys(Keys.ENTER)
