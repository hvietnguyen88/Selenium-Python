import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login():
    driver = webdriver.Edge()

    try:
        driver.get("https://the-internet.herokuapp.com/login")
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        assert "https://the-internet.herokuapp.com/secure" in driver.current_url
    finally:
        time.sleep(2)  # Wait for the page to load
        driver.quit()