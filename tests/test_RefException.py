import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestExceptions:

    @pytest.mark.refException
    def test_refExceptions(self, driver):
        #go webpage
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")


        # Click the Add button
        add_btn = driver.find_element(By.ID, "add_btn")
        add_btn.click()

        # Wait for the input field to be enabled
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located((By.ID, "instructions"))), "Instructions element should not be displayed"

