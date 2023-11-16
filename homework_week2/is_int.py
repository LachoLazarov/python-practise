# Create a function that returns True if the argument is an integer and False to any other type of data
# I am not sure of this - need clarifications!
def is_integer(argument):
    return type(argument) == int

argument_a = is_integer(3)
argument_b = is_integer("Test text")
print(argument_a)
print(argument_b)
