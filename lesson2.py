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

