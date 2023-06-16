

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

def Input(self):
        print()
        print()
        self.first_name = input("Please Enter first name : ")
        self.last_name = input("Please Enter last name : ")
        self.age = int(input("Please Enter your age : "))
        self.cnic = int(input("Enter your CNIC no : "))
        self.gender = str(input("Please Enter your gender : "))
        self.CGPA = float(input("Enter your CGPA : "))
        self.SGPA = float(input("Enter your SGPA : "))
        self.current_credit_hours = int(input("Enter your current credit hours : "))
        i = 1
        while i != 0:
            self.courses.append(input("Please Enter a Course you want to register : "))
            i = int(input("Do you want to enter another Course. Press any number for yes except 0 : "))

    def Display_student_data(self):
        print(f"First Name = {self.first_name}")
        print(f"Last Name = {self.last_name}")
        print(f"Age = {self.age}")
        print(f"CNIC = {self.cnic}")
        print(f"self.courses = {self.courses}")
        print(f"self.gender = {self.gender}")
        print(f"self.CGPA = {self.CGPA}")
        print(f"self.SGPA = {self.SGPA}")
        print(f"self.Current_Credit_Hours = {self.current_credit_hours}")

def Display_All_Students(self, Students):
        if len(Students) == 0:
            print("\nNo Student with such CNIC found.")
            return
        for i in Students:
            i.Display_student_data()

    def Add_Student_data(self, Students):
        NEW_STUDENT = Student()
        NEW_STUDENT.Input()
        Students.append(NEW_STUDENT)

def Delete_Student_data(self, cnic, Students):
        DEL = self.Search_Student(cnic, Students)
        if DEL != 0:
            print("\nStudent record deleted.")
            Students.remove(DEL)
        else:
            print("\nThere is no student with such CNIC.\n")

    def Search_Student(self, cnic, Students):
        for i in Students:
            if i.cnic == cnic:
                return i
        return 0
