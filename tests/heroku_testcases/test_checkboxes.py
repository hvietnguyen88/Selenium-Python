import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def check_checkbox(checkbox):
    if not checkbox.is_selected():
        checkbox.click()

def uncheck_checkbox(checkbox):
    if checkbox.is_selected():
        checkbox.click()

def test_checkboxes():
    driver = webdriver.Edge()

    try:
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        time.sleep(1)  # Wait for the page to load
        checkbox1 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[1]")
        checkbox2 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[2]")

        # Check the first checkbox and uncheck the second checkbox
        check_checkbox(checkbox1)
        time.sleep(1)  # Wait for the action to take effect
        uncheck_checkbox(checkbox2)

        # Verify the states of the checkboxes
        assert checkbox1.is_selected() == True
        assert checkbox2.is_selected() == False

    finally:
        time.sleep(2)  # Wait for the page to load
        driver.quit()    