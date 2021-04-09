# # Типи даних
# i = 33333333333333333333333333333333333333333333333333333
# f = 1.3
# b = True
# s = 'text'
# n = None

# a = c = 10
# print(a, c)
# print(type(i))


# # math operation
# a = 0
# a -= 1
# a += 1
# a /= 1

# print(5 + 2)
# print(5 - 2)
# print(5 * 2)
# print(5 / 2)  # завжди повернає float
# print(5 // 2)  # обрізає після '.' все, робить int
# print(5 % 2)  # повертає залишок від ділення
# print(5 ** 2)  # степень


# num = input('Enter your number: ')  # повертає строку
# i = int(num)
# print(type(i))


# # методи перетворення типів даних ( спробують перевести тип даних, якщо не вийде app падає )
# int()
# float()
# str()
# bool()


# # LIST аналог масива
# l = [1, 2, 3, 4, 5]
# print(len(l))


# l = [1, 2, 3, 4, 5]
# l.insert( 4, 55)

# l = [1, 2, 3, 4, 5]
# l[7] = 555
# print(l)


# l = [1, 2, 3, 4, 5, 3, 3, 5, 7, 8, 9, 6, 4]
# l2 = l.index()
#
# print(l2)
# l2[0] = 100
# print(l1, l2)
# l2 = [8, 9, 10]
# l.append(1)
# # l.append(2)
# l.insert(30, 222)
# # pop = l.pop()
# pop = l.pop(8)
# l.remove(2)
# l.extend(l2)
# print(l.index(2, 3))
# l.reverse()
# l.sort(reverse=True)
# print(l)
# print(l.count(3))
# copy = l.copy()
# print(copy)
# l1 = [1, 2, 3, 4, 2, 3, 4, 5, 6, 7, 8]
# print(l1[::3])

# l = list(range(6, 35))
# print(l)


#


# # logical operators
# a = 4
# b = 5
#
# print(a is b)
# print(a == b)
#
# print(a is not b)
# print(a != b)
#
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)


#


# # conditions
# a = 4
# b = 5
# if a < b:
#     print('a is biggest')
# elif a > b:
#     print('b is biggest')
# elif a == b:
#     print('a = b')
# else:
#     print('bad request')

# a = 4
# if {a}:
#     print(True)
# else:
#     print(False)

# a = 8
# b = 6
# print('yes') if a > b else print('no')


#


# # dict
# create
# dict1 = {True: [1, 2, 3], 'age': 15, 'status': False}
# dict2 = dict(true=[1, 2, 3], age=15, status=False)

# methods
# print(dict1[True])
# print(dict1.get('age', 25))

# del dict1['age']
# dict1.pop('age', None)

# dict1.setdefault('age1', 25)

# print(list(dict1.values()))
# print(list(dict1.items()))

# dict.fromkeys(['qwe', 'www'], 'piska')

# dict1.update({'qwe': 'www', True: 3456})
# print(dict1)

# print(dict1.keys())
# print(dict1)


#


# # Цикли
# i = 0
# while i < 10:
#     print(i)
#     i += 1
# else:
#     print('Finish')


# for i in range(100):
#     print(i, end=' - ')

# dict1 = {True: [1, 2, 3], 'age': 15, 'status': False}
# for key, value in dict1.items():
#     print(key, value)

# list1 = [12.3, 4, 6.6, 4, 2, 5, 7.5]
# for i in list1:
#     print(i)
