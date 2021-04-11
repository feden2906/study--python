# # # приватність # # #
# class Animal:
#     _dich = 0                 # протект змінна
#     __count = 0               # приватна змінна
#
#     def __init__(self, name):
#         self.__name = name
#
# animal = Animal('Maksym')
# print(animal._Animal__name)


#


# # # інкапсуляція # # #
# class User:                                                 ## METHOD 1
#     def __init__(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         self.__name = name
#
#     def delete_name(self):
#         del self.__name
#
# user1 = User('Maks')
# print(user1.get_name())
# user1.set_name('Tamara')
# print(user1.get_name())
# print(user1.delete_name())


# class User:                                                 ## METHOD 2
#     def __init__(self, name):
#         self.__name = name
#
#     def __get_name(self):
#         return self.__name
#
#     def __set_name(self, name):
#         self.__name = name
#
#     def __delete_name(self):
#         del self.__name
#
#     my_name = property(fget=__get_name, fset=__set_name, fdel=__delete_name)
#
# user1 = User('Maksym')
# print(user1.my_name)                           # відпрацює fget
# user1.my_name = 'Alindos'                      # відпрацює fset
# print(user1.my_name)                           # відпрацює fget
# del user1.my_name                              # відпрацює fdel
# print(user1.__dict__)


# class User:                                                 ## METHOD 3  (top^)
#     def __init__(self, name):
#         self.__name = name
#
#     @property                                    # @property вішається на геттер! В наступних з'явиться декоратор "name"
#     def name(self):
#         return self.__name
#
#     @name.setter                                 # setter для запису
#     def name(self, name):
#         self.__name = name
#
#     @name.deleter                                # deleter для видалення
#     def name(self):
#         del self.__name
#
# user1 = User('Maksym')
# print(user1.name)
# user1.name = 'Alindos'
# print(user1.name)
# del user1.name
# print(user1.__dict__)


#


# # # полімофізм # # #
# class Shape:
#     def area(self):
#         print('Area', end=': ')
#
#     def perimetr(self):
#         print('Perimetr', end=': ')
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         super().area()
#         return self.a * self.b
#
#     def perimetr(self):
#         super().perimetr()
#         return (self.a + self.b) * 2
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def area(self):
#         super().area()
#         p = (self.a + self.b + self.c) / 2
#         return pow(p * (p - self.a) * (p - self.b) * (p - self.c), 0.5)
#
#     def perimetr(self):
#         super().perimetr()
#         return self.a + self.b + self.c
#
#
# shapes = [Rectangle(2, 4), Triangle(3, 3, 3), Triangle(1, 1, 1)]
#
# for shape in shapes:
#     print(shape.area())
#     print(shape.perimetr())


#


# # # abstract basic class # # #
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        print('Area', end=': ')

    @abstractmethod
    def perimetr(self):
        print('Perimetr', end=': ')


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        super().area()
        return self.a * self.b

    def perimetr(self):
        super().perimetr()
        return (self.a + self.b) * 2


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        super().area()
        p = (self.a + self.b + self.c) / 2
        return pow(p * (p - self.a) * (p - self.b) * (p - self.c), 0.5)

    def perimetr(self):
        super().perimetr()
        return self.a + self.b + self.c


shapes = [Rectangle(2, 4), Triangle(3, 3, 3), Triangle(1, 1, 1)]

for shape in shapes:
    print(shape.area())
    print(shape.perimetr())

