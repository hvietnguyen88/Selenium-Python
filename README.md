# Python Selenium Automation Project

This project demonstrates automated browser testing using Selenium WebDriver with Python and pytest.

## Features

- Automated test for opening a browser and navigating to Selenium's website
- Uses pytest for test framework
- WebDriver Manager for automatic ChromeDriver handling
- Runs tests in headless mode for faster execution and CI/CD compatibility

## Prerequisites

- Python 3.14.4 or higher
- Google Chrome browser installed

## Installation

1. Clone or download this repository.

2. Navigate to the project directory:
   ```
   cd Selenium-Python
   ```

3. Create a virtual environment:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows: `.\venv\Scripts\Activate.ps1`
   - On macOS/Linux: `source venv/bin/activate`

5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Project Structure

```
Selenium-Python/
├── src/
│   └── test/
│       ├── __init__.py
│       └── heroku/
│           ├── test_open_browser.py
│           ├── test_login.py
│           ├── test_checkboxes.py
│           ├── test_dropdown.py
│           ├── test_hyperlink.py
│           └── test_web_table.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── .vscode/
│   └── settings.json
├── .idea/
├── requirements.txt
└── README.md
```

## Usage

### Running Tests

To run all tests:
```
pytest src/test/
```

To run a specific test file:
```
pytest src/test/heroku/test_open_browser.py
```

To run with verbose output:
```
pytest -v
```

### Test Description

- **Browser Tests** (`src/test/heroku/test_open_browser.py`):
  - Headless mode: Verify Chrome opens in headless mode and navigates to https://www.selenium.dev/
  - Mobile view: Test mobile device emulation
  - Old version: Test with older Chrome versions
  - Fake geolocation: Test geolocation spoofing
  - Network interception: Test network request interception
  - Performance metrics: Capture performance metrics during page load
  - Network conditions: Simulate 3G network conditions

- **Login Tests** (`src/test/heroku/test_login.py`):
  - Test successful login on the-internet.herokuapp.com

- **Checkboxes Tests** (`src/test/heroku/test_checkboxes.py`):
  - Test checking and unchecking checkboxes

- **Dropdown Tests** (`src/test/heroku/test_dropdown.py`):
  - Test dropdown selection functionality

- **Hyperlinks Tests** (`src/test/heroku/test_hyperlink.py`):
  - Test accessing and verifying hyperlinks

- **Web Table Tests** (`src/test/heroku/test_web_table.py`):
  - Test web table data validation

## Troubleshooting

- If you encounter ChromeDriver issues, webdriver-manager should handle it automatically.
- Ensure Chrome browser is installed and up to date.
- If tests fail due to network issues, check your internet connection.

## Contributing

Feel free to add more test cases or improve the existing ones.

## License

This project is for educational purposes.