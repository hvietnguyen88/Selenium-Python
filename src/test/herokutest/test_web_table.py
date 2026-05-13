from selenium import webdriver
from src.main.heroku import web_table_utils


def test_successfully_validate_largest_due_person():
    driver = webdriver.Chrome()
    try:
        driver.get("https://the-internet.herokuapp.com/tables")
        due_values = web_table_utils.get_due_values(driver)
        max_due = web_table_utils.get_max_due(due_values)
        max_due_persons = web_table_utils.get_persons_by_due(driver, max_due)
        assert "Doe Jason" in max_due_persons
    finally:
        driver.quit()

def test_successfully_validate_smallest_due_person():
    driver = webdriver.Chrome()
    try:
        driver.get("https://the-internet.herokuapp.com/tables")
        due_values = web_table_utils.get_due_values(driver)
        min_due = web_table_utils.get_min_due(due_values)
        min_due_persons = web_table_utils.get_persons_by_due(driver, min_due)
        assert "Smith John" in min_due_persons
        assert "Conway Tim" in min_due_persons
    finally:
        driver.quit()