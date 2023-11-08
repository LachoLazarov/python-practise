msg = 'Welcome to Python 101: Split and Join'
csv = 'Eric, John, Michael, Terry, Graham'
friends_list = ['Eric', 'John', 'Michael', 'Terry', 'Graham']

print(csv.split(','))
print(''.join(friends_list))

print(''.join(msg.split()))
print(msg.replace(' ', ''))

# From the list below fill a list (friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Exercise: fill me with names']
print(friends_list)

print((','.join(','.join(csv.split(';')).split(':'))).split(','))
friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',')
print(friends_list)

print('replace', csv.replace(';',',').replace(':',',').split(','))