from classes.person import Person
import csv

class Staff(Person):
    def __init__(self, name, age, role, password, staff_id) -> None:
        super().__init__(name, age, role, password)
        self.staff_id = staff_id

    @staticmethod
    def all_staff():
        # return contents of student.csv
        with open('data/staff.csv', newline='') as file:
            csv_reader = csv.DictReader(file, skipinitialspace=True)
            staff = [row for row in csv_reader]
            file.close()
        
        return staff