names = ['john', 'ClEEse', 'Eric','IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

# You are having a party and want to invite your friends.
# You want to print out invitations for each friend using for loops
# The names are in two lists, 'names' and 'names1'
# You also need to add two extra names to the list using na 'input" box when you run the code
# Printout one invitation to each friend per line
# Names should be properly capitalized
# Example: John Cleese! You are invite to the party on Saturday.
# Hint: you may need two for loops

msg = 'You are invited to the party on Saturday.'
names.extend(names1)
# names = names + names1
# names += names1
for index in range(2):
    names.append(input('Enter a name to a friend to invite him to the party: '))

for name in names:
    inv = f'{name.title()}! {msg}'
    print(inv)
