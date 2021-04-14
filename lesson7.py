# # # ТИПІЗАЦІЯ # # #
# def concat(name: str, surname: str) -> str:
#     return 2                                           # підкреслює якщо не вірний тип даних, але повертає


# class User:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     def __repr__(self):
#         return str(self.__dict__)
#
#
# def create_user(name: str, age: int) -> User:
#     return User(name.title(), age)
#
#
# user1 = create_user('maksym', 25)
# print(user1)


# class User:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     def __repr__(self):
#         return str(self.__dict__)
#
#
# from typing import List
#
# def create_user(arr1: List[str], arr2: List[int]) -> List[User]:
#     users: List[User] = []
#     for i in range(len(arr1)):
#         users.append(User(arr1[i].title(), arr2[i]))
#
#     return users
#
#
# names = ['maksym', 'Tamara', 'Alina', 'Dimas']
# ages = [25, 16, 27, 23]
#
# print(create_user(names, ages))


#


# # # venv(віртуальне середовище розробки) # # #
# class User:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     def __repr__(self):
#         return str(self.__dict__)
#
#
# from typing import List
#
# def create_user(arr1: List[str], arr2: List[int]) -> List[User]:
#     users: List[User] = []
#     for i in range(len(arr1)):
#         users.append(User(arr1[i].title(), arr2[i]))
#
#     return users
#
#
# names = ['maksym', 'Tamara', 'Alina', 'Dimas']
# ages = [25, 16, 27, 23]
#
# print(create_user(names, ages))
#
# перевірку типів робимо командою - mypy lesson7.py
# попередньо mypy встановлене в venv
