name = input('What is your name: ')
age = input('What is your age: ')
print('Hello there ' + name + '!' + ' You are ' + age + ' years old!')

num1 = input('Enter a number: ')
num2 = input('Enter a second number: ')
answer = int(num1) + int(num2)
print(answer)

# Distance converter converting kilometers to miles
#Take two inputs from user:
# Their first name and the distance in km
# Print: Greet user by name and show km, and mile values
# 1 mile is 1.609 kilometers
name1 = input('What is your name: ')
km = input('How many kilometers have you run: ')
mile = float(km)/1.609
print(f'Hello {name1.capitalize()}! You have run {km} kilometers or {round(mile,0)} miles')
