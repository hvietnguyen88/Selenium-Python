from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_open_browser():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.selenium.dev/")
    assert driver.current_url == "https://www.selenium.dev/"
    driver.quit()