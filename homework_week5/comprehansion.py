# Write a function that takes a list of numbers and appends only the odd numbers to a new list.
# Return the new list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filter_odd_numbers(input_list):
    return [num for num in input_list if num % 2 != 0]

result = filter_odd_numbers(numbers)
print(result)
