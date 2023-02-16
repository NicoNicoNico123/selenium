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

        # Find the instructions text element
        instructions = driver.find_element(By.ID, "instructions")
        assert instructions.text == "Push “Add” button to add another row" , "Instructions element should be displayed"

        # Click the Add button
        add_btn = driver.find_element(By.ID, "add_btn")
        add_btn.click()

        # Wait for the input field to be enabled
        wait = WebDriverWait(driver, 10)
        wait.until_not(ec.visibility_of_element_located((By.ID, "instructions")))

        # verify the instructions element is no longer displayed
        time.sleep(2)
        assert not instructions.is_displayed(), "Instructions element should not be displayed"