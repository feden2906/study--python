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
# from collections import namedtuple
#
# Player = namedtuple('Player', 'name age yearBorn')
# player1 = Player('Maksym', 25, 1995)
# player2 = Player('Alina', 25, 1995)
# player3 = Player('Dina', 10, 2011)
# player4 = Player('Alfred', 35, 1324)
# player5 = Player('Tamara', 88, 1932)
#
# print(player1)              # Player(name='Maksym', age=25, yearBorn=1995)
# print(player2.name)         # Alina
# print(player3.yearBorn)     # 2011


#


# # # CLASS # # #
# class User(object):
# class User:
#     name = 'Maksym'
#
#     def hello(self):
#         print(f'Hello {self.name}')
#
# user1 = User()
# user2 = User()
#
# user1.name = 'Kokos'
# user2.name = 'Adolf'
#
# print(user1.name)
# print(user2.name)


# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def __str__(self):
#         return f'{self.brand} -- {self.model} -- {self.year}'
#
#     def __repr__(self):
#         return f'{self.brand} -- {self.model} -- {self.year}'
#
#     def get_model(self, location):
#         return f'Автомобіль {self.model} знаходиться в місті {location}.'
#
# car = Car('BMW', 'X6', 2015)
# print(car)
# print(car.get_model('Madrid'))
#
# list = [Car('BMW', 'X6', 2015), Car('Audi', 'A6', 2010)]
# print(list)


#


# # # Наслідування # # #
# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def __str__(self):
#         return f'{self.brand} -- {self.model} -- {self.year}'
#
#     def __repr__(self):
#         return f'{self.brand} -- {self.model} -- {self.year}'
#
#     def get_model(self, location):
#         return f'Автомобіль {self.model} знаходиться в місті {location}.'
#
#
# class ElectroCar(Car):
#     def __init__(self, brand, model, year, acuma, charge):
#         super().__init__(brand, model, year)
#         self.acuma = acuma
#         self.charge = charge
#
#     def __str__(self):
#         return f'{self.brand} -- {self.model} -- {self.year} -- {self.acuma} -- {self.charge}'
#
#     def __repr__(self):
#         return f'{self.brand} -- {self.model} -- {self.year} -- {self.acuma} -- {self.charge}'
#
# tesla = ElectroCar('Tesla', 's3', 2018, '200000A', 'QuickCharge5')
# print(tesla)


#


# # # Численне наслідування # # #
# class Car:
#     def driving(self):
#         print('driving')
#
# class Boat:
#     def swimming(self):
#         print('swimming')
#
# class Amfibia(Car, Boat):
#     pass
#
#
# amfibia1 = Amfibia()
# amfibia1.driving()
# amfibia1.swimming()
