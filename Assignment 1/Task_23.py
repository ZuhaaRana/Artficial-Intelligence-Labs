

# Task 22
# Write a python program to create a class. And do the following tasks
# i Make a class named Shape, Rectangle and Circle.
# ii In the class Shape there is a print function that tells which
# object is calling it and prints the class name.
# iii Also make 2 functions of area and perimeter in Rectangle and 
# Circle class.
# iv Display the name of both classes using the print function in 
# class
# Shape and also the calculations of each function of their respective
# classes.

import math as M
class SHAPE:
    def display_class_name(self):
        print(f"The name of this class is : {self.__class__}")

class RECTANGLE(SHAPE):

    def input_values(self):
        self.length = int(input('Enter length to find area and perimeter : '))
        self.width = int(input('Enter width to find area and perimeter :  '))

    def Area(self):
        area_of_re4ctangle = self.width * self.length
        return area_of_re4ctangle

    def Perimeter(self):
        perimeter_of_rectangle = 2 * (self.width + self.length)
        return perimeter_of_rectangle


class CIRCLE(SHAPE):

    def input_values(self):
        r = int(input('Enter radius of circle to find the area and perimeter : '))
        self.radius = r

    def Area(self):
        #area is pie r square
        area_of_the_circle = M.pi * self.radius * self.radius
        return area_of_the_circle


    def Perimeter(self):
        #perimeter is 2 pie r
        perimeter_of_circle = 2 * M.pi * self.radius
        return perimeter_of_circle

rectangle = RECTANGLE()
rectangle .display_class_name()
rectangle .input_values()

print("Area of rectangle is :",rectangle.Area())
print("Perimeter of rectangle is : ",rectangle.Perimeter())
print()
print()

circle = CIRCLE()
circle .display_class_name()
circle .input_values()

print("Area of circle is : ",circle.Area())
print("Perimeter of circle is : ",circle.Perimeter())
