import math

# exercise 1 - Circumference of circle
#Scan the input
result = float(input("Enter the radius of the circle: "))


#Circumference calculation

circumference = math.pi * 2 * result

#print circumference

print(f'The circumference of the circle is: {round(circumference, 2)} cm')

#exercise 2 - Area of Circle
#Scan the input

result1 = float(input("Enter the radius: "))

#Area calculation

area = math.pi * pow(result1, 2)

#print Area

print(f'The area of your circle is: {round(area, 2)} cm^2 ')

# exercise 3 - Finding hypotnuse

# Scan the inputs
q = float(input('Enter side A: '))
w = float(input('Enter side B: '))

# Hypotnuse calculation
e = math.sqrt(pow(q, 2) + pow(w, 2))

# print statement
print(f'Side C: {e}')