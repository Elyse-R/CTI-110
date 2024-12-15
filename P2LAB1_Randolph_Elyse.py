#Elyse Randolph
#October 5 2024
#P2LAB1
#Program takes user input radius to calculate the diameter, circumference, and area of a circle
radius = float(input("What is the radius of the circle? "))
print("The diameter of the circle is",f'{2*radius:.1f}')
print("The circumference of the circle is",f'{2*3.1415926*radius:.2f}')
print("The area of the circle is", f'{3.1415926*radius**2:.3f}')
