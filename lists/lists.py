people = ['John' , 'Michael', 'Terry' , 'Eric', 'Graham']
cars = [911, 130, 328, 535, 740, 308]
print(people)
people.sort()
print(people)
people.reverse()
print(people)
print(min(cars))
print(max(people))
people.append('Lacho')
print(people)
people.insert(1,'Billy')
print(people)
people[0] = 'Denzel'
print(people)
people.extend(cars)
print(people)
people.remove('Lacho')
print(people)
people = ['John' , 'Michael', 'Terry' , 'Eric', 'Graham']
people.pop(-1)
print(people)
people = ['John' , 'Michael', 'Terry' , 'Eric', 'Graham']
people.clear()
print(people)

people1 = ['John' , 'Michael', 'Terry' , 'Eric', 'Graham']
del people1[2]
print(people1)

people2 = ['John' , 'Michael', 'Terry' , 'Eric', 'Graham']
new_people = people2.copy()
print(new_people)

people3 = ['John' , 'Michael', 'Terry' , 'Eric', 'Graham']
ew_people = list(people3)
print(new_people)