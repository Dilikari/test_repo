# 1Выведите все элементы, которые меньше 5.
# a = [1, 1, 2, 3, 6, 9, 77, 55, 99, 5]
# for elem in a:
#     if elem <= 5:
#         print(elem)

# 2Нужно вернуть список, который состоит из
# элементов, общих для этих двух списков
# a = [1, 1, 2, 3, 6, 9, 77, 55, 99, 5]
# b = [1, 5, 8, 9, 6, 3, 2, 1, 5, 5, 9, 2, 11, 5, 6]
# result = list(filter(lambda elem: elem in a,b))
# print(result)

import operator

# 3 d = {1: 2, 5: 8, 9: 2, 1: 2, 3: 1} #Отсортируйте словарь по
# значению в порядке возрастания и убывания.
# print(d)

# 4Напишите программу для слияния нескольких словарей в один.
# dict_a = {1:2, 2:4, 4:5}
# dict_b = {33: 3, 5:4 }
# dict_c = {55: 66, 77:8}
# result = {}
# for dict_f in (dict_a, dict_b, dict_c):
#     result.update(dict_f)
#     print(dict_f)

# 5Найдите три ключа с самыми высокими значениями в словаре my_dict =
# ={'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
# print(result)

# 6Напишите код, который переводит целое число в строку, при том что
# его можно применить в любой системе счисления.
# a = 16
# print(int('ABC', 16))

# 8 def is_polindrom(string):
#    return string == ''.join(reversed(string))
# print(is_polindrom('adda'))
#    #2 вариантНапишите проверку на то, является ли строка палиндромом.
# def is_polindrom(string):
#     return string == string[::-1]
# print(is_polindrom("adda"))

# 9Сделайте так, чтобы число секунд отображалось
# в виде дни:часы:минуты:секунды.
# def convert(seconds):
#     days = seconds // (24 * 3600)
#     seconds %= 24 * 3600
#     hours = seconds //3600
#     seconds %= 3600
#     minutes = seconds // 60
#     seconds %= 60
#     print(f"{days}:{hours}:{minutes}:{seconds}")
# convert(1234565)

# 10Вы принимаете от пользователя последовательность чисел, разделённых
# запятой. Составьте список и кортеж с этими числами.
# values = input('введите числа через запятую: ')
# ints_as_string = values.split(",")
# ints = map(int, ints_as_string)
# lst = list(ints)
# tup = tuple(lst)
# print('список:', lst)
# print('кортеж:', tup)

# #11Выведите первый и последний элемент списка.
# lst = [1, 2, 58, 9, 6, 6, 3, 6]
# print(f'first{lst[0]}; last; {lst[-1]}')


# списки
# numbers = [2, 5, 69, 9, 6, 33, 3, 2, 2, 555, 5, 5, 5]
# string = list("tproger")
# print(numbers)
# print(string)
#
# numbers = [i for i in range(1, 8)]
# print(numbers)

# numbers = [5, 8, 1, 6, 3, 8]
# print(numbers.index(1))
#
# numbers = [5, 8, 1, 6, 3, 8, 1]
# print(numbers.count(1))

# numbers = [5, 8, 1, 6, 3, 8, 1]
# numbers.append(4)
# print(numbers)
#
# numbers = [5, 8, 1, 6, 3, 7, 2, 4]
# numbers.sort()
# print(numbers)
#
# numbers = [5, 8, 1, 6, 3, 7, 2, 4]
# numbers.sort(reverse= True)
# print(numbers)

# numbers = [5, 8, 1, 6, 3, 7, 2, 4]
# numbers.sort(reverse=True)
# print(numbers)
#
# Вставляет элемент перед указанным индексом
# numbers = [5, 8, 1, 6, 3, 7, 2, 4]
# numbers.insert(3, [2, 4])
# print(numbers)

# Удаляет первое попавшееся вхождение элемента в списке Python:
# numbers = [5, 8, 1, 6, 3, 7, 2, 4]
# numbers.remove(1)
# print(numbers)

# #Подобно методу append(), добавляет элементы,
# numbers = [5, 8, 1, 6, 3, 7, 2, 4]
# numbers.extend([10, 9])
# print(numbers)

# numbers = [5, 8, 1, 6, 3, 7, 2, 4]
# numbers.pop(1)
# print(numbers)
#
# Преобразовывает список в строку. Разделитель
# элементов пишут в кавычках перед методом,
# а сам список Питона должен состоять из строк:
# mylist = ['сайт', 'типичный', 'программист']
# print(', '.join(mylist))

# line = [1, 2, 5, 6, 44, 6, 6]
#
# img = [[1, 2, 8, 9, 13, 3, 32], [1, 2, 8, 9, 13, 3, 32], [1, 2, 8, 9, 13, 3, 32], [1, 2, 8, 9, 13, 3, 32],
#        [1, 2, 8, 9, 13, 3, 32]]
# print(img)
#
# img = [line[:], line[:], line[:], line[:], line[:]]
# print(img)
# print(img[0])
# print(img[0][1])
#
# img[1] = [0, 0, 0, 0, 0, 0, 0, 0]
# print(img)
#
# img[1] = [0] * 5
# print(img)
#
# t = [["салам", "алекум", "хахаха", "не", "догонеш"],
#      ["не", "догонеш", "ты", "сильно", "слаб"],
#      ["ты", "очень", "слаб", "я", "очень"],
#      ["крутой", "прогер"]
#      ]
# print(t)
# print(t[0])
# print(t[0][2])
# t[0][2] = 'Dilik'
# print(t[0])
# t.append(["Твоих", "оград", "узор", "чугунный"])
# print(t)
# del t[1]
# print(t)
#
# A = [[[True, False], [1, 2, 3]], ["матрица", "вектор"]]
# print(A)
# print(A[0])
# print(A[1])
# print(A[0][1][0])

# , x = -4
# if x < 0:
#     x =- x
# print(x)
#
# a = float(input("a: "))
# b = float(input("b: "))
# if a < b:
#     a, b = b, a
#
# print(a ,b)

# a = 6
# b = 2
#
# res = a + 3 if a > b else b -4
# print(res)
#
# s = "python"
# t = "upper"
# res = s.upper() if t == "upper" else s
# print(res)


# i = 1
# while i < 10:
#     print(i)
#     i += 1

# pass_true = "password"
# ps = ""
#
# while ps != pass_true:
#     ps = input("enter u pass: ")
# print("log in")

# N = 20
# i = 1
#
# while i <= N:
#     if i %  3 == 0:
#         print(i)
#
#     i += 1
#
# d = [4, 5, 99, 9, 33, 1, 1, 1, 5]
# flFind = False
# i = 0
# while i < len(d):
#      flFind = d[i] % 2 == 0
#      if flFind:
#          break
#      i += i
#
# print(flFind)
#
# s =0
# d = 1
# while d != 0:
#     d = int(input("enter u number"))
#     if d % 2 !=0:
#         #continue
#         s += d
#         print(" s = " + str())

# def solve(n):
#     n1 = n
#     n2 = int(str(n) * 2)
#     n3 = int(str(n) * 3)
#     print(n1 + n2 + n3)
#
#
# solve(5)

# 14Напишите программу, которая выводит чётные числа из
# заданного списка и останавливается, если встречает число 237.
# n = [823, 566, 597, 978, 328, 615, 953, 345, 237,
#      399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,237,
#      ]
# for x in n:
#     if x == 237:
#         break
#     elif x % 2 == 0:
#         print(x)

# Напишите программу, которая принимает
# два списка и выводит все элементы первого, которых нет во втором.
# set_1 = set(['white', 'black', 'yellow'])
# set_2 = set(['red', 'black', 'yellow'])
# print(set_1 - set_2)

# for x in list(range(-67, 0, 6)):
#     print(x)

# d = [5, 8, 5, 6, 6, 9, 8]
# p = 1
# for i in list(range(7)):
#     d[i] = 0
# print(d)

# Посчитайте, сколько раз символ встречается в строке.
# string = "Python Software Foundation"
# print(string.count("o"))

x = 5
y = 10
temp = x
x = y
y = temp
print(x, y)