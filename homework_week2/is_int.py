# Create a function that returns True if the argument is an integer and False to any other type of data

user_input = input("Enter number or a text: ")

if user_input.isdigit():
    print('True')
else:
    print('False')

