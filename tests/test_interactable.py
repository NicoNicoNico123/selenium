import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestInteractable:

    @pytest.mark.interactException
    def test_Element_Not_Interact_Exception(self, driver):
        #go webpage
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        #Click Add button
        Add_locator = driver.find_element(By.ID, "add_btn")
        Add_locator.click()

        #Explicit wait
        wait = WebDriverWait(driver, 10)
        row_2 = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/input[@type='text']")))

        #wait Row 2
        row_2.send_keys("Chicken")

        # Find the Save button by name and click it
        save = driver.find_element(By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/button[@id='save_btn']")
        save.click()

        wait5 = WebDriverWait(driver, 5)
        confirm = wait5.until(ec.presence_of_element_located((By.ID, "confirmation")))
        assert confirm.is_displayed(), "confirm row should be displayed"
