# # # destructuring # # #
# tuple1 = (1, 2, 3, 4, 5, 6)
# a, b, *other = tuple1
# print(a)
# print(b)
# print(other)

# a = 5
# b = 6
# a, b = b, a
# a, b = (b, a)
# print(a)
# print(b)

# def function(a='a', b='b', c='c'):
#     return (a, b, c)
#
# print(function(c=1))

# def function(a='a', b='b', c='c'):
#     return (a, b, c)
#
# dict1 = {'a':1, 'b':5}
# print(function(**dict1))


#


# # # IMPORT # # #
# import file_name as ll        # import всього файлу пріоритетніший № 1
#
# from file_name import *       # import всього файлу пріоритетніший № 2


#


# # # namedtuple # # #
from collections import namedtuple

Player = namedtuple('Player', 'name age yearBorn')
player1 = Player('Maksym', 25, 1995)
player2 = Player('Alina', 25, 1995)
player3 = Player('Dina', 10, 2011)
player4 = Player('Alfred', 35, 1324)
player5 = Player('Tamara', 88, 1932)

print(player1)              # Player(name='Maksym', age=25, yearBorn=1995)
print(player2.name)         # Alina
print(player3.yearBorn)     # 2011


#

