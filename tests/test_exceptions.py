import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestExceptions:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        #go webpage
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        #Click Add button
        Add_locator = driver.find_element(By.ID, "add_btn")
        Add_locator.click()

        #Explicit wait
        wait = WebDriverWait(driver, 10)
        row_2 = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/input[@type='text']")))

        #wait Row 2
        assert row_2.is_displayed(), "row2 should be displayed"
