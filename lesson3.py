# # # ZIP # # #
# l1 = ['Maks', 'Karina', 'Anton']
# l2 = [14, 15, 45]
# l3 = [11, 22, 33]
# data1 = dict(zip(l1, l2))
# data2 = tuple(zip(l1, l2, l3))
# print(data1)
# print(data2)


#


# # # function # # #
# def hello_world():
#     print('Hello world')
#
# hello_world()

# def hello_world(a, b, *args, **kwargs):
#     print(a, b, args, kwargs)
#
# hello_world(1, 2, 3, 4, 5, name='Maks')

# list1 = [1, 2, 3]
# dict1 = {'name': 'Maks', 'age': 13, 'gender': 'male'}
#
# def function1(a, b, c):
#     print(a, b, c)
#
# function1(*list1)                 # take list item
# function1(*dict1)                 # take dict keys


#


# # # closure # # #
# x = 5
#
# def function2():
#     global x
#     x += 1
#     print(x)
#
# function2()
# print(x)

# def function3():
#     count = 0                             # не задіяна
#
#     def wrap1():
#         count = 5                         # не задіяна
#
#         def wrap2():
#             nonlocal count                # шукає змінну на попередньому рівні
#             count += 1
#             print(count)
#
#         return wrap2
#     return wrap1
#
# function3()()()


# def counter():
#     count = 0
#
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#
#     return increment
#
# event = counter()
# print(event())
# print(event())
# print(event())
# print(event())
# print(event())


#


# # # decorator # # #
# def greeting():
#     print('Hello world')
#
# def decor(func):
#     print('------------------------')
#     func()
#     print('------------------------')
#
# decor(greeting)


# def decor1(func):
#     def wrapper():
#         print('------------------------')
#         func()
#         print('------------------------')
#     return wrapper
#
# def decor2(func):
#     def wrapper():
#         print('************************')
#         func()
#         print('************************')
#     return wrapper
#
# @decor1
# @decor2
# def greeting():
#     print('Hello world')
#
# greeting()


# def decor1(func):
#     def wrapper(*args, **kwargs):
#         print('******************************************************')
#         func(*args, **kwargs)
#         print('******************************************************')
#     return wrapper
#
#
# @decor1
# def greeting(name, age, weight):
#     print(f'Hello {name}, you have {age} years. Your weight - {weight} kg')
#
#
# greeting('Maksym', 25, 75.5)


#
