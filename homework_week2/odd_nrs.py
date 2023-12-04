# Write a function that takes a list of numbers and appends only the odd numbers to a new list.
# Return the new list.
def odd_numbers(list):
    odd_numbers=[]
    for i in list:
        if i % 2 != 0:
            odd_numbers.append(i)
    return odd_numbers

list = [1,2,3,4,5,6,7,8,9,10]
print(odd_numbers(list))
