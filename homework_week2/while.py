# Use a generator (while) to multiply by 2 input values
def multiply_by_two(values):
    i = 0
    while i < len(values):
        yield values[i] * 2
        i += 1

input_numbers = [1,2,3,4,5]
result_gen = multiply_by_two(input_numbers)
for result in result_gen:
    print(result)
