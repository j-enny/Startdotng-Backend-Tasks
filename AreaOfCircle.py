#Area of a circle calculator
import math

#the input function returns string value by default, hence we are to change the data type 
# float data type is used, as it can accept both intergers and floating numbers
radius = float(input("Please enter the area of your circle: "))

#the area of a circle is pi*radius^2
#python has a built in math module that provides #values for some math constants with pi being one of #them
area_of_circle = math.pi * (radius*radius)

print( "The area of the circle is : ",round(area_of_circle,2))

