# From the string 'Welcome to Python 101: Strings', extract text and create/print a new string that says:
# * '1 Welcome Ring To Tyler'
# * Every first letter in a word should be capitalized
string = 'Welcome to the Python 101: Strings'
new_msg=string[22]+' '+string[0:8]+string[-5:-1]+' '+string[8:11]+string[8]+string[16]+string[2]+string[1]+string[-5]
print(new_msg.title())


# Print the same string backwards and every first letter in a word should be capitalized
print(new_msg[::-1].title())
