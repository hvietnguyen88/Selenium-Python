from selenium.webdriver.common.by import By
from main.heroku.person import Person


class TablePage:
    def __init__(self, driver):
        self.driver = driver
        self.person_list = []

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/tables")
        self._get_table()

    def _get_table(self):
        self.person_list.clear()

        rows = self.driver.find_elements(
            By.XPATH,
            "//table[@id='table1']/tbody/tr"
        )

        for row in rows:
            cells = row.text.split()
            self.person_list.append(
                Person(
                    cells[0],  # last_name
                    cells[1],  # first_name
                    cells[3]   # due
                )
            )

    def _get_max_due(self):
        return max(
            self.person_list,
            key=lambda person: person.get_due()
        ).get_due()

    def _get_min_due(self):
        return min(
            self.person_list,
            key=lambda person: person.get_due()
        ).get_due()

    def get_max_due_persons(self):
        return [
            person.get_full_name()
            for person in self.person_list
            if person.get_due() == self._get_max_due()
        ]

    def get_min_due_persons(self):
        return [
            person.get_full_name()
            for person in self.person_list
            if person.get_due() == self._get_min_due()
        ]