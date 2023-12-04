#1. Add new print statement - on a new line
# which saus 'We hear you like the color xxx! xxx is a string with color
#2. extend the function with another input parameter 'color', that defaults to 'red'
#3. Capture the color via input box as variable:color
#4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday adding 1 to the age
#5. Capitaliza first letter of the 'name', and rest are small caps
#6. Favorite color should be lowercase
def greeting(name, age, color = 'red'):
    print('Hello ' + name.capitalize() + ', you will be ' + str(age+1) + ' next birthday!')
    print(f'Hello {name.capitalize()}, you will be {age+1} next birthday!')
    print(f'We hear you like the color {color.lower()}!')

name = input('Enter your name: ')
age = input(('Enter your age: '))
color = input('What is your favourite color: ')
greeting(name, int(age), color)





