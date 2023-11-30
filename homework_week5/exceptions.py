# Homework refactor calculator project with exception usage.
# Find out how to handle another data type problems like str in calculations or zero division problem.

def calculator():
    try:
        mode = input('Enter math operation (+, -, *, /) or "f" for Celsius to Fahrenheit conversion: ')
        first_nr = float(input('Enter a number: '))

        if mode.lower() == 'f':
            print(f'The temperature in Fahrenheit is: {first_nr * 9/5 + 32}')
        else:
            second_nr = float(input('Enter a second number: '))

            if mode == '+':
                result = first_nr + second_nr
            elif mode == '-':
                result = first_nr - second_nr
            elif mode == '*':
                result = first_nr * second_nr
            elif mode == '/':
                if second_nr == 0:
                    raise ValueError("Cannot divide by zero.")
                result = first_nr / second_nr
            else:
                raise ValueError("Invalid operator.")

            print(f'The answer is: {result}')

    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

calculator()
