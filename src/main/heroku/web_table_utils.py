from selenium import webdriver
from selenium.webdriver.common.by import By

def get_due_values(driver):
    table = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr")
    due_values = []
    for row in table:
        due_text = row.find_element(By.XPATH, "td[4]").text
        due_value = float(due_text.replace("$", ""))
        due_values.append(due_value)
    return due_values

def get_persons_by_due(driver, target_due):
    table = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr")
    persons = []
    for row in table:
        due_text = row.find_element(By.XPATH, "td[4]").text
        due_value = float(due_text.replace("$", ""))
        if due_value == target_due:
            last_name = row.find_element(By.XPATH, "td[1]").text
            first_name = row.find_element(By.XPATH, "td[2]").text
            persons.append(last_name + " " + first_name)
    return persons

def get_max_due(due_values):
    return max(due_values)

def get_min_due(due_values):
    return min(due_values)