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


