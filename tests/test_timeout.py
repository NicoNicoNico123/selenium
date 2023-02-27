import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Test_timeout:

    @pytest.mark.timeout
    def test_InvalidElementStateException(self, driver):
        #go webpage
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click the Add button
        add_btn = driver.find_element(By.ID, "add_btn")
        add_btn.click()

        # wait for the input field for row 2 to be displayed
        wait = WebDriverWait(driver, 3)
        assert wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/input[@type='text']")), "Input element should be displayed")
