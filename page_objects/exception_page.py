from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage

class ExceptionPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button = (By.ID, "add_btn")
    __row2_field = (By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/input[@type='text']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)
    
    def execute_add(self):
        super()._click(self.__add_button)
        super()._wait_until_element_is_visible(self.__row2_field)

    def is_row2_field_displayed(self) -> bool:
        return super()._is_displayed(self.__row2_field)