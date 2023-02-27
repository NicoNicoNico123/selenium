import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_objects.exception_page import ExceptionPage

class TestExceptions:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        #go webpage
        exception_page = ExceptionPage(driver)
        exception_page.open()

        #Click Add button
        exception_page.execute_add()

        #wait Row 2
        assert exception_page.is_row2_field_displayed(), "row2 should be displayed"
