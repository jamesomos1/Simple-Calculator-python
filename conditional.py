# if = Do some code only IF some condition is True
#       Else do something else

age = int(input('Enter your age: '))

if age >= 21:
    print('You are old enough to drink')
elif age < 21:
    print('You are still a small boy')

name = input('Enter your name: ')

if name == '':
    print('Enter a name please')
else:
    print(f'Wassup witch {name}') 

online = False

if online:
    print('You are online')
else:
    print('You are offline')