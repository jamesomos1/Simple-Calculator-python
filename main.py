
# This is my first Python program
print("I love basketball")
print("Its odee fun")

# Variable = a container for a value(string, integer, float, boolean)

# Strings
first_name = "James"
food = "CHICKEN WINGS"
email = "Jay.omos@gmail.com"

print(f"Wassup {first_name}")
print(f"Hey James i know you love {food}")
print(f"Your email is {email}")

# Integers

age = 22
count=4
num_of_students = 23

print(f"You are {age} years old")
print(f'You are buying {count} items')
print(f'There are {num_of_students} students in the classroom')

 # Float
price = 3.99

print(f'The price for juice is {price}')

# Boolean

is_student = False
is_online = False

print(f'Are you a student?: {is_student}')

if is_student:
    print("You are a student")
else:
    print("You are Not a student")

if is_online:
    print('You are online')
else:
    print('You are offline')

#Casting
 
student = True
grade = 99

student = str(student)
print(type(student))

grade = bool(grade)
print(grade)