# # # try # # #
# num = 0
#
# try:
#     result = 23456 / num
#     if num == 2:
#         raise Exception('message')
#
# except ValueError as value_err:
#     print(value_err)
#
# except ZeroDivisionError as zero_err:
#     print(zero_err)
#
# except Exception as err:
#     print(err)
#
# else:
#     print('Спрацьовує якщо блок try виконався успішно')
#
# finally:
#     print('Спрацьовує в будь-якому разі')


#


# # # read files # # #
# import os
# file_path = os.path.join('lesson6', 'lesson6.text.txt')
#
# file = open(file=file_path, mode='r')            # завантажуємо в пам'ять якусь сутність
# print(file)                                      # <_io.TextIOWrapper name='lesson6.text.txt' mode='r' encoding='cp1251'>
#
# file.seek(5)                                     # пробустить 5 байт
# file = file.read()
# file = file.read(5)                              # 5 байт // 1 байт == 1 символ
# file = file.readline()                           # читає 1 рядок + /n
# file = file.readline().rstrip()                  # читає 1 рядок
# file = file.readlines()                          # повертає list рядків
# print(file)


# # # write files # # #
# import os
# file_path = os.path.join('lesson6', 'lesson6.text.txt')
#
# file = open(file=file_path, mode='w')            # завантажуємо в пам'ять якусь сутність
# file.write('Fedenko Maksym\n')
#
# l = ['cat\n', 'dog\n', 'goose\n']
# file.writelines(l)
#
# file.close()


# # # append files # # #
# import os
# file_path = os.path.join('lesson6', 'lesson6.text.txt')
#
# file = open(file=file_path, mode='a')            # завантажуємо в пам'ять якусь сутність
# file.write('Fedenko Maksym\n')                   # додає в кінці файлу
#
# l = ['cat\n', 'dog\n', 'goose\n']
# file.writelines(l)                               # додає в кінці файлу
#
# file.close()


# # # конструкція яка автоматично закриває файл # # #
# import os
# file_path = os.path.join('lesson6', 'lesson6.text.txt')
#
# with open(file=file_path, mode='r') as file:                # за блоком with автоватично закривається файл
#     print(file.read())


#


# # # generators # # #
# list1 = [i for i in range(100000000000)]                    # приклад використання (процес помирає бо недостатньо ОЗУ)


# gen = (i for i in range(100000000000000000000))             # перебор по одному
# print(next(gen))
# print(next(gen))
# print(next(gen))


# gen = (i for i in range(100000000000000000000))             # перебор циклом
# for i in gen:
#     print(i)


# def gen(num):                                               # кастомний генератор
#     print('start')
#     while num >= 0:
#         yield num                                           # Якщо є "yield", то ця функція генератор
#         num -= 1
#
# g = gen(5)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# for i in gen:
#     print(i)

