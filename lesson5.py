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
