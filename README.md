# Python Selenium Automation Project

This project demonstrates automated browser testing using Selenium WebDriver with Python and pytest.

## Features

- Automated test for opening a browser and navigating to Selenium's website
- Uses pytest for test framework
- WebDriver Manager for automatic ChromeDriver handling
- Runs tests in headless mode for faster execution and CI/CD compatibility

## Prerequisites

- Python 3.14.3 or higher
- Google Chrome browser installed

## Installation

1. Clone or download this repository.

2. Navigate to the project directory:
   ```
   cd "d:\LEARNING\SOFTWARE TESTING\TVN\AUTOMATION\AK2604_Python"
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

## Usage

### Running Tests

To run all tests:
```
pytest
```

To run a specific test file:
```
pytest test_open_browser.py
```

To run with verbose output:
```
pytest -v
```

### Test Description

- `test_open_browser.py`: Tests opening Chrome browser in headless mode, navigating to https://www.selenium.dev/, and verifying the URL.

## Troubleshooting

- If you encounter ChromeDriver issues, webdriver-manager should handle it automatically.
- Ensure Chrome browser is installed and up to date.
- If tests fail due to network issues, check your internet connection.

## Contributing

Feel free to add more test cases or improve the existing ones.

## License

This project is for educational purposes.