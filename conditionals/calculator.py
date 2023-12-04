# Create a calculator which handles +,-,*,/ and outputs answer based on mode/ operator used
# Hint: use 3 separate inputs
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in fahrenheit

mode = input('Enter math operation(+,-,*,/) or f for Celcius to Fahrenheit conversion: ')
first_nr = float(input('Enter a number: '))
if mode.lower() == 'f':
    print(f'First number Celcius entered is equivalent to: {first_nr * 9/5 + 32} Fahrenheit!' )
else:
    second_nr = float(input('Enter a second number: '))

    if mode == '+':
     print(f'The sum is: {first_nr + second_nr}')
    elif mode == '-':
        print(f'The anwser is: {first_nr - second_nr}')
    elif mode == '*':
        print(f'The anwser is: {first_nr * second_nr}')
    elif mode == '/':
     print(f'The anwser is: {first_nr / second_nr}')
    else:
     print('Input error!')
