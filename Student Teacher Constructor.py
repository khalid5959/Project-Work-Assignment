class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

# Example usage:
student1 = Student(name="Alice", age=20, student_id="S12345")
teacher1 = Teacher(name="Mr. Smith", age=35, subject="Math")

print(f"Student: {student1.name}, Age: {student1.age}, Student ID: {student1.student_id}")
print(f"Teacher: {teacher1.name}, Age: {teacher1.age}, Subject: {teacher1.subject}")
