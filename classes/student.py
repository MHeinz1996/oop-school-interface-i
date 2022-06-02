from classes.person import Person
import csv

class Student(Person):
    def __init__(self, name, age, role, password, student_id) -> None:
        super().__init__(name, age, role, password)
        self.student_id = student_id

    @staticmethod
    def all_students():
        # return contents of student.csv
        with open('data/students.csv', newline='') as file:
            csv_reader = csv.DictReader(file, skipinitialspace=True)
            students = [row for row in csv_reader]
            file.close()
        
        return students