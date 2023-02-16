from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def driver():
    print("Create chrome driver")
    my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # my_driver.implicitly_wait(10)
    yield my_driver
    print("Close chrome driver")
    my_driver.quit()