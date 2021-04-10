# # # SET # # #
# set_1 = {1, 3, 4, 5, 7, 6, 4, 3, 3, 3, 2}
# set_2 = {7, 7, 6, 5, 6, 7, 5, 4, 3, 3, 1}
# print(set_1)
#

# # Створюють новий сет, не мутують
# set_1 = {1, 3, 4, 5, 7, 6, 4, 3, 3, 3, 2}
# set_2 = {7, 6, 5}
#
# print(set_1.issuperset(set_2))
# print(set_2.issubset(set_1))
#
# print(set_1.isdisjoint(set_2))
# print(set_1.intersection(set_2))
#
# print(set_1.difference(set_2))
# print(set_1.symmetric_difference(set_2))
#

# # Мутують той сет на якому були викликані
# set_1 = {1, 3, 4, 5, 7, 6, 4, 3, 3, 3, 2}
# set_2 = {7, 6, 5, 55}

# set_1.update(set_2)
# print(set_1)

# set_1.remove(4)
# print(set_1)

# set_1.discard(4)
# print(set_1)

# set_1.pop()
# print(set_1)


#


# # # STRING # # #
# name = 'Max'
# age = 25
# weight = 75.5
#
# string = 'Hello, my name is ' + name + ', I`m ' + str(age) + ' and my weight - ' + str(weight) + ' kg.'
# string = 'Hello, my name is %s, I`m %d and my weight - %f kg.' % (name, age, weight)
# string = 'Hello, my name is {}, I`m {} and my weight - {} kg.'.format(name, age, weight)
# string = f'Hello, my name is {name}, I`m {age} and my weight - {weight} kg.'
# print(string)

# print(string.index('Ma', 2, 12))
# print(string.find('l'))
# print(string.count('e', 5, 55))
# print(string.capitalize())
# print(string.upper())
# print(string.lower())
# print(string.title())
# print(string.swapcase())

# string = '-     aaBadaafagah aDad  a - fag -ha,a a-kaFfagaah-alal'
# print(string.isalpha())
# print(string.isdigit())
# print(string.isalnum())
# print(string.isspace())
# print('5.5'.isdecimal())
# print(string.isdecimal())
# print(string.istitle())

# print(string.startswith('ll'))
# print(string.endswith('ll'))

# print(string.strip())
# print(string.split(' '))
# print(string.partition('-'))

# li = ['apple', 'car', 'user']
# string = ' * '.join(li)
# print(string)

# print(string.replace('ll', 'ss', 1))


#


# # # list comprehension # # #
# list1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list1)

# list2 = [[1, 2, 3, 4, 5], [4, 5, 6, 7, 5, 3, 2, 9]]
# newList = [i for j in list2 for i in j]
# print(newList)

# list3 = [1, 2, 3, 4, 5, 4, 5, 6, 7, 5, 3, 2, 9]
# newList = ['even' if i % 2 == 0 else 'odd' for i in list3]
# print(newList)

# dict1 = {'NaMe': 'Maksym', 'aGe': 25}
# dict2 = {k.lower(): v for k, v in dict1.items()}
# print(dict2)

# list4 = [1, 2, 3, 4, 5, 4, 5, 6, 7, 5, 3, 2, 9]
# set1 = {i for i in list4}
# print(set1)
