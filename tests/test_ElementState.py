import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestElementState:

    @pytest.mark.elementState
    def test_InvalidElementStateException(self, driver):
        #go webpage
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        #Click Edit button
        Edit_locator = driver.find_element(By.ID, "edit_btn")
        Edit_locator.click()

        # wait for the "disabled" attribute to disappear from the input field
        wait = WebDriverWait(driver, 12)
        input_field = wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@id='rows']/div[1]/div[@class='row']/input[@value='Pizza']")))
        assert "disabled" not in input_field.get_attribute("class"), "input field should be enabled"

        # clear the input field and type new text
        input_field.clear()
        input_field.send_keys("Coke")


        # Find the Save button by name and click it
        save_btn = driver.find_element(By.XPATH, "/html//button[@id='save_btn']")
        save_btn.click()

        # verify the text has changed
        # time.sleep(2)
        wait.until(ec.presence_of_element_located((By.ID, "confirmation")))
        assert input_field.get_attribute("value") == "Sushi"