class Person:
    def __init__(self, name, age, address):
        self._name = name
        self._age = age
        self._address = address

    def __str__(self):
        return_string = f"Name: {self._name}\n"
        return_string += f"Age: {self._age}\n"
        return_string += f"Address: {self._address}\n"

        return return_string
    
class Student(Person):
    def __init__(self, name, age, address, student_id, grade_level):
        Person.__init__(self, name, age, address)
        self._student_id = student_id
        self._grade_level = grade_level

    def __str__(self):
        return_string = f"Name: {self._name}\n"
        return_string += f"Age: {self._age}\n"
        return_string += f"Address: {self._address}\n"
        return_string += f"Student ID: {self._student_id}\n"
        return_string += f"Grade level: {self._grade_level}\n"

        return return_string
    

class Employee(Person):
    def __init__(self, name, age, address, salary, experience):
        Person.__init__(self, name, age, address)
        self._salary = salary
        self._experience = experience

    
    def __str__(self):
        return_string = f"Name: {self._name}\n"
        return_string += f"Age: {self._age}\n"
        return_string += f"Address: {self._address}\n"
        return_string += f"Salary: ${self._salary:,.2f}\n"
        return_string += f"Years on the job: {self._experience}\n"

        return return_string
    
class Faculty(Employee):
    def __init__(self, name, age, address, salary, experience, faculty_id, subject_taught):
        Employee.__init__(self, name, age, address, salary, experience)
        self._faculty_id = faculty_id
        self._subject_taught = subject_taught

    def __str__(self):
        return_string = f"Name: {self._name}\n"
        return_string += f"Age: {self._age}\n"
        return_string += f"Address: {self._address}\n"
        return_string += f"Salary: ${self._salary:,.2f}\n"
        return_string += f"Years on the job: {self._experience}\n"
        return_string += f"Faculty ID: {self._faculty_id}\n"
        return_string += f"Subject taught: {self._subject_taught}\n"

        return return_string




def main():

    person = Person("Khoa Hoang", 25, "13691 Sutter Dr")
    student = Student("Ethan Nguyen", 20, "131 N Grant Pl", "01943581", "Freshman")
    employee = Employee("Thao Ngan Tran", 20, "9052 Vons Dr", 25000, 5)
    faculty = Faculty("Terry Duong", 35, "8027 Westminster Ave", 200000, 20, "F12345", "Python Advance")

    print(person)
    print(student)
    print(employee)
    print(faculty)

main()