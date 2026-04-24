import time
import pytest
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_open_browser_with_headless_mode():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.selenium.dev/")
    assert driver.current_url == "https://www.selenium.dev/"
    
    driver.quit()

def test_open_browser_with_mobile_view_mode():
    mobile_emulation = {
        "deviceMetrics": {
            "width": 344,
            "height": 882
        }
    }

    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://www.selenium.dev/")
        assert "Selenium" in driver.title
    finally:
        time.sleep(3)  # Wait for the page to load
        driver.quit()

def test_open_browser_with_old_version():
    chrome_options = Options()
    chrome_options.browser_version = "129"
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get("https://www.selenium.dev/")
        assert driver.title == "Selenium"
    finally:
        time.sleep(3)  # Wait for the page to load
        driver.quit()

def test_open_browser_with_fake_geo_location():
    driver = webdriver.Chrome()
    dev_tools = driver.execute_cdp_cmd

    try:
        # Mountain view
        driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
            "latitude": 37.386052,
            "longitude": -122.083851,
            "accuracy": 1
        })

        driver.get("https://the-internet.herokuapp.com/geolocation")
        driver.find_element(By.XPATH, "//button[.='Where am I?']").click()

        assert driver.find_element(By.CSS_SELECTOR, "#lat-value").text == "37.386052"
        assert driver.find_element(By.CSS_SELECTOR, "#long-value").text == "-122.083851"
    finally:
        time.sleep(3)  # Wait for the page to load
        driver.quit()

def test_interception_network():
    chrome_options = Options()
    chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.execute_cdp_cmd("Network.enable", {})
        driver.get("https://selenium.dev")

        logs = driver.get_log("performance")

        for log in logs:
            message = json.loads(log["message"])["message"]
            method = message.get("method")
            params = message.get("params", {})

            if method == "Network.requestWillBeSent":
                request = params.get("request", {})
                print(f"Request URL => {request.get('url')}")
                print(f"Request Method => {request.get('method')}")
                print(f"Request Headers => {request.get('headers')}")
                print("------------------------------------------------------")

            elif method == "Network.responseReceived":
                response = params.get("response", {})
                print(f"Response URL => {response.get('url')}")
                print(f"Response Status => {response.get('status')}")
                print(f"Response Headers => {response.get('headers')}")
                print(f"Response MIME Type => {response.get('mimeType')}")
                print("------------------------------------------------------")

    finally:
        driver.quit()

def test_open_selenium_home_page_and_capture_performance_metrics():
    driver = webdriver.Chrome()

    try:
        # Enable Performance domain via CDP
        driver.execute_cdp_cmd("Performance.enable", {})

        driver.get("https://selenium.dev")

        assert driver.title == "Selenium"

        # Get performance metrics
        metrics = driver.execute_cdp_cmd("Performance.getMetrics", {})

        for metric in metrics.get("metrics", []):
            print(f"{metric['name']} = {metric['value']}")

    finally:
        driver.quit()

def test_simulate_3g_network_conditions():
    driver = webdriver.Chrome()

    try:
        # Enable Network domain via CDP
        driver.execute_cdp_cmd("Network.enable", {
            "maxTotalBufferSize": 100000000
        })

        # Simulate 3G network conditions with realistic speeds
        driver.execute_cdp_cmd("Network.emulateNetworkConditions", {
            "offline": False,
            "latency": 100,                       # ms
            "downloadThroughput": 750 * 1024 / 8, # 750 kbps → bytes/sec
            "uploadThroughput": 250 * 1024 / 8,   # 250 kbps → bytes/sec
            "connectionType": "cellular3g",
            "packetLoss": 0,
            "packetQueueLength": 0,
            "packetReordering": False
        })

        driver.get("https://selenium.dev")

        # Wait for title instead of hardcoded sleep
        WebDriverWait(driver, 30).until(
            EC.title_is("Selenium")
        )

        assert driver.title == "Selenium"

    finally:
        driver.quit()