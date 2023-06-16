

# Task 21
# From Task 20 you have to create lists of objects, dictionary of
# objects and tuples of objects.
# Compare these objects if they are equal or not. Also print each 
# objects values from different data-structures.

class Student:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.age = 20
        self.cnic= 0
        self.courses = []
        self.gender = ""
        self.CGPA = 0.00
        self.SGPA = 0.00
        self.current_credit_hours = 0

    def get_first_name(self):
        return self.first_name
    def set_first_name(self, F):
        self.first_name = F

    def get_last_name(self):
        return self.last_name
    def set_last_name(self, L):
        self.last_name = L

    def get_age(self):
        return self.Age
    def set_age(self, A):
        self.Age = A

    def get_cnic(self):
        return self.cnic
    def set_cnic(self, C):
        return self, C.cnic

    def get_courses(self):
        return self.courses
    def set_courses(self, COURSE):
        return self, COURSE.courses

    def get_gender(self):
        return self.gender
    def setGender(self, G):
        return self, G.gender

    def get_CGPA(self):
        return self.CGPA
    def set_CGPA(self, cgpa):
        return self, cgpa.CGPA

    def get_SGPA(self):
        return self.SGPA
    def set_SGPA(self, sgpa):
        self.SGPA = sgpa

    def get_current_credit_hours(self, value):
        self.current_credit_hours = value
    def set_current_credit_hours(self, value):
        self.current_credit_hours = value
