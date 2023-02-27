import time

# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
# to supress the error messages/logs
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()

#go webpage
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)

#Typer username student into Username field
username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("student")
#Password

#Push Submit button
password_locator =  driver.find_element(By.NAME, "password")
password_locator.send_keys("Password123")
#Push submit button
submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
submit_button_locator.click()
time.sleep(2)

#Verify new page URL contains practicetestautomation.com/logged-in
actual_url = driver.current_url
assert "practicetestautomation.com/logged-in-successfully/" in actual_url

#Verify new page URL contains exptected text
text_locator = driver.find_element(By.TAG_NAME, "h1")
actual_text = text_locator.text
assert actual_text == "Logged In Successfully"

#VerifyLogout button
log_out_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
assert log_out_button_locator.is_displayed()