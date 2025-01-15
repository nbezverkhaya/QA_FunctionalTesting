from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name_field = "//input[@id='first-name']"
        self.last_name_field = "//input[@id='last-name']"
        self.email_field = "//input[@id='email']"
        self.mobile_field = "//input[@id='mobile']"
        self.country_dropdown = "//select[@id='country']"
        self.city_field = "//input[@id='city']"
        self.message_field = "//textarea[@id='message']"
        self.code_input = "//input[@id='code']"
        self.captcha_image = "//img[contains(@class, 'upcoming__registration--captcha')]"
        self.send_button = "//*[@id='enroll-form']/button"
        self.reg_button = "/html/body/div[1]/div[1]/div/div[1]/div[2]/a"

    def verify_registration_form_fields(self):
        # Перевіряємо наявність кожного елемента на сторінці
        assert self.driver.find_element(By.XPATH, self.first_name_field).is_displayed(), "First name field is missing"
        assert self.driver.find_element(By.XPATH, self.last_name_field).is_displayed(), "Last name field is missing"
        assert self.driver.find_element(By.XPATH, self.email_field).is_displayed(), "Email field is missing"
        assert self.driver.find_element(By.XPATH, self.mobile_field).is_displayed(), "Mobile field is missing"
        assert self.driver.find_element(By.XPATH, self.country_dropdown).is_displayed(), "Country dropdown is missing"
        assert self.driver.find_element(By.XPATH, self.city_field).is_displayed(), "City field is missing"
        assert self.driver.find_element(By.XPATH, self.message_field).is_displayed(), "Message field is missing"
        assert self.driver.find_element(By.XPATH, self.code_input).is_displayed(), "Code input field is missing"
        assert self.driver.find_element(By.XPATH, self.captcha_image).is_displayed(), "Captcha image is missing"
        assert self.driver.find_element(By.XPATH, self.send_button).is_displayed(), "Send button is missing"

    def click_reg_button(self):
        self.driver.find_element(By.XPATH, self.reg_button).click()