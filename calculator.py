run = True
while run: 

    user = input('Enter an operator (+, -, *, /): ')

    if user in ('+', '-', '*', '/'):

        num1 = float(input('Enter your first number: '))
        num2 = float(input('Enter your second number: '))

        if user == '+':
            print("Your number is:", round(num1 + num2, 3))
            break
        elif user == '-':
            print("Your number is:", round(num1 - num2, 3))
            break
        elif user == '*':
            print("Your number is:", round(num1 * num2, 3))
            break
        elif user == '/':
            print("Your number is:", round(num1/num2, 3))
            break
    else:
      print(f"{user} is not an option")


