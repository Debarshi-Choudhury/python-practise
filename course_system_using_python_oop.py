class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        sum=0
        for student in self.students:
            sum += student.get_grade()
        return sum/len(self.students)

    
s1=Student("Harry", 19, 85)
s2=Student("Hermione", 19, 95)
s3=Student("Ron", 19, 65)

c1 = Course("science", 3)

c1.add_student(s1)
c1.add_student(s2)
print(c1.get_average_grade())
c1.add_student(s2)
print(c1.get_average_grade())