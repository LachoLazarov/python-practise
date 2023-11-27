friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']
efriends = [(51,'Brian'), (52,'Judith'), (53,'Reg'), (54,'Loretta'), (55,'Colin')]

i = 51
for friend in friends:
    print(i, friend)
    i +=1
for num, friend in enumerate(friends, 51):
    print(num, friend)

print(type(enumerate(friends)))
