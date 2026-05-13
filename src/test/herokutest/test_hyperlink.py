from selenium import webdriver
from selenium.webdriver.common.by import By


def test_successfully_access_hyperlinks():
    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/status_codes")
        driver.find_element(By.LINK_TEXT, "200").click()
        assert "https://the-internet.herokuapp.com/status_codes/200" in driver.current_url
        driver.find_element(By.LINK_TEXT, "here").click()
        driver.find_element(By.LINK_TEXT, "301").click()
        assert "https://the-internet.herokuapp.com/status_codes/301" in driver.current_url
        driver.find_element(By.LINK_TEXT, "here").click()
        driver.find_element(By.LINK_TEXT, "404").click()
        assert "https://the-internet.herokuapp.com/status_codes/404" in driver.current_url
        driver.find_element(By.LINK_TEXT, "here").click()
        driver.find_element(By.LINK_TEXT, "500").click()
        assert "https://the-internet.herokuapp.com/status_codes/500" in driver.current_url
        driver.find_element(By.LINK_TEXT, "here").click()
        assert "https://the-internet.herokuapp.com/status_codes" in driver.current_url
    finally:
        driver.quit()




