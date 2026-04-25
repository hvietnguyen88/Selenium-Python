import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_dropdown():
    driver = webdriver.Edge()

    try:
        driver.get("https://the-internet.herokuapp.com/dropdown")
        dropdown = Select(driver.find_element(By.ID, "dropdown"))
        
        dropdown.select_by_index(1)  # Select Option 1
        assert dropdown.first_selected_option.text == "Option 1" # Verify Option 1 is selected
        time.sleep(1)  # Wait for the action to take effect

        dropdown.select_by_visible_text("Option 2")  # Select Option 2
        assert dropdown.first_selected_option.text == "Option 2" # Verify Option 2 is selected
        time.sleep(1)  # Wait for the action to take effect
        dropdown.select_by_value("1")  # Select Option 1 again
        assert dropdown.first_selected_option.text == "Option 1" # Verify Option 1 is selected

    finally:
        time.sleep(2)  # Wait for the page to load
        driver.quit()