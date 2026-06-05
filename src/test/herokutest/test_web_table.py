import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from main.heroku.person import Person
from main.herokupages import table_page
from main.herokupages.table_page import TablePage

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver

    table_page = TablePage(driver)
    request.cls.table_page = table_page

    table_page.open()

    yield

    driver.quit()


@pytest.mark.usefixtures("setup")
class TestWebTable:

    def test_successfully_validate_max_due_persons_new(self):
        assert self.table_page.get_max_due_persons() == ["Jason Doe"]

    def test_successfully_validate_min_due_persons_new(self):
        assert self.table_page.get_min_due_persons() == ["John Smith", "Tim Conway"]

# def test_successfully_validate_max_due_persons():
#     driver = webdriver.Chrome()
#     driver.get("https://the-internet.herokuapp.com/tables")
#     rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr")
#     person_list: list[Person] = []
#     for row in rows:
#         cells = row.text.split(" ")
#         person_list.append(Person(cells[0], cells[1], cells[3]))
#     max_due = max(person_list, key=lambda person: person.get_due()).get_due()
#     max_due_persons = [
#         person.get_full_name()
#         for person in person_list
#         if person.get_due() == max_due
#     ]
#     assert max_due_persons == ["Jason Doe"]
#
# def test_successfully_validate_min_due_persons():
#     driver = webdriver.Chrome()
#     driver.get("https://the-internet.herokuapp.com/tables")
#     rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr")
#     person_list: list[Person] = []
#     for row in rows:
#         cells = row.text.split(" ")
#         person_list.append(Person(cells[0], cells[1], cells[3]))
#     min_due = min(person_list, key=lambda person: person.get_due()).get_due()
#     min_due_persons = [
#         person.get_full_name()
#         for person in person_list
#         if person.get_due() == min_due
#     ]
#     assert min_due_persons == ['John Smith', 'Tim Conway']