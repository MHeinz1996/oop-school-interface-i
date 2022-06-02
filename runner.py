from classes.school import School 
from classes.student import Student
from classes.staff import Staff

school = School('Ridgemont High') 

print(school.name)

# student_info = {'name': 'Diana', 'password': 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}
# Student(**student_info) # This syntax allows us to send a dict of kwargs through the class to init the instance
# print(Student.all_students())
# print(Staff.all_staff())