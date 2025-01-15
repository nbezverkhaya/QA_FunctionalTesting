from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.training_banner = "//a[@href='https://www.toolsqa.com/selenium-training/']//img[@src='/images/WB.svg']"

    def click_training_banner(self):
        self.driver.find_element(By.XPATH, self.training_banner).click()

