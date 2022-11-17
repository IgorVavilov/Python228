
# text = " Привет мир! "
# print(text)
# print(text[1])
# print(text[0:6])
# print(text[0:6:2])
# print(text[::-1])
# search = text.find('мир')
# print(search)
# search = text.find('имя')
# print(search)
# text = text.upper()
# print(text)
# text = text.lower()
# print(text)
#
# num = len(text)
# print(num)
#
# a = 'Привет '
# b = 'мир'
# c = 6
# print(a + b + str(c))
#
# print('В лесу родилась елочка! \nВ лесу она была.')
# print('В лесу родилась елочка!', end=' ')
# print('В лесу она была.')
# print("В лесу родилась елочка! \nВ лесу она \"была\".")
# print('стол' * 3)
#
#
# txt = 'привет мир'
# print(txt.title())
# print(txt.capitalize())
# print(txt.swapcase())
#
# print(txt.startswith('привет'))
# print(txt.startswith('мир', 3))
# print(txt.endswith('привет'))
# print(txt.replace('мир', 'небо'))
#
#
# a = 20
# b = 25
# prod = a * b
# print(f'Произведение {a} на {b} равно {prod}')
#
# print(text.rfind('мир'))
#
# print(text.isdigit())
# print(text.isalpha())
# print(text.isalnum())
# print(text.islower())
# print(text.isupper())
# print(text.isspace())
# print(text.istitle())
#
# print(ord('т'))
# print(chr(1090))
#
# print(text.count('мир', 0, 16))
#
# print(text.lstrip())
# print(text.rstrip())
# print(text.strip())
#
# print(text.zfill(12))

# text = 'Привет мир!'
# for i in text:
#     print(i)
#
# for i in text:
#     print(i, end=' ')
# Программа, которую вы напишете, должна начинаться с запроса у пользователя суммы заказа в ресторане.
# После этого должен быть произведен
# расчет налога и  чаевых официанту. Вы можете использовать принятую
# в вашем регионе налоговую ставку для подсчета суммы сборов. В качестве
# чаевых мы оставим 18 % от стоимости заказа без учета налога. На выходе программа должна отобразить отдельно
# налог, сумму чаевых и итог,
# включая обе составляющие. Форматируйте вывод таким образом, чтобы
# все числа отображались с двумя знаками после запятой.

# summa_zakaza = float(input('Введите сумму заказа: '))
# tax = 0.22
# chai = 0.18
#
# tax_sum = summa_zakaza * tax
# chai_sum = summa_zakaza * chai
#
# total = summa_zakaza + tax_sum + chai_sum
#
# print(f'{round(tax_sum, 2)}, {round(chai_sum, 2)}, {round(total, 2)}')

# Дана строка. Замените в этой строке все появления буквы h на букву H,
# кроме первого и последнего вхождения.
# s = 'Hello hello HelloH'
# s = s.replace('h', 'H', s.count('H') - 1)
# print(s)
# s = s.replace('H', 'h', 1)
# print(s)
#
# num = len(s)
# a = s[1:num-1]
# print(a)
# b = a.replace('h', 'H')
# print(b)
# print(s[0], a, s[17], sep='')

# Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.

# text = 'В лесу родилась елочка'
# total = ''
# for i in range(len(text)):
#     if i % 3 != 0:
#         total += text[i]
# print(total)

# На вход программе подается строка текста. Напишите программу,
# которая заменяет все вхождения цифры 1 на слово «one».

# txt = '1 two 1 3 5 1'
# print(txt.replace('1', 'one'))
# print(txt.replace('two', ''))

# Сначала выведите третий символ этой строки.
# Во второй строке выведите предпоследний символ этой строки.
# В третьей строке выведите первые пять символов этой строки.

# text = 'В лесу родилась елочка'
#
# print(text[2])
# print(text[-2])
# print(text[:6])

# В четвертой строке выведите всю строку, кроме последних двух символов.
# text = 'Рододендрон'
# print(text[:-2])
# print()

# В пятой строке выведите все символы с четными индексами (считая, что индексация
# начинается с 0, поэтому символы выводятся начиная с первого).
# txt = ''
# for i in range(len(text)):
#     if i % 2 == 0:
#         txt += text[i]
# print(txt, end='')
# print()
# print()

# В шестой строке выведите все символы с нечетными индексами, то есть начиная
# со второго символа строки.
# txt = ''
# for i in range(len(text)):
#     if i % 2 != 0:
#         txt += text[i]
# print(txt, end='')
# print()
# print()

# В седьмой строке выведите все символы в обратном порядке.
# print(text[::-1])
# print()

# В восьмой строке выведите все символы строки через один в обратном порядке,
# начиная с последнего.
# txt1 = text[::-1]
# # print(txt1)
# txt = ''
# for i in range(len(txt1)):
#     if i % 2 == 0:
#         txt += txt1[i]
# print(txt, end='')
# print()
# print()

# В девятой строке выведите длину данной строки.
# print(len(text))
# print()

# Дана строка, состоящая из слов, разделенных пробелами. Определите,
# сколько в ней слов. Используйте для решения задачи метод count.
# text = 'когда предел обратного квадрата также «равен» бесконечности'
# a = text.count(' ')
# print(a+1)
# print()

# Дана строка, состоящая ровно из двух слов, разделенных пробелом.
# Переставьте эти слова местами. Результат запишите в строку и выведите
# получившуюся строку.
# При решении этой задачи не стоит пользоваться циклами и инструкцией if.
# text = 'решу тебя'
# txt1 = text[:4]
# txt2 = text[5:]
# print(txt2 + ' ' + txt1)

# line = input('Введите слово:')
# is_palindrom = True
# i = 0
#
# while i < len(line) / 2 and is_palindrom:
#     if line[i] != line[len(line) - i - 1]:
#         is_palindrom = False
#     i += 1
#
# if is_palindrom:
#     print(line, "- Это палиндром")
# else:
#     print(line, "Это не палиндром")
#
# if line == line[::-1]:
#     print(line, "- Это палиндром")
# else:
#     print

# message = input("Введите сообщение: ")
# shift = int(input("Введите сдвиг: "))
# new_message = ""
# for ch in message:
#     if ch >= "a" and ch <= "z":
#         pos = ord(ch) - ord('a')
#         pos = (pos + shift)
#         print(pos)
#         nes_char = chr(pos+ord('a'))
#         new_message += nes_char
#     elif ch >= "A" and ch <= "Z":
#         pos = ord(ch) - ord('A')
#         pos = (pos + shift) % 26
#         nes_char = chr(pos+ord('A'))
#         new_message += nes_char
#     else:
#         new_message += nes_char
# print(message)
# print(new_message)

# print("  ", end="   ")
# for i in range(1, 11):
#     print(i, end="   ")
# print()
# for i in range(1, 11):
#     print(i, end='    ')
#     for j in range(1, 11):
#         print(i*j, end="  ")
#     print()

# 18.09.2022

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
# print(numbers)
# print(numbers[2])

# num = [i for i in range(1, 7)] #генератор списка
# print(num)
#
# print(numbers[0:2])
# print(numbers[:3])
# print(numbers[::-1])

# print(len(numbers))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
#
# print(numbers.index(9))
# print(numbers.count(1)) #подсчет одинаковых элементов
#
# numbers.append(4) # добавление элемента
# print(numbers)
# numbers.sort() # сортировка по возрастанию
# print(numbers)
#
# numbers.insert(3, 5) # добавление элемента в заданное место
# print(numbers)
#
# numbers.remove(5) # удаление заданого эелемнта (первого попавшегося)
# print(numbers)
#
# numbers.extend([2, 4, 6, 8]) # добавление элементов
# print(numbers)
#
# numbers.pop(10) # удаление элемента по заданному индексу
# print(numbers)
#
# del numbers[9] # удаление элмента по заданному индексу
# print(numbers)
#
# mylist = ['стол', 'стул']
# print(', '.join(mylist)) #выводит элементы в качестве строчных данных
#
# text = 'стол, стул'
# massiv = text.split(",") #создает массив из строчных элементов
# print(massiv)
#
# #пример создания пустого списка
# # arr = []
# # arr = list()
#
# massiv.clear() #полная очиска массива
# print(massiv)
#
# mylist.reverse() # переворот массива
# print(mylist)

# arr = list()
# num = int(input('Введите число: '))
# while num != 0:
#     arr.append(num)
#     num = int(input('Введите число: '))
# arr.sort()
# print(arr)

# words = []
# word = input("Введите значение (Enter - остановить): ")
#
# while word !='':
#     if word not in words:
#         words.append(word)
#     word = input("Введите значение (Enter - остановить): ")
#
# for word in words:
#     print(word)

# negatives = []
# zeros = []
# positives = []
#
# line = input("Введите значение (Enter - остановить): ")
# while line != '':
#     num = int(line)
#     if num < 0:
#         negatives.append(num)
#     elif num > 0:
#         positives.append(num)
#     else:
#         zeros.append(num)
#     line = input("Введите значение (Enter - остановить): ")
#
# negatives.sort()
# positives.sort()
# zeros.sort()
#
# for n in negatives:
#     print(n, end=' ')
# for n in zeros:
#     print(n, end=' ')
# for n in positives:
#     print(n, end=' ')

# В списке целых, заполненном  числами
# вычислить:
# ■ Сумму отрицательных чисел;
# ■ Сумму четных чисел;
# ■ Сумму нечетных чисел;
# ■ Произведение элементов с индексами кратными 3;
# ■ Произведение элементов между минимальным и
# максимальным элементом;
# ■ Сумму элементов, находящихся между первым и последним положительными элементами.
#
# num = [i for i in range(-5, 9)]
# neg = 0
# a = 0
# b = 0
# c = max(num) * min(num)
# d = 0
# ind = []
# poslist = []
# for n in num:
#     if n < 0:
#         neg += n
#     elif n % 2 == 0:
#         a += n
#     elif n % 2 != 0:
#         b += n
#         ind.append(n)
#     elif n > 0:
#         d += n
#         poslist.append(n)
#
#
#
# print("Сумму отрицательных чисел", neg)
# print('Сумму четных чисел', a)
# print('Сумму нечетных чисел', b)
# print('Произведение элементов между минимальным и максимальным элементом', c)
# print(ind)
# print(poslist)

# Для выигрыша главного приза необходимо, чтобы шесть номеров на лотерейном билете совпали с шестью
# числами, выпавшими случайным образом в диапазоне от 1 до 49 во время очередного тиража.
# Напишите программу, которая будет случайным образом подбирать шесть номеров для
# вашего билета. Убедитесь в том, что среди этих чисел не будет дубликатов.
# Выведите номера билетов на экран по возрастанию.

# import random
#
# print(random.randint(0, 10))
# print(random.randrange(0, 100, 5))
#
# seq = [10, 11, 12, 13, 14, 15]
# random_e = random.choice(seq)
# print(random_e)
#
# import random
# numlist = []
# for i in range(1, 7):
#     numlist.append(random.randrange(1, 50))
# for k in numlist:
#     print(k, end=' ')
# print()
# print(numlist)


# ДЗ за 17.09

# Многие в своих сообщениях не ставят заглавные буквы, особенно если используют для набора мобильные
# устройства. Создайте программу, которая
# будет принимать на вход исходную строку и возвращать строку с восстановленными заглавными буквами. По существу,
# ваша программа должна:
#  сделать заглавной первую букву в строке, не считая пробелы;
#  сделать заглавной первую букву после точки, восклицательного или
# вопросительного знака, не считая пробелы;
#  если текст на английском языке, сделать заглавными буквы «i», которым предшествует пробел или
# за которыми следует пробел, точка,
# восклицательный или вопросительный знак.
# Реализация такого рода автоматической корректуры исключит большую часть ошибок с регистром букв.
# Например, строку «what time do i have to be there? what’s the address? this time i’ll try to be on time!»
# ваша программа
# должна преобразовать в более приемлемый вариант «What time do I have
# to be there? What’s the address? This time I’ll try to be on time!». В основной
# программе запросите у  пользователя исходную строку, обработайте ее
# при помощи своей функции и выведите на экран итоговый результат.

#
# s = input("Введите текст: ")
# result = s
# pos = 0
# while pos < len(s) and result[pos] == ' ':
#     pos = pos + 1
# if pos < len(s):
#     result = result[0: pos] + result[pos].upper() + result[pos + 1: len(result)]
#
# pos = 0
# while pos < len(s):
#     if result[pos] == "." or result[pos] == "!" or result[pos] == "?":
#         pos = pos + 1
#         while pos < len(s) and result[pos] == " ":
#             pos = pos + 1
#         if pos < len(s):
#             result = result[0: pos] + \
#                         result[pos].upper() + \
#                         result[pos + 1: len(result)]
#     pos = pos + 1
#
# pos = 0
# while pos < len(s):
#     if result[pos] == 'i' and result[pos-1] == ' ' and result[pos+1] == ' ':
#         result = result[0: pos] + \
#                  result[pos].upper() + \
#                  result[pos + 1: len(result)]
#     if result[pos] == 'i' and result[pos-1] == ' ' and result[pos+1] == "’":
#         result = result[0: pos] + \
#                  result[pos].upper() + \
#                  result[pos + 1: len(result)]
#     pos = pos + 1
#
# print(result)

# дз за 18.09.2022
# Напишите программу, которая будет запрашивать у пользователя числа, пока он не пропустит ввод.
# Сначала на экран должно быть выведено среднее значение введенного ряда чисел, после
# этого друг за другом необходимо вывести список чисел ниже среднего, равных ему (если такие найдутся)
# и выше среднего. Каждый список должен предваряться соответствующим заголовком.

# num = input('Введите число (пустой ввод - выход): ')
# listNum = []
# while num != '':
#     listNum.append(num)
#     num = input('Введите число (пустой ввод - выход): ')
#
# sumNum = 0
# count = 0
# for i in listNum:
#     sumNum += int(i)
#     count += 1
# averNum = sumNum / count
# print()
# print("Среднее значение введенного ряда равно:", averNum)
#
# lesNum = []
# for k in listNum:
#     if int(k) < averNum:
#         lesNum.append(k)
# print('Список чисел ниже среднего:', ', '.join(str(i) for i in lesNum))
#
# equNum = []
# for k in listNum:
#     if int(k) == averNum:
#         equNum.append(k)
# print('Список чисел равных среднему:', ', '.join(str(i) for i in equNum))
#
# upNum = []
# for k in listNum:
#     if int(k) > averNum:
#         upNum.append(k)
# print('Список чисел выше среднего:', ', '.join(str(i) for i in upNum))
#
# print()
# print('Введенный список чисел:', ', '.join(str(i) for i in listNum))

# Собственным делителем числа называется всякий его делитель, отличный от самого числа. Напишите функцию,
# которая будет возвращать список всех собственных делителей заданного числа. Само это число должно передаваться
# в функцию в виде единственного аргумента. Результатом функции будет перечень собственных делителей числа,
# собранных в список. Основная программа должна демонстрировать работу функции, запрашивая у пользователя число
# и выводя на экран список его собственных делителей. Программа должна запускаться только в том случае, если она
# не импортирована в виде модуля в другой файл.

# num = input('Введите число: ')
# devList = []
# for i in range(1, int(num)):
#     if int(num) % i == 0:
#         devList.append(i)
# print('Список собственных делителей числа:', num, '-', ', '.join(str(i) for i in devList))

# Напишите программу, показывающую, отсортирован ли переданный ей в качестве параметра список (по возрастанию
# или убыванию). Функция должна возвращать True, если список отсортирован, и False в противном случае. В основной
# программе запросите у пользователя последовательность чисел для списка, после чего выведите сообщение о том,
# является ли этот список отсортированным изначально. Можно прогнать через рандом

# import random
# numlist = []
# numlist_sorted = []
# result = True
# for i in range(1, 7):
#     numlist.append(random.randrange(1, 50))
# for i in numlist:
#     numlist_sorted.append(i)
# numlist_sorted.sort()
#
# if numlist == numlist_sorted:
#     print(result)
# else:
#     result = False
#     print(result)
#
# print('Начальный список:', numlist)
# print('Сортированный список:', numlist_sorted)

# 24.09.2022

# В данном упражнении вам предстоит разработать программу, в которой
# у  пользователя будет запрошен список слов, пока он не оставит строку
# ввода пустой. После этого на экране должны быть показаны слова, введенные пользователем,
# но без повторов, – каждое по одному разу. При этом
# слова должны быть отображены в том же порядке, в  каком их вводили
# с клавиатуры. Например, если пользователь на запрос программы введет
# следующий список слов:
# first
# second
# first
# third
# second
# программа должна вывести:
# first
# second
# third
#
# words = []
# word = input("Введите слово (Enter - завершить): ")
# while word != '':
#     if word not in words:
#         words.append(word)
#
#     word = input("Введите слово (Enter - завершить): ")
#
# for word in words:
#     print(word)

# При анализе собранных по результатам научных экспериментов данных
# зачастую возникает необходимость избавиться от экстремальных значений, прежде чем продолжать двигаться дальше.
# Напишите функцию,
# создающую копию списка с исключенными из него n наибольшими и наименьшими значениями и возвращающую ее в качестве
# результата. Порядок следования элементов в измененном списке не обязательно должен
# в точности совпадать с источником.Для начала попросите пользователя ввести целые числа, затем
# соберите их в список. Выведите на экран измененную версию списка
# вместе с оригинальной. Если
# пользователь введет менее четырех чисел, должно быть отображено соответствующее сообщение об ошибке.

# values = []
# retval = ''
# s = input("Введите значение (Enter - завершить): ")
# while s != '':
#     num = float(s)
#     values.append(num)
#     s = input("Введите значение (Enter - завершить): ")
#
# if len(values) < 4:
#     print('Вы ввели недостаточное количество чисел: ')
# else:
#     retval = sorted(values)
#     retval.pop()
#     retval.pop(0)
#     print(retval)
#     print(values)
#
# def namefunction():
#     тело программы
#
# import random
#
# def createDeck():
#     cards = []
#
#     for suit in ["s", "h", "d", "c"]:
#         for value in ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]:
#             cards.append(value + suit)
#
#     return cards
#
# def shuffle(cards):
#     for i in range(0, len(cards)):
#         other_pos = random.randrange(i, len(cards))
#
#         temp = cards[i]
#         cards[i] = cards[other_pos]
#         cards[other_pos] = temp
#
# cards = createDeck()
# print('Исходная колода карт: ')
# print(cards)
# print()
#
# shuffle(cards)
# print('Перетасованная колода карт: ')
# print(cards)
#
# В стандартной библиотеке языка Python присутствует функция count, позволяющая подсчитать,
# сколько раз определенное значение встречается
# в списке. В данном упражнении вы создадите новую функцию countRange,
# которая будет подсчитывать количество элементов в  списке, значения
# которых больше или равны заданному минимальному порогу и  меньше максимального. Функция
# должна принимать три параметра: список,
# минимальную границу и максимальную границу. Возвращать она будет
# целочисленное значение, большее или равное нулю. В основной программе реализуйте демонстрацию вашей
# функции для нескольких списков
# с разными минимальными и максимальными границами. Удостоверьтесь,
# что программа будет корректно работать со списками, содержащими как
# целочисленные значения, так и числа с плавающей запятой.

# def count_range(mas, minimum, maximum) -> int:
# 	counter = 0
# 	for i in mas:
# 		if minimum <= i < maximum:
# 			counter += 1
#
# 	return counter
#
#
# ls = [1, 2, 3, 4, 5, 0.2, 12.23, 2, 1231.123]
# print(count_range(ls, 2, 100))


# ball = (11, 12, 12, 10, 9, 12)
# print(ball)
# ball[0] = 100
# print(ball)

#
# dict = dict()
# dict = {}
#
# d = {"Ужасы":"Пила", "Мультики":"Дом"}
#
# print(d)
# print()
# print(d.values())
# print(d.keys())
# print(d.items())
# d["Ужасы"] = "Оно"
# print(d)
# d.pop("Мультики")
# print(d)
# d["Коммедия"] = "Горько"
# print(d)
# print(d.get("Ужасы"))
#
# del d["Коммедия"]
# print(d)
#
# print(d["Ужасы"])
#
# dictvar = {154:34, 121:56, 98:68}
# sorted_key = sorted(dictvar)
# print(sorted_key)
#
# Написать программу для рекомендации книги по жанру:
# На экран выводится список доступных жанров. Затем пользователь запрашивает нужный жанр.
# Если введённый жанр есть в списке, то вывести название соответствующей книги. Иначе — «Жанр не найден».

# books = { 'детектив': 'Шерлок Холмс', 'приключения': 'Властелин колец', 'фантастика': 'Гарри Поттер',
#           'юмор': 'Трое в лодке'}
# print('Выберете один из', len(books), 'жанров')
# genres = books.keys()
# print(genres)
# genre = input('Введите жанр:').lower()
# if genre in books:
#     print('Рекомендуем:', books[genre])
# else:
#     title = input('Жанр не найден! Напишите любую книгу этого жанра:')
#     books[genre] = title
#     print('Список рекомендаций обновлён')
#     print(books)

# 1.	С клавиатуры вводится фамилия автора. 2. По одному вводятся книги до тех пор,
# пока не будет напечатан символ 's'. Книги сохраняются в список. 3. Автор и список
# книг добавляются в словарь my_shelf. Затем словарь выводится на экран.
# my_shelf = {}
# author = input("Введите автора: ")
#
# while author != "":
# 	if author not in my_shelf:
# 		mas = input("Введите книги через пробел: ").split()
# 		my_shelf[author] = mas
# 	author = input("Введите автора: ")
#
# print(my_shelf)

# Напишите программу, определяющую и выводящую на экран количество
# уникальных символов во введенной пользователем строке. Например,
# в строке Hello, World! содержится десять уникальных символов, а в строке
# zzz – один. Используйте словарь или набор для решения этой задачи.
#
# s = input("Введите строку: ")
# characters = {}
# for ch in s:
#     characters[ch] = True
#
# print(len(characters))

# points = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4,  "G": 2, "H": 4, "I": 1, "J": 2, "K": 5, "L": 1,
#  "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1,
#  "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8,
#  "Y": 4, "Z": 10}
#
# word = input("Введите слово: ")
# uppercase = word.upper()
# score = 0
# for ch in uppercase:
#     score += points[ch]
#
# print

# 25.09.2022

# def tovar_summa(tovar):
#     count = 0
#     for i in range(tovar):
#         if i == 0:
#             count += 10.95
#         else:
#             count += 2.95
#     return count
# tovar = int(input("введите кол-во товара: "))
#
# print(tovar_summa(tovar))

# x = float(input("Ener first number: "))
# y = float(input("Ener second number: "))
# z = float(input("Ener third number: "))
#
# def median(a, b, c):
#     if a < b and b < c or a > b and b > c:
#         return b
#     if b < a and a < c or b > a and a > c:
#         return a
#     if c < a and b < c or c > a and b > c:
#         return c
#
# def altmedian(a, b, c):
#     return a + b + c - min(a, b, c) - max(a, b, c)
#
# print(median(x, y, z))
# print(altmedian(x, y, z))

# def checkPass(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if ch >= "A" and ch <= "Z":
#             has_upper = True
#         elif ch >= "a" and ch <= "z":
#             has_lower = True
#         elif ch >= "0" and ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
# p = input("Enter password: ")
#
# if checkPass(p):
#     print("This good pass")
# else:
#     print("NOt good pass")

# def characterCounts(s):
#     counts = {}
#     for ch in s:
#         if ch in counts:
#             counts[ch] = counts[ch] + 1
#         else:
#             counts[ch] = 1
#     return counts
#
# a = input("Enter 1 word: ")
# b = input("Enter 2 word: ")
#
# counts1 = characterCounts(a)
# counts2 = characterCounts(b)
#
# if counts1 == counts2:
#     print("Yes")
#     print(counts1)
#     print(counts2)
# else:
#     print("no")
#     print(counts1)
#     print(counts2)


# from random import randrange
# num_runs = 1000
# d_max = 6
#
#
# def twodice():
#
#     d1 = randrange(1, d_max + 1)
#     d2 = randrange(1, d_max + 1)
#
#     return d1 + d2
#
#
# expected = {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36}
# counts = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
#
# for i in range(num_runs):
#     t = twodice()
#     counts[t] = counts[t] + 1
#
# print("Всего   реальных   ожиданий")
# print("         процент    процент")
#
# for i in sorted(counts.keys()):
#     print("%5d %9.2f %10.2f" % (i, counts[i]/num_runs*100, expected[i]*100))

# Задание 1
# Создайте программу, хранящую информацию о великих баскетболистах. Нужно хранить ФИО баскетболиста и
# его рост. Требуется реализовать возможность добавления,
# удаления, поиска, замены данных. Используйте словарь
# для хранения информации.

# basket = {"Кельвин Мерфи": "175", "Слэйтер Мартин": "178", "Эвери Джонсон": "178"}
# print(basket)
# zapros = input("Сделайте выбор (0 - Добавить, 1 - Удалить, 2 - Найти, 3 - Изменить, для выхода нажмите Enter): ")
#
# while zapros != '':
#     if zapros == "0":
#         gamer = input("Введите ФИО игрока: ")
#         if gamer not in basket:
#             rost = input("Введите рост игрока в сантиметрах: ")
#             basket[gamer] = rost
#         zapros = input("Сделайте выбор (0 - Добавить, 1 - Удалить, 2 - Найти,
#         3 - Изменить, для выхода нажмите Enter): ")
#     elif zapros == "1":
#         gamer = input("Введите ФИО игрока: ")
#         del basket[gamer]
#
#         zapros = input("Сделайте выбор (0 - Добавить, 1 - Удалить, 2 - Найти,
#         3 - Изменить, для выхода нажмите Enter): ")
#     elif zapros == "2":
#         gamer = input("Введите ФИО игрока: ")
#         print("Рост игрока", basket[gamer])
#
#         zapros = input("Сделайте выбор (0 - Добавить, 1 - Удалить, 2 - Найти,
#         3 - Изменить, для выхода нажмите Enter): ")
#     elif zapros == "3":
#         gamer = input("Введите ФИО игрока: ")
#         rost = input("Введите нужный рост: ")
#         basket[gamer] = rost
#         zapros = input("Сделайте выбор (0 - Добавить, 1 - Удалить, 2 - Найти,
#         3 - Изменить, для выхода нажмите Enter): ")
#
# print(basket.items())

# alpha = {
#     'A': '2', 'B': '22', 'C': '222', 'D': '3', 'E': '33', 'F': '333', 'G': '4', 'H': '44',
#     'I': '444', 'J': '5', 'K': '55',
#     'L': '555', 'M': '6', 'N': '66', 'O': '666', 'P':'7', 'Q':'77', 'R':'777', 'S':'7777',
#     'T':'8', 'U':'88', 'V':'888', 'W':'9', 'X':'99', 'Y':'999', 'Z':'9999', ' ':'0', '.': '1',
#     ',': '11', '?': '111', '!': '1111', ':': '11111'
# }
#
# word = input("Введите слово: ")
# uppercase = word.upper()
# score = ''
# for ch in uppercase:
#     score += alpha[ch]
#
# print(score)

# дз 24.09.2022
#   Карточка для игры в лото состоит из пяти колонок, в каждой из которых - пять номеров. Колонки помечены
# буквами B, I, N, G и O. Под каждой буквой могут быть номера в своем диапазоне из 15 чисел. А именно под буквой 'B'
# могут присутствовать числа от 1 до 15, под 'I' - от 16 до 30, под 'N' - от 31 до 45 и т.д.
#   Напишите функцию, которая будет создавать случайную карточку лото и сохранять ее в словаре. Ключами словаря будут
# буквы B, I, N, G, и O, а значениями - списки из пяти чисел, располагающихся в колонке под каждой буквой. Создайте
# еще одну функцию для отображения созданной карточки лото на экране со столбцами с заголовками. В основной
# программе создайте карту лото слчайным образом и выведедите ее на экран.

# from random import randrange
# num_runs = 5
# # d_max = 6
# B = []
# I = []
# N = []
# G = []
# O = []
# counts = {}
# def createcard():
#
#     for i in range(num_runs):
#         B.append(randrange(1, 16))
#         I.append(randrange(16, 31))
#         N.append(randrange(31, 46))
#         G.append(randrange(46, 61))
#         O.append(randrange(61, 76))
#
#     counts = {'B': [], 'I': [], 'N': [], 'G': [], 'O': []}
#     counts['B'] = B
#     counts['I'] = I
#     counts['N'] = N
#     counts['G'] = G
#     counts['O'] = O
#
#     return counts
#
# def showcard():
#     t = createcard()
#     for key in t:
#         print(key, end='    ')
#     print()
#     count = 0
#     while count < len(t.values()):
#         for i in t.values():
#             print(i[count], end='   ')
#         print()
#         count +=1
#
# showcard()
#

# дз 25.09.22

# Первый, третий и пятый символы в канадском почтовом индексе представляют собой буквы,
# а второй, четвертый и шестой - цифры. Провинцию или территорию, которой принадлежит индекс,
# можно определить по первому символу индекса, как показано в табл. 6.4. Символы
# D, Q, U, W, и Z в настоящее время не используются в почтовых индексах Канады.
#     Второй символ в почтовом индексе определяет, расположен ли интересующий нас адрес
# в городе или в сельской местности. Если на этом месте стоит ноль, значит, это сельская
# местность, иначе город.
#     Напишите программу, которая будет запрашивать почтовый индекс у пользователя и
# обображать провинцию или территорию, которой он принадлежит, с указанием того, городская
# это территория или сельская. Например, если пользователь введет индекс T2N1N4, программа
# должна определить, что речь идет о городе на территории провинции Альберта. А индекс X0A1B2
# соответствует сельской местности в провинции Нувавут или в Северо-Западных территориях.
# Используйте словарь для хранения информации о соответствии первого символа индекса
# конкретной провинции или территории. Выведите на экран соостветствующее сообщение об
# ошибке, если индекс начинается с символа, который не используется для этих целей, или
# второй символ не является цифрой.
#
# indexLetter = {'A': 'Ньюфаундленд', 'B': 'Новая Шотландия', 'C': 'Остров Принца Эдуарда',
#                'E': 'Нью-Брансуик', 'G': 'Квебек', 'H': 'Квебек', 'J': 'Квебек',
#                'К': 'Онтарио', 'L': 'Онтарио', 'M': 'Онтарио', 'N': 'Онтарио', 'P': 'Онтарио',
#                'R': 'Манитоба', 'S': 'Саскачеван', 'T': 'Альберта', 'V': 'Британская Колумбия',
#                'X': 'Нанавут либо Северо-Западные территории', 'Y': 'Юкон'}
#
# indexnum = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#
# index = input('Введите индекс для инициализации: ')
# indexupper = index.upper()
#
# for j in indexnum:
#     if j == indexupper[1]:
#         print('ys')
#         for i in indexLetter.keys():
#             if i == indexupper[0] and int(indexupper[1]) == 0:
#                 print('Это сельская местность на территории провинции - ', indexLetter[i])
#                 break
#             elif i == indexupper[0] and int(indexupper[1]) > 0:
#                 print('Это город на территории провинции - ', indexLetter[i])
#                 break
#         else:
#             print('Индекс начинаестя с несуществующего символа.')
#         break
# else:
#     print('Второй символ не является цифрой', indexupper[1])
#
# Создайте программу «Книжная коллекция». Нужно хранить информацию о книгах: автор, название книги, жанр, год выпуска,
# количество страниц, издательство. Требуется реализовать возможность добавления, удаления, поиска, замены данных.
# Используйте словарь для хранения информации.

# print("         *** Книжная коллекция ***")
# booksLib = {}
# print()
# request = input('Сделайте выбор, того что Вам необходимо сделать (0 - Добавить, 1 - Удалить, 2 - Найти, 3 - Изменить, для выхода нажмите Enter):')
# while request != '':
#     if request == "0":
#         autor = input("Введите автора: ")
#         if autor not in booksLib:
#             data = input("Введите название книги, жанр, год выпуска, количество страниц и издательство через пробел: ").split()
#             booksLib[autor] = data
#             print('Добавление успешно')
#         request = input('Сделайте выбор, того что Вам необходимо сделать (0 - Добавить, 1 - Удалить, 2 - Найти, 3 - Изменить, для выхода нажмите Enter):')
#     elif request == "1":
#         autor = input("Введите автора: ")
#         del basket[autor]
#         print('Удаление успешно')
#         request = input('Сделайте выбор, того что Вам необходимо сделать (0 - Добавить, 1 - Удалить, 2 - Найти, 3 - Изменить, для выхода нажмите Enter):')
#
#     elif request == "2":
#         autor = input("Введите автора: ")
#         print("Данные книги", booksLib[autor])
#
#         request = input('Сделайте выбор, того что Вам необходимо сделать (0 - Добавить, 1 - Удалить, 2 - Найти, 3 - Изменить, для выхода нажмите Enter):')
#     elif request == "3":
#         autor = input("Введите автора: ")
#         data = input("Введите название книги, жанр, год выпуска, количество страниц и издательство через пробел: ").split()
#         booksLib[autor] = data
#         print('Изменение успешно')
#         request = input('Сделайте выбор, того что Вам необходимо сделать (0 - Добавить, 1 - Удалить, 2 - Найти, 3 - Изменить, для выхода нажмите Enter):')
#
# print(booksLib)

# 01.10.2022

# Множества

# first_set = set(("Connor", 32, (1,2,3)))
# print(first_set)
# cond_set = set("Connor")
# print(cond_set)
#
# m_set = set((1,2,3,4,5))
# print(m_set.discard(5))
# print(m_set.discard(6))
#
# print(m_set.pop())
# print(m_set)
#
# add_set = set((1,2,3,4))
# print(add_set)
#
# add_set.update((1,))
# print(add_set)
# add_set.update((5,))
# print(add_set)
# add_set.update(('cello', 'violin'))
# print(add_set)
#
# add_set.remove('violin')
# print(add_set)
#
# first_set = {1, 2, 3}
# scnd_set = {3, 4, 5}
# print(first_set.union(scnd_set)) # объединяет множества исключая пересекающиеся элементы
#
# print(first_set.intersection(scnd_set)) #при пересечении множеств, выбирает пересекающиеся значения
#
# print(scnd_set.difference(first_set)) # выбирает уникальные значения массива при сравнении двух, при чем выбирает значения из первого массива
#
# print(first_set.symmetric_difference(scnd_set)) # выбирает уникальные значения из обоих массивов.

# Задание 2
# Существует два множества, содержащие названия
# городов. Необходимо создать третье множество, содержащее названия,
# которые есть в обоих множествах.

# gorod_one = {'Липецк', 'Москва', 'Воронеж'}
# gorod_two = {'Липецк', 'Ростов', 'Воронеж', 'Курск'}
# print(gorod_one.union(gorod_two))

# Задание 3
# Существует два множества, содержащие названия
# городов. Необходимо создать третье множество, содержащее названия,
# которые есть в первом множестве, но
# нет во втором.

# print(gorod_one.difference(gorod_two))

# Задание 4
# Существует два множества, содержащие названия
# городов. Необходимо создать третье множество, содержащее названия,
# которые есть во втором множестве, но
# нет в первом.

# print(gorod_two.difference(gorod_one))

# Задание 5
# Существует два множества, содержащие названия
# городов. Необходимо создать третье множество, содержащее уникальные
# названия для каждого множества.

# print(gorod_one.symmetric_difference(gorod_two))

# import random
#
# print("Вывод случайного числа при помощи random: ")
# print(random.random())
#
# print("Вывод случайного числа при помощи random: ")
# print(random.randint(0, 9))
#
# print("Вывод случайного числа при помощи random: ")
# print(random.randrange(0, 10, 2))
# import random
#
# city_list = ['Воронеж', 'Москва', 'Питер']
# print('Выбор случайного города из списка: ', random.choice(city_list)) # Выбор значения из списка
#
# random.shuffle(city_list) #перемешивание списка в случайном порядке
# print(city_list)
#
# seq = [10, 11, 12, 11, 14, 11]
# random_seq = random.sample(seq, 4) # выборака 4-х элементов из списка в случайном порядке.
# print(random_seq)
#
# number_list = [3, 6, 9, 12, 15, 18, 21, 27, 30]
#
# print('Первоя выборка - ', random.sample(number_list, 5))
# state = random.getstate() # устанавливает состояние предыдущей выборки
#
# print('Вторая выборка - ', random.sample(number_list, 5))
# random.setstate(state)  # сохраняет (кэширует) состояние предыдущей выборки
#
# print('Третья выборка - ', random.sample(number_list, 5))
# random.setstate(state)
#
# print('Четвертая выборка -

# Игра в кости с использованием модуля random в Python
# Далее представлен код простой игры в кости, которая поможет понять
# принцип работы функций модуля random. В игре два участника и два кубика.
# Участники по очереди бросают кубики, предварительно встряхнув их;
# Алгоритм высчитывает сумму значений кубиков каждого участника и добавляет
# полученный результат на доску с результатами;
# Участник, у которого в результате большее количество очков, выигрывает.

# import random
#
# AnnaScore = 0
# AlexScore = 0
#
# diceOne = [1, 2, 3, 4, 5, 6]
# diceTwo = [1, 2, 3, 4, 5, 6]
#
# def playDiceGame():
#     for i in range(5):
#         random.shuffle(diceOne)
#         random.shuffle(diceTwo)
#     firstNumber = random.choice(diceOne)
#     secondNumber = random.choice(diceTwo)
#     return firstNumber + secondNumber
#
# print('Игра в кости использует модуль рандом')
#
# for i in range(3):
#     AlexTossNumber = random.randint(1, 100)
#     AnnaTossNumber = random.randint(1, 100)
#
#     if AlexTossNumber > AnnaTossNumber:
#         print('Алекс выиграл жеребьевку')
#         AlexScore = playDiceGame()
#         AnnaScore = playDiceGame()
#     else:
#         print('Анна выиграла жеребьевку')
#         AlexScore = playDiceGame()
#         AnnaScore = playDiceGame()
#
#     if AlexScore > AnnaScore:
#         print('Алекс выиграл игру в кости')
#     else:
#         print('Анна выиграла игру в кости')

# В данном упражнении мы будем симулировать 1000 выбрасываний
# игральных костей. Начнем с написания функции, выполняющей случайное
# выбрасывание двух обычных шестигранных костей. Эта функция не
# будет принимать входных параметров, а возвращать должна число, выпавшее в сумме на двух костях.
# В основной программе реализуйте симуляцию тысячи выбрасываний
# костей. Программа должна хранить все результаты с частотой их выпадения.
# После завершения процесса должна быть показана итоговая таблица
# с  результатами, похожая на ту, что представлена в табл. 6.1. Выразите
# частоту выпадения каждого из чисел в процентах вместе с ожидаемым
# результатом согласно теории вероятностей.

# from random import randint
#
# NUM_RUNS = 1000
# D_MAX = 6
#
# def twoDice():
#     d1 = randint(1, D_MAX)
#     d2 = randint(1, D_MAX)
#     return d1 + d2
#
# expected = {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36}
#  # Составим словарь для хранения результатов выбрасывания костей
# counts = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
#
# for i in range(1000):
#     t = twoDice()
#     counts[t] += counts[t]
#
# print('Всего        Реальный        Ожидаемый')
# print('             процент         процент')
# for i in sorted(counts.keys()):
#     print('%5d  %9.2f   %10.2f' % (i, counts[i]/NUM_RUNS * 100, expected[i]*100))

# Для выигрыша главного приза необходимо, чтобы шесть номеров на лотерейном билете
# совпали с шестью числами, выпавшими случайным образом в диапазоне от 1 до 49 во
# время очередного тиража. Напишите программу, которая будет случайным образом
# подбирать шесть номеров для вашего билета. Убедитесь в том, что среди этих чисел не будет дубликатов.
# Выведите номера билетов на экран по возрастанию.

# import random
# list = []
# listUser = input("Введите шесть цифр от 1 до 49 через пробел: ").split()
#
# for i in range(6):
#     num = random.randrange(1, 49)
#     list.append(num)
#
# listSor = sorted(list)
# listUserSor = sorted(listUser)
#
# if listSor == listUserSor:
#     print('Ваш билет выиграл')
# else:
#
#     print('Ваш билет', listUser, 'не выиграл')

# 02.10.2022

# def bubble_sort(nums):
#     # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(nums) - 1):
#             if nums[i] > nums[i + 1]:
#                 # Меняем элементы
#                 nums[i], nums[i + 1] = nums[i + 1], nums[i]
#                 # Устанавливаем swapped в True для следующей итерации
#                 swapped = True
#
# # Проверяем, что оно работает
# random_list_of_nums = [5, 2, 1, 8, 4]
# bubble_sort(random_list_of_nums)
# print(random_list_of_nums)



# def selection_sort(nums):
#     # Значение i соответствует кол-ву отсортированных значений
#     for i in range(len(nums)):
#         # Исходно считаем наименьшим первый элемент
#         lowest_value_index = i
#         # Этот цикл перебирает несортированные элементы
#         for j in range(i + 1, len(nums)):
#             if nums[j] < nums[lowest_value_index]:
#                 lowest_value_index = j
#         # Самый маленький элемент меняем с первым в списке
#         nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
#
# # Проверяем, что оно работает
# random_list_of_nums = [12, 8, 3, 20, 11]
# selection_sort(random_list_of_nums)
# print(random_list_of_nums)


# def insertion_sort(nums):
#     # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
#     for i in range(1, len(nums)):
#         item_to_insert = nums[i]
#         # Сохраняем ссылку на индекс предыдущего элемента
#         j = i - 1
#         # Элементы отсортированного сегмента перемещаем вперёд, если они больше
#         # элемента для вставки
#         while j >= 0 and nums[j] > item_to_insert:
#             nums[j + 1] = nums[j]
#             j -= 1
#         # Вставляем элемент
#         nums[j + 1] = item_to_insert
#
# # Проверяем, что оно работает
# random_list_of_nums = [9, 1, 15, 28, 6]
# insertion_sort(random_list_of_nums)
# print(random_list_of_nums)




#
# def heapify(nums, heap_size, root_index):
#     # Индекс наибольшего элемента считаем корневым индексом
#     largest = root_index
#     left_child = (2 * root_index) + 1
#     right_child = (2 * root_index) + 2
#
#     # Если левый потомок корня — допустимый индекс, а элемент больше,
#     # чем текущий наибольший, обновляем наибольший элемент
#     if left_child < heap_size and nums[left_child] > nums[largest]:
#         largest = left_child
#
#     # То же самое для правого потомка корня
#     if right_child < heap_size and nums[right_child] > nums[largest]:
#         largest = right_child
#
#     # Если наибольший элемент больше не корневой, они меняются местами
#     if largest != root_index:
#         nums[root_index], nums[largest] = nums[largest], nums[root_index]
#         # Heapify the new root element to ensure it's the largest
#         heapify(nums, heap_size, largest)
#
# def heap_sort(nums):
#     n = len(nums)
#
#     # Создаём Max Heap из списка
#     # Второй аргумент означает остановку алгоритма перед элементом -1, т.е.
#     # перед первым элементом списка
#     # 3-й аргумент означает повторный проход по списку в обратном направлении,
#     # уменьшая счётчик i на 1
#     for i in range(n, -1, -1):
#         heapify(nums, n, i)
#
#     # Перемещаем корень Max Heap в конец списка
#     for i in range(n - 1, 0, -1):
#         nums[i], nums[0] = nums[0], nums[i]
#         heapify(nums, i, 0)
#
# # Проверяем, что оно работает
# random_list_of_nums = [35, 12, 43, 8, 51]
# heap_sort(random_list_of_nums)
# print(random_list_of_nums)

#
#
#
# def merge(left_list, right_list):
#     sorted_list = []
#     left_list_index = right_list_index = 0
#
#     # Длина списков часто используется, поэтому создадим переменные для удобства
#     left_list_length, right_list_length = len(left_list), len(right_list)
#
#     for _ in range(left_list_length + right_list_length):
#         if left_list_index < left_list_length and right_list_index < right_list_length:
#             # Сравниваем первые элементы в начале каждого списка
#             # Если первый элемент левого подсписка меньше, добавляем его
#             # в отсортированный массив
#             if left_list[left_list_index] <= right_list[right_list_index]:
#                 sorted_list.append(left_list[left_list_index])
#                 left_list_index += 1
#             # Если первый элемент правого подсписка меньше, добавляем его
#             # в отсортированный массив
#             else:
#                 sorted_list.append(right_list[right_list_index])
#                 right_list_index += 1
#
#         # Если достигнут конец левого списка, элементы правого списка
#         # добавляем в конец результирующего списка
#         elif left_list_index == left_list_length:
#             sorted_list.append(right_list[right_list_index])
#             right_list_index += 1
#         # Если достигнут конец правого списка, элементы левого списка
#         # добавляем в отсортированный массив
#         elif right_list_index == right_list_length:
#             sorted_list.append(left_list[left_list_index])
#             left_list_index += 1
#
#     return sorted_list
#
# def merge_sort(nums):
#     # Возвращаем список, если он состоит из одного элемента
#     if len(nums) <= 1:
#         return nums
#
#     # Для того чтобы найти середину списка, используем деление без остатка
#     # Индексы должны быть integer
#     mid = len(nums) // 2
#
#     # Сортируем и объединяем подсписки
#     left_list = merge_sort(nums[:mid])
#     right_list = merge_sort(nums[mid:])
#
#     # Объединяем отсортированные списки в результирующий
#     return merge(left_list, right_list)
#
# # Проверяем, что оно работает
# random_list_of_nums = [120, 45, 68, 250, 176]
# random_list_of_nums = merge_sort(random_list_of_nums)
# print(random_list_of_nums)



#
# def partition(nums, low, high):
#     # Выбираем средний элемент в качестве опорного
#     # Также возможен выбор первого, последнего
#     # или произвольного элементов в качестве опорного
#     pivot = nums[(low + high) // 2]
#     i = low - 1
#     j = high + 1
#     while True:
#         i += 1
#         while nums[i] < pivot:
#             i += 1
#
#         j -= 1
#         while nums[j] > pivot:
#             j -= 1
#
#         if i >= j:
#             return j
#
#         # Если элемент с индексом i (слева от опорного) больше, чем
#         # элемент с индексом j (справа от опорного), меняем их местами
#         nums[i], nums[j] = nums[j], nums[i]
#
# def quick_sort(nums):
#     # Создадим вспомогательную функцию, которая вызывается рекурсивно
#     def _quick_sort(items, low, high):
#         if low < high:
#             # This is the index after the pivot, where our lists are split
#             split_index = partition(items, low, high)
#             _quick_sort(items, low, split_index)
#             _quick_sort(items, split_index + 1, high)
#
#     _quick_sort(nums, 0, len(nums) - 1)
#
# # Проверяем, что оно работает
# random_list_of_nums = [22, 5, 1, 18, 99]
# quick_sort(random_list_of_nums)
# print(random_list_of_nums)

# Напишите программу на Python для сортировки списка элементов с использованием алгоритма
# пузырьковой сортировки.
# Примечание. Согласно Википедии «Пузырьковая сортировка, иногда называемая сортировкой по
# убыванию, представляет собой простой алгоритм сортировки, который последовательно проходит
# по списку для сортировки, сравнивает каждую пару смежных элементов и меняет их местами, если
# они находятся в неправильном порядке. Пропуск через список повторяется до тех пор, пока не
# понадобятся перестановки, что указывает на сортировку списка. Алгоритм, который является
# сортировкой сравнения, назван так, чтобы меньшие элементы «пузырились» в верхней части
# списка. Хотя алгоритм прост , он слишком медленный и непрактичный для большинства задач, даже
# по сравнению с сортировкой вставкой. Это может быть практичным, если входные данные обычно
# находятся в порядке сортировки, но иногда могут иметь некоторые неупорядоченные элементы,
# находящиеся почти на месте ».
# Пример данных : [14,46,43,27,57,41,45,21,70]
# Ожидаемый результат : [14, 21, 27, 41, 43, 45, 46, 57, 70]

# def bubbleSort(nlist):
#     for passnum in range(len(nlist) - 1, 0, -1):
#         for i in range(passnum):
#             if nlist[i] > nlist[i + 1]:
#                 temp = nlist[i]
#                 nlist[i] = nlist[i + 1]
#                 nlist[i + 1] = temp
#
# nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
# bubbleSort(nlist)
# print(nlist)

# Метод выборки

# def selectionSort(nlist):
#     for fillslot in range(len(nlist) - 1, 0, -1):
#         maxpos = 0
#         for location in range(1, fillslot + 1):
#             if nlist[location] > nlist[maxpos]:
#                 maxpos = location
#
#         temp = nlist[fillslot]
#         nlist[fillslot] = nlist[maxpos]
#         nlist[maxpos] = temp
#
# nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
# selectionSort(nlist)
# print(nlist)

# Метод вставки

# def insertionSort(nlist):
#     for index in range(1, len(nlist)):
#         currentvalue = nlist[index]
#         position = index
#         while position > 0 and nlist[position - 1] > currentvalue:
#             nlist[position] = nlist[position - 1]
#             position = position - 1
#         nlist[position] = currentvalue
#
# nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
# insertionSort(nlist)
# print(nlist)

# Метод сортировки Слиянием

# def mergeSort(nlist):
#     print('Расщипление: ', nlist)
#     if len(nlist) > 1:
#         mid = len(nlist)//2
#         lefthalf = nlist[:mid]
#         righthalf = nlist[mid:]
#         mergeSort(lefthalf)
#         mergeSort(righthalf)
#
#         i=j=k=0
#
#         while i < len(lefthalf) and j < len(righthalf):
#             if lefthalf[i] < righthalf[j]:
#                 nlist[k] = lefthalf[i]
#                 i += 1
#             else:
#                 nlist[k] = righthalf[j]
#                 j += 1
#
#             k = k + 1
#
#         while i < len(lefthalf):
#             nlist[k] = righthalf[i]
#             i += 1
#             k += 1
#
#         while j < len(righthalf):
#             nlist[k] = righthalf[j]
#             j += 1
#             k += 1
#     print('слияние', nlist)
#
# nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
# mergeSort(nlist)
# print(nlist)

# mass = ['banana', 'apple', 'bananamango', 'mango', 'strawberry-banana']
# fruct = input('Введите название фрукта: ')
# while fruct != '':
#     mass.append(fruct)
#     fruct = input('Введите название фрукта: ')

# fruct_user = input('Введите название искомого фрукта: ')
#
# count = 0
# for i in mass:
#     if i == fruct_user:
#         count += 1
# print(count)

# Задание 2
# Добавьте к заданию 1 подсчет количества раз, когда
# название фрукта является частью элемента. Например:
# banana, apple, bananamango, mango, strawberry-banana.
# В примере выше banana встречается три раза.

# count_1 = 0
# index = 0
# for submass in mass:
#     if submass.find(fruct_user) >= 0:
#         count_1 += 1
# print(count_1)

# дз 01.10.22

# import random
#
# dictGame = {1: "Камень", 2: "Ножницы", 3: "Бумага"}
#
# def Game():
#     for i in range(3):
#         num = random.randint(1, 3)
#         return num
#
# hod = int(input("Введите 1 - начать игру, 2 - выйти из игры: "))
#
# gamerName_1 = input("Введите свое Имя: ")
# gamerName_2 = input("Введите свое Имя: ")
#
# while hod != 2:
#     gamer_1 = input(f'{gamerName_1}, Сделайте ход - нажмите клавишу "Y": ')
#     gamer_2 = input(f'{gamerName_2}, Сделайте ход - нажмите клавишу "Y": ')
#     agr1 = gamer_1.upper()
#     agr2 = gamer_2.upper()
#
#     if agr1 == 'Y' and agr2 == 'Y':
#         gamer1_hod = Game()
#         gamer2_hod = Game()
#
#         if dictGame[gamer1_hod] == dictGame[gamer2_hod]:
#             print(f'У {gamerName_1} - {dictGame[gamer1_hod]}, а у {gamerName_2} - {dictGame[gamer2_hod]}. Ничья.')
#         elif gamer1_hod == 1 and gamer2_hod == 2:
#             print(f'У {gamerName_1} - {dictGame[gamer1_hod]}, а у {gamerName_2} - {dictGame[gamer2_hod]}. {gamerName_1} Выиграл')
#         elif gamer1_hod == 2 and gamer2_hod == 3:
#             print(f'У {gamerName_1} - {dictGame[gamer1_hod]}, а у {gamerName_2} - {dictGame[gamer2_hod]}. {gamerName_1} Выиграл')
#         elif gamer1_hod == 1 and gamer2_hod == 3:
#             print(f'У {gamerName_1} - {dictGame[gamer1_hod]}, а у {gamerName_2} - {dictGame[gamer2_hod]}. {gamerName_2} Выиграл')
#         elif gamer1_hod == 2 and gamer2_hod == 1:
#             print(f'У {gamerName_1} - {dictGame[gamer1_hod]}, а у {gamerName_2} - {dictGame[gamer2_hod]}. {gamerName_2} Выиграл')
#         elif gamer1_hod == 3 and gamer2_hod == 2:
#             print(f'У {gamerName_1} - {dictGame[gamer1_hod]}, а у {gamerName_2} - {dictGame[gamer2_hod]}. {gamerName_2} Выиграл')
#         elif gamer1_hod == 3 and gamer2_hod == 1:
#             print(f'У {gamerName_1} - {dictGame[gamer1_hod]}, а у {gamerName_2} - {dictGame[gamer2_hod]}. {gamerName_1} Выиграл')
#
#     hod = int(input("Введите 1 - продолжить игру, 2 - выйти из игры: "))


# 09,10,2022

# import os
#
# print("Текущая директория: ", os.getcwd())

# os.mkdir("C:\\test") - создание директории

# os.chdir() - изменение названия текущей директории

# os.makedirs('C:\\test\\test2') - создание нескольких папок

# text_file = open('C:\\test\\text.txt', 'w+') - создание файла
# text_file.write("Это текстовый файл") - запись информации в файл
# text_file.close() - закрытие файла

# os.rename('C:\\test\\text.txt', 'C:\\test\\renamed-text.txt') - изменение названия файла

# os.replace() - перемещение файла
#
# os.remove('C:\\test\\renamed-text.txt') - удаление файла

# os.rmdir('C:\\test') - удаление директории (только если она пустая)

# os.removedirs() - Удаление папок рекурсивно

# print(os.stat('C:\\test\\renamed-text.txt')) - отображает информацию о файле

# with open('C:\\test\\renamed-text.txt') as file:
#     # txt = file.read()
#     # print(txt)
#
#     num = int(input('enter quontity of lines: '))
#
#     for i in range(num):
#         txt = file.readlines(num)
#         print(txt)

# with open('C:\\test\\text.txt', 'w+', encoding='unf-8') as file:
#     text = 'Добавляем некоторый текст в файл'
#     file.write(text)
#
# txt = open('C:\\test\\text.txt', 'r', encoding='utf-8')
# print(txt.read())
# txt.close()

# import os

# with open('C:\\test\\renamed-text.txt', 'r') as file:
#
#     n = 0
#     arr = []
#     for i in file:
#         i = i.rstrip()
#         arr.append(i)
#         n += 1
#     print(arr)
#     num = int(input('Введите кол-во строк: '))
#     minimum = len(arr) - num
#     txt = arr[minimum:len(arr)]
#     for j in txt:
#         print(j)

# with open('C:\\test\\renamed-text.txt', 'r') as file:
#
#     words = file.read()
#
#     simbol = '!?,.-:—;'
#
#     for i in simbol:
#         words = words.replace(i, '')
#
#     text = words.split()
#     print(text)
#     maxs = 0
#     for word in text:
#         num = len(word)
#         if maxs < num:
#             maxs = num
#
#     print(maxs)

# 9. Напишите программу на Python для подсчета количества строк в текстовом файле.

# with open('C:\\test\\renamed-text.txt', 'r') as file:
#     n = 0
#     for i in file:
#         n += 1
#     print(n)

# 10. Напишите программу на Python для подсчета частоты слов в файле.
# with open('C:\\test\\renamed-text.txt', 'r') as file:
#     words_1 = file.read().rstrip()
#     symbol = '.,;:?!-"\''
#     for i in symbol:
#         words_1 = words_1.replace(i, '')
#     print(words_1)
#
#     dt = {}
#
#     count = 0
#     words_1 = words_1.split()
#     dt = dt.fromkeys(words_1, count)
#     for i in words_1:
#         if i in dt.keys():
#             dt[i] = dt[i] + 1
#     print(dt)

# 12. Напишите программу на Python для записи списка в файл.

# arr = ['яблоко', 'банан', 'апельсин', 'груша', 'виноград']
# with open(r'C:\\test\\fructs.txt', 'w+') as file:
#     for i in arr:
#         file.write('%s\n' % i)
#
#
# txt = open(r'C:\\test\\fructs.txt', 'r')
# print(txt.read())
# txt.close()

# import csv
# import datetime
# import time
#
# with open(r'C:\\test\\rows_300.csv', 'w+') as file:
#     writer = csv.writer(file)
#     writer.writerow(['№', 'Секунда', 'Микросекунда'])
#     for line in range(1, 301):
#         writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
#         time.sleep(0.01)


# дз 02.10.22

# Задание 1
# Есть массив с целыми числами. Нужно вывести статистику по количеству цифр в элементах кортежа. Например:
# ■ Одна цифра — 3 элемента;
# ■ Две цифры — 4 элемента;
# ■ Три цифры — 5 элементов.

# numList = (3, 50, 2, 8, 400, 222, 32, 8, 4, 45, 568, 91, 7)
# count1 = 0
# count10 = 0
# count100 = 0
# for i in numList:
#     if 0 <= int(i) < 10:
#         count1 += 1
#     elif 10 <= int(i) < 100:
#         count10 += 1
#     elif 100 <= int(i) < 1000:
#         count100 += 1
#
# print(f'Одна цифра - {count1} элемента(ов)')
# print(f'Две цифры - {count10} элемента(ов)')
# print(f'Три цифры - {count100} элемента(ов)')

# Задание 2
# Есть массив с названиями производителей автомобилей (название производителя может встречаться от 0
# до N раз). Пользователь вводит с клавиатуры название
# производителя и слово для замены. Необходимо заменить
# в кортеже все элементы с этим названием на слово для
# замены. Совпадение по названию должно быть полным.

# carList = ['bmw', 'mercedes benz', 'lada', 'suzuki', 'hyunday', 'kia', 'suzuki', 'lada', 'jaguar', 'lada', 'bmw']
# print(carList)
# print()
# origCar = input("Введите название авто из списка выше, которое нужно заменить: ")
# newCar = input("Введите название авто, на которое нужно заменить: ")
# indexCar = 0
# for car in carList:
#     if carList[indexCar] == origCar:
#         carList[indexCar] = newCar
#
#     indexCar += 1
# print()
# print('Измененный результат:')
# print(carList)

# дз 08.10.22
#
# Задание 2
# Дан текстовый файл. Необходимо создать новый файл
# и записать в него следующую статистику по исходному
# файлу:
# ■ Количество символов;
# ■ Количество строк;
# ■ Количество гласных букв;
# ■ Количество согласных букв;
# ■ Количество цифр.

# with open('C:\\test\\text.txt', 'r', encoding='utf-8') as txt, open('C:\\test\\new_text.txt', 'w+', encoding='utf-8') as new_txt:
#     sym = len(txt.read().rstrip())
#     new_txt.write(f'Количество символов: {sym}')
#
# with open('C:\\test\\text.txt', 'r', encoding='utf-8') as txt, open('C:\\test\\new_text.txt', 'a', encoding='utf-8') as new_txt:
#     s = 0
#     for i in txt:
#         s += 1
#     new_txt.write(f'\nКоличество строк: {s}')
#
# with open('C:\\test\\text.txt', 'r', encoding='utf-8') as txt, open('C:\\test\\new_text.txt', 'a', encoding='utf-8') as new_txt:
#     sogl = 'цкнгшщзхъждлрпвфчсмтьб'
#     glas = 'йуеыаоэяию'
#     num = '0123456789'
#     sym = txt.read()
#     count_glas = 0
#     count_sogl = 0
#     count_num = 0
#     for i in sym:
#         if i in glas:
#             count_glas += 1
#         elif i in sogl:
#             count_sogl += 1
#         elif i in num:
#             count_num += 1
#
#     new_txt.write(f'\nКоличество гласных букв: {count_glas}')
#     new_txt.write(f'\nКоличество согласных букв: {count_glas}')
#     new_txt.write(f'\nКоличество цифр: {count_glas}')

# Задание 3
# Дан текстовый файл. Удалить из него последнюю
# строку. Результат записать в другой файл.

# with open('C:\\test\\text.txt', 'r', encoding='utf-8') as txt, open('C:\\test\\new_text.txt', 'w+', encoding='utf-8') as new_txt:
#     s = txt.readlines()
#     s.pop(len(s)-1)
#     for i in s:
#         new_txt.write(i)

# дз 09.10.22

# 14. Напишите программу на Python для объединения каждой строки из первого файла с соответствующей строкой во втором файле.

# with open('C:\\test\\file_1.txt', 'r', encoding='utf-8') as txt, open('C:\\test\\file_2.txt', 'r', encoding='utf-8') as new_txt, open('C:\\test\\file_3.txt', 'w+', encoding='utf-8') as split_txt:
#     file_1 = txt.read().split()
#     file_2 = new_txt.read().split()
#     file_split = []
#     for i in range(len(file_1)):
#         file_split.append(file_1[i] + file_2[i])
#     for i in file_split:
#         split_txt.write(i + '\n')

# 15. Напишите программу на Python для чтения случайной строки из файла.

# from random import randrange
# txt = open('C:\\test\\text.txt', 'r', encoding='utf-8')
# n = 0
# for i in txt:
#     n += 1
# txt.close()
#
# txt1 = open('C:\\test\\text.txt', 'r', encoding='utf-8')
# list_txt1 = txt1.read().split()
# rand_s = list_txt1[randrange(n)]
# print(rand_s)
# txt1.close()

# 18. Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим,
# что задано положительное целое число).

# file_name = input("введите путь к текстовому файлу: ")
# lines = input('Введите кол-во строк для вывода: ')
# def read_last(lines, file):
#     if int(lines) > 0:
#         file = open(file_name, 'r', encoding='utf-8')
#         file1 = file.read().splitlines()
#         print(file1)
#         for l in range(len(file1)-1, (len(file1) - int(lines))-1, -1):
#             print(file1[l])
#     else:
#         print('Вы ввели отрицательное число в параметрах кол-ва строк, либо другие символы. Попробуйте еще раз.')
#
# read_last(lines, file_name)

# Задача 1
# Дан список некоторых целых чисел, найдите значение 20
# в нем и, если оно присутствует, замените его на 200. Обновите список только
# при первом вхождении числа 20.

# with open('C:\\test\\text.txt', 'r', encoding='utf-8') as txt, open('C:\\test\\file_2.txt', 'w+', encoding='utf-8') as new_txt:
#
#     num_list = txt.read().split()
#     for i in range(len(num_list)):
#         if num_list[i] == '20':
#             num_list[i] = '200'
#             break
#     for i in num_list:
#         new_txt.write(i + '\n')


# Задача 2
# Необходимо удалить пустые строки из списка строк.

# with open('C:\\test\\text.txt', 'r', encoding='utf-8') as txt, open('C:\\test\\file_2.txt', 'w+', encoding='utf-8') as new_txt:
#
#     str_list = txt.read().splitlines()
#
#     for line in str_list:
#         if line == '':
#             str_list.remove(line)
#     for line in str_list:
#         new_txt.write(line + '\n')



# Задача 3
# Дан список чисел. Превратите его в список квадратов этих чисел.

# with open('C:\\test\\text.txt', 'r', encoding='utf-8') as txt, open('C:\\test\\file_2.txt', 'w+', encoding='utf-8') as new_txt:
#
#     num_list = txt.read().split()
#
#     new_list = []
#     for i in range(len(num_list)):
#         num_list[i] = int(num_list[i]) ** 2
#         num_list[i] = str(num_list[i])
#         new_list.append(num_list[i])
#     for i in new_list:
#         new_txt.write(i + '\n')

# Задача 4
# Дан список чисел, необходимо удалить все вхождения числа 20 из него.
#
# with open('C:\\test\\text.txt', 'r', encoding='utf-8') as txt, open('C:\\test\\file_2.txt', 'w+', encoding='utf-8') as new_txt:
#
#     num_list = txt.read().split()
#     for i in num_list:
#         if i == '20':
#             num_list.remove(i)
#     print(num_list)
#     for i in num_list:
#         new_txt.write(i + '\n')


# Заполнить список ста нулями, кроме первого и последнего элементов, которые должны быть равны единице;

# zero_list = []
#
# for i in range(1, 101):
#     n = 0
#     zero_list.append(n)
# zero_list[0] = 1
# zero_list[-1] = 1
# print(zero_list)


# Дан массив, например, M = [3,8,2,4] . Как узнать равна ли сумма каких-нибудь двух его элементов числу 12?

# m_list = [2, 4, 2, 9, 8, 4, 2, 1, 8, 5, 4, 3]
# for i in m_list:
#     for j in m_list:
#         if i + j == 12:
#             print(f"Да сумма {i} и {j} будет равна 12")


# Дан одномерный массив числовых значений, насчитывающий N элементов. Определить образуют ли
# элементы массива, расположенные перед первым отрицательным элементом, убывающую последовательность.

# num_list = [5, 0, 3, 2, 0, -2, 5, 4, 7]
# i = 0
# flag = True
# new_list = []
# while num_list[i] >= 0:
#     new_list.append(num_list[i])
#     i += 1
#
# for i in range(len(new_list)-1):
#     if new_list[i] > new_list[i+1]:
#         flag = True
#     else:
#         flag = False
#         break
#
# print(new_list)
#
# if flag == True:
#     print("yes")
# else:
#     print("NO")



# Построить матрицу заданной размерности m*n и вывести ее на экран. Элементы матрицы формируются
# случайно и имеют значение от 1 до 10 включительно.
# Построить матрицу целых чисел размерностью m×n, где m — количество строк матрицы, n — количество столбцов
# матрицы. Значения m и n вводятся с клавиатуры. Числа в матрице формируются случайным образом и находятся в
# пределах от 1 до 10. Используя генератор списков вычислить количество элементов матрицы, которые более 5.
#
# import random
#
# m = int(input("Введите кол-во строк матрицы от 1 до 10: "))
# n = int(input("Введите кол-во столбцов матрицы от 1 до 10: "))
# count_list = 0
#
# for i in range(n):
#     for j in range(1, m+1):
#         print(random.randint(1, 10), end='  ')
#
#     print()
# print()
# print(count_list)

# 22.10.2022
# def b(value):
#     print('-> b')
#     print(value + 1)
#
# def a(value):
#     print('-> a')
#     b(value)
# try:
#     a('10')
# except:
#     print

# try:
#     a = 7/0
# except:
#     print('Ошибка! Деление на 0')
#
# try:
#     a = 7/0
# except ZeroDivisionError:
#     print('Ошибка! Деление на 0')

# try:
#     a = 7/'0'
# except Exception:
#     print('Любая ошибка!')

# try:
#     b = int(input())
#     a = b + b
#     print(a)
# except ValueError:
#     print('Неверный тип введенных данных')

# try:
#     file = open('C:\\test\\tet.txt')
# except FileNotFoundError as e:
#     print(e)

# import datetime
# now = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
# try:
#     file = open('C:\\test\\tet.txt', "r")
# except FileNotFoundError  as e:
#     print(f'{now} [FileNotFoundError]: ', e)

# file = open('C:\\test\\text.txt', "r")
#
# try:
#     lines = file.readlines()
#     print(lines[8])
# except IndexError:
#     print('Недостаточно строк для вывода')
# finally:
#     file.close()
#     if file.closed:
#         print('Файл закрыт!')

# def sum(a, b):
#     res = 0
#     try:
#         res = a + b
#     except TypeError:
#         res = int(a) + int(b)
#     finally:
#         print(f'a = {a}, b = {b}, res = {res}')
# sum(1, '2')


# try:
#     b = int(input('b = '))
#     c = int(input('c = '))
#     a = b/c
# except ZeroDivisionError:
#     print("Ошибка! Деление на 0")
# except ValueError:
#     print('Ошибка! Введено не корректное число')
# else:
#     print(f'a = {a}')

# try:
#     b = int(input('b = '))
#     c = int(input('c = '))
#     a = b/c
# except (ZeroDivisionError, ValueError) as e:
#     print(e)
# else:
#     print(f'a = {a}')

# min = 100
# if min > 10:
#     raise Exception('минимальное число 10')

# min = 100
# try:
#     if min > 10:
#         raise Exception('Минимальное число 10')
# except Exception:
#     print('Моя ошибка')
#     raise

# try:
#     a = 7/0
# except:
#     pass

# 1. Напишите программу ввода нутальных чисел через запятую и преобразования этой строки в список чисел.
# Реализовать обработку возможных значений.

# try:
#     num = input('Введите числа через пробел: ').split()
#     int_num = list(map(int, num))
#     print(int_num)
# except ValueError:
#     print('Неправильный тип данных')

# 2. Написать функцию вычисления среднего арифметического элементов переданного ей списка. Исключения

# def sr_arif(nums):
#     sr = sum(nums)/len(nums)
#     print("среднеее арифметического = ", sr)
# try:
#     nums = list(map(int, input('Введите числа через пробел: ').split()))
#     if len(nums) == 0:
#         raise ZeroDivisionError
#     sr_arif(nums)
# except ValueError:
#     print("введеные значения должны быть числами")
# except ZeroDivisionError:
#     print("Список должен иметь минимум один элемент")

# 3. Написать функцию для удаления произвольного элемента из множества с помощью .pop()
# Функция должна возвращать значение удаленного элемента. Исключения.
#
# def funcpop(num):
#     a = num.pop()
#     return print(a)
#
# try:
#      num = set(2, '2', 5, 3, 6, '5', 2)
#     funcpop(num)
#     print(num)
# except KeyError:
#     print('Множество не может быть пустым')

# Напишите программу, которая запрашивает ввод двух значений.
# Если хотя бы одно из них не является числом, то должна выполняться конкатенация,
# то есть соединение, строк. В остальных случаях введенные числа суммируются.

# a = input("Введите значение: ")
# b = input("Введите значение: ")
# try:
#     print(int(a) + int(b))
# except ValueError:
#     print(a + b)

# 23.10.2022

# Как вы знаете, в языке Python для создания комментариев в коде исполь-
# зуется символ #. Комментарий начинается с этого символа и продолжает-
# ся до конца строки – без возможности остановить его раньше.
# В данном упражнении вам предстоит написать программу, которая
# будет удалять все комментарии из исходного файла с кодом на языке
# Python. Пройдите по всем строкам в файле на предмет поиска символа
# #. Обнаружив его, программа должна удалить все содержимое, начиная
# с этого символа и до конца строки. Для простоты не будем рассматривать
# ситуации, когда знак решетки встречается в середине строки. Сохраните
# новое содержимое в созданном файле. Имена файла источника и фай-
# ла назначения должны быть запрошены у пользователя. Удостоверьтесь
# в том, что программа корректно обрабатывает возможные ошибки при
# работе с обоими файлами.

# Открытие файла
# try:
#     in_name = input('Введите название файла: ')
#     inf = open('C:\\test\\' + in_name + '.txt', 'r', encoding='utf-8')
# except:
#     print('При открытии файла произошла ошибка.')
#     print('Завершение работы программы')
#
# # имя итогового файла
# try:
#     out_name = input('Введите название нового файла: ')
#     outf = open(r'C:\\test\\' + out_name + '.txt', 'w+', encoding='utf-8')
# except Exception as e:
#     print('При открытии файла произошла ошибка:', e)
#     print('Завершение работы программы.')
#
# # сама программа
# try:
#     for line  in inf:
#         pos = line.find("#")
#         if pos > -1:
#             line = line[0:pos]
#             line = line + '\n'
#         outf.write(line)
#     inf.close()
#     outf.close()
# except Exception as es:
#     print('При открытии файла произошла ошибка:', es)
#     print('Завершение работы программы.')

# Перед публикацией текста или документа обычно принято удалять или
# изменять в них служебную информацию.
# В данном упражнении вам необходимо написать программу, которая
# будет заменять все служебные слова в тексте на символы звездочек (по
# количеству символов в словах). Вы должны осуществлять регистрозави-
# симый поиск служебных слов в тексте, даже если эти слова входят в состав
# других слов. Список служебных слов должен храниться в отдельном файле.
# Сохраните отредактированную версию исходного файла в новом файле.
# Имена исходного файла, файла со служебными словами и нового файла
# должны быть введены пользователем.
# В качестве дополнительного задания расширьте свою программу таким
# образом, чтобы она выполняла замену служебных слов вне зависимости от
# того, какой регистр символов используется в тексте. Например, если в списке
# служебных слов будет присутствовать слово exam, то все следующие
# варианты слов должны быть заменены звездочками: exam, Exam, ExaM и EXAM.

# try:
#     in_name = input('Введите название файла для редактирования: ')
#     inf = open('C:\\test\\' + in_name + '.txt', 'r', encoding='utf-8')
# except Exception as es:
#     print('При открытии файла произошла ошибка:', es)
#     print('Завершение работы программы.')
#
# try:
#     sen_name = input('Введите название файла со списком служебных слов: ')
#     senf = open(r'C:\\test\\' + sen_name + '.txt', 'r', encoding='utf-8')
#
#     words = []
#     line = senf.readline()
#     while line != '':
#         line = line.strip()
#         words.append(line)
#         line = senf.readline()
# except Exception as e:
#     print('При открытии файла произошла ошибка:', e)
#     print('Завершение работы программы.')
# finally:
#     senf.close()
#
# try:
#     out_name = input('Введите название нового файла: ')
#     outf = open(r'C:\\test\\' + out_name + '.txt', 'w+', encoding='utf-8')
# except Exception as ew:
#     print('При открытии файла произошла ошибка:', ew)
#     print('Завершение работы программы.')
#
# try:
#     line = inf.readline().lower()
#     while line != '':
#         for word in words:
#             line = line.replace(word, '*' * len(word))
#         outf.write(line)
#         line = inf.readline().lower()
# except Exception as er:
#     print('произошла ошибка:', er)
#     print('Завершение работы программы.')
# finally:
#     inf.close()
#     outf.close()

# Задание 1
# Дан текстовый файл. Необходимо создать новый файл
# убрав из него все неприемлемые слова. Список неприемлемых слов находится в другом файле.

# try:
#     in_name = input('Введите название файла для редактирования: ')
#     inf = open('C:\\test\\' + in_name + '.txt', 'r', encoding='utf-8')
# except Exception as es:
#     print('При открытии файла произошла ошибка:', es)
#     print('Завершение работы программы.')
#
# try:
#     wordf_name = input('Введите название файла со списком служебных слов: ')
#     wordf = open(r'C:\\test\\' + wordf_name + '.txt', 'r', encoding='utf-8')
#
#     words = []
#     line = wordf.readline()
#     while line != '':
#         line = line.strip()
#         words.append(line)
#         line = wordf.readline()
# except Exception as e:
#     print('При открытии файла произошла ошибка:', e)
#     print('Завершение работы программы.')
# finally:
#     wordf.close()
#
# try:
#     out_name = input('Введите название нового файла: ')
#     outf = open(r'C:\\test\\' + out_name + '.txt', 'w+', encoding='utf-8')
# except Exception as ew:
#     print('При открытии файла произошла ошибка:', ew)
#     print('Завершение работы программы.')
#
# try:
#     line = inf.readline().lower()
#     while line != '':
#         for word in words:
#             line = line.replace(word, '')
#         outf.write(line)
#         line = inf.readline().lower()
# except Exception as er:
#     print('произошла ошибка:', er)
#     print('Завершение работы программы.')
# finally:
#     inf.close()
#     outf.close()


# Задание 2
# Написать программу транслитерации с русского на
# английский и наоборот. Данные для транслитерации
# берутся из файла и записываются в другой файл. Направление перевода определяется через меню пользователя.

# try:
#     in_name = input('Введите название файла для транлитерации: ')
#     inf = open('C:\\test\\' + in_name + '.txt', 'r', encoding='utf-8')
# except Exception as es:
#     print('При открытии файла произошла ошибка:', es)
#     print('Завершение работы программы.')
#
# try:
#     out_name = input('Введите название нового файла: ')
#     outf = open(r'C:\\test\\' + out_name + '.txt', 'w+', encoding='utf-8')
# except Exception as ew:
#     print('При открытии файла произошла ошибка:', ew)
#     print('Завершение работы программы.')
#
# try:
#     eng_input = input("Введите с какого языка нужно сделать транслитерацию (eng - с английского, rus - с кирилицы): ")
#     line = inf.readline().lower()
#     words = {"а": "a", "б": "b", "в": "w", "г": "g", "д": "d", "е": "e", "ё": "yo", "ж": "j", "з": "z", "и": "i",
#              "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r", "с": "c", "т": "t", "у": "u",
#              "ф": "f", "х": "h", "ц": "c", "ч": "ch", "ш": "sh", "щ": "sh", "э": "e", "ю": "yu", "я": "ya", "ъ": "'"}
#     if eng_input == "rus":
#         while line != '':
#             for key in words:#
#                 line = line.replace(key, words[key])
#             outf.write(line)
#             line = inf.readline().lower()
#     elif eng_input == "eng":
#         while line != '':
#             for key in words:
#                 line = line.replace(words[key], key)
#             outf.write(line)
#             line = inf.readline().lower()
#
# except Exception as er:
#     print('произошла ошибка:', er)
#     print('Завершение работы программы.')
# finally:
#     inf.close()
#     outf.close()


# Задача 3
# Пользователь с клавиатуры вводит названия файлов,
# до тех пор, пока он не введет слово quit. После завершения ввода программа должна записать в итоговый файл
# символы, которые есть во всех перечисленных файлах
# (символы должны быть в каждом файле).

# last_name = ''
# content_list = []

# try:
#     file_name = input('Введите название текстового файла (либо "quit" для завершения): ')
#
#
#     while file_name != 'quit':
#         content = open('C:\\test\\' + file_name + '.txt', 'r', encoding='utf-8')
#         last_name = file_name
#         for i in content:
#             content_list.append(i)
#         content.close()
#         file_name = input('Введите название текстового файла (либо "quit" для завершения): ')
# except Exception as e:
#     print('При открытии файла произошла ошибка', e)
#
# try:
#     new_content = open('C:\\test\\' + last_name + '.txt', 'r+', encoding='utf-8')
#     for item in content_list:
#         new_content.write(item)
# except Exception as e:
#     print('При открытии файла произошла ошибка', e)
# finally:
#     new_content.close()
#     print('Весь контент из указанных файлов, записан в последний.')



# дз 03.10.22

# Задача 1
# Напишите программу, которая принимает имя файла и выводит его расширение. Если расширение у файла
# определить невозможно, выбросите исключение.

# file_name = input('Введите название файла, который нужно проверить: ')
# try:
#     ind = file_name.index('.')
#     print(file_name[ind:])
# except:
#     print('Расширение файла определить невозможно.')

# Задача 2
# Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237.

# ls = [2, 5, 6, 33, 44, 237, 854, 567]
# try:
#     for i in ls:
#         if i % 2 == 0:
#             print(i)
#         elif i == 237:
#             break
# except Exception as e:
#     print(e)


# дз 22.10.22
# Упражнение 157. Буквенные и числовые оценки
# Напишите программу, выполняющую перевод из буквенных оценок в чис-
# ловые и обратно. Программа должна позволять пользователю вводить
# несколько значений для перевода – по одному в каждой строке. Для на-
# чала предпримите попытку сконвертировать введенное пользователем
# значение из числового в буквенное. Если возникнет исключение, попро-
# буйте выполнить обратное преобразование – из буквенного в числовое.
# Если и эта попытка окончится неудачей, выведите предупреждение о том,
# что введенное значение не является допустимым. Пусть ваша програм-
# ма конвертирует оценки до тех пор, пока пользователь не оставит ввод
# пустым. При решении данного задания вам могут помочь наработки из
# упражнений 52 и 53.

# score = input('Введите оценку буквами либо цифрами для конвертации (от одного до пяти): ')
#
# while score != '':
#     num_list1 = {'1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять'}
#     num_list2 = {'один': '1', 'два': '2', 'три': '3', 'четыре': '4', 'пять': '5'}
#     try:
#         print(num_list1[score])
#         score = input('Введите оценку буквами либо цифрами для конвертации (от одного до пяти): ')
#     except KeyError:
#         if score in num_list2:
#             print(num_list2[score])
#             score = input('Введите оценку буквами либо цифрами для конвертации (от одного до пяти): ')
#         elif score not in num_list2:
#             print("Введено недопустимое значение")
#             score = input('Введите оценку буквами либо цифрами для конвертации (от одного до пяти): ')

# 29.10.22

# ООП

# import math
# class Okr():
#     def __init__(self, x, y, r):
#         self.x = x
#         self.y = y
#         self.r = r
#     def get_s(self):
#         return math.pi**2 * self.r
# okrug = Okr(2, 4, 6)
# print(okrug.get_s())

# class Ghost():
#     def __init__(self, color, nicname):
#         self.color = color
#         self.nicname = nicname
#
#     def print_info(self):
#         print ('Цвет персонажа: ', self.color)
#         print ('Ник: ', self.nicname)
#
# character = Ghost('Оранжевый', 'Clyde')
# character.print_info()
#
# character1 = Ghost('Розовый', 'Nic')
# character1.print_info()

# Создай класс Animal:
# 1. Опиши конструктор класса. Он должен создавать экземпляр с двумя свойствами: вид (например, «собака»)
# и голос (например, «Гав!»).
# 2. Добавь в класс метод make_voice(), который выводит на экран голос животного.
# 3. Создай экземпляр класса с параметрами, заданными пользователем и выведи сообщение о создании объекта.
# После создания объекта запроси у пользователя разрешения дать животному команду «Голос». Если разрешение получено,
# программа должна вывести на экран голос животного. В противном случае на экран не выводится никаких сообщений.

# class Animal():
#     def __init__(self, species, voice):
#         self.species = species
#         self.voice = voice
#
#     def make_voice(self):
#         print(self.voice)
#
# animal = input('Какое животное будем программировать? ')
# voice = input('Как животное отвечает на команду Голос? ')
#
# my_animal = Animal(animal, voice)
#
# print('Объект', my_animal.species, 'создан')
#
# answer = input('Подать команду? да/нет')
# if answer == 'да':
#     my_animal.make_voice()

# class People():
#     def __init__(self, name, birthdate, phone, country, city, address):
#         self.name = name
#         self.birthdate = birthdate
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def change_info(self):
#         self.name = input('Имя: ')
#         self.birthdate = input('Дата рождения: ')
#         self.phone = input('Номер телефона: ')
#         self.country = input('Страна: ')
#         self.city = input('Город: ')
#         self.address = input('Адрес: ')
#
#     def print_info(self):
#         print(f'Имя: {self.name}')
#         print(f'Дата рождения: {self.birthdate}')
#         print(f'Номер телефона: {self.phone}')
#         print(f'Страна: {self.country}')
#         print(f'Город: {self.city}')
#         print(f'Адрес: {self.address}')
#
# person = People('', '', '', '', '', '')
# person.change_info()
# person.print_info()

# class Student:
#     def __init__(self, full_name = '', group_number = 0, progress = []):
#         self.full_name = full_name
#         self.group_number = group_number
#         self.progress = progress
#
#     def print_info(self):
#         txt = 'Студент: ' + self.full_name + 'Группа: ' + self.group_number
#         txt += ' Оценки: '
#         for x in self.progress:
#             txt += ' ' + str(x)
#         print(txt)
#
# def SortParam(st):
#     return st.full_name
#
# st_size = int(input('Введите кол-во студентов: '))
# students = []
# for i in range(st_size):
#     print('Введите полное имя студента: ')
#     full_name = input()
#     print('Введите номер группы: ')
#     group_number = input()
#     n = int(input('Сколько оценок у студента? '))
#     print(f'Введите {n} оценок в столбик: ')
#     progress = []
#     for i in range(n):
#         score = int(input())
#         progress.append(score)
#     st = Student(full_name, group_number, progress)
#     st.print_info()
#     students.append(st)
#
# print('Лист студента')
# for st in students:
#     st.print_info()
#
# students = sorted(students, key=SortParam)
#
# print('Отсортированный список: ')
# for st in students:
#     st.print_info()
#
# print('Неуспевающие студенты: ')
# n = 0
# for st in students:
#     for val in st.progress:
#         if val < 3:
#             st.print_info()
#             n += 1
#             break
# if n ==0:
#     print('нет студентов с плохой оценкой')

# class Data():
#     def __init__(self, info):
#         self.info = info
#
#     def __getitem__(self, item):
#         return self.info[item]
#
# class Teacher():
#     def __init__(self):
#         self.work = 0
#
#     def teach(self, info, pupil):
#         for i in pupil:
#             i.take(info)
#             self.work += 1
#
# class Pupil():
#     def __init__(self):
#         self.knowledge = []
#
#     def take(self, info):
#         self.knowledge.append(info)
#
# lesson = Data(['цыклы', 'массивы', 'строки', 'ООП', 'JS'])
# marIvanna = Teacher()
# vasy = Pupil()
# pety = Pupil()
# marIvanna.teach(lesson[2], [vasy, pety])
# marIvanna.teach(lesson[1], [pety])
#
# print(vasy.knowledge)
# print(pety.knowledge)

# import time
# import random
#
# class Card():
#     NumList = ['Джокер', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
#     MastList = ['пик', 'крестей', 'бубей', 'черви']
#
#     def __init__(self, i, j):
#         self.Num = self.NumList[i-1]
#         self.Mastb = self.MastList[j - 1]
#
# class DeckOfCards():
#     def __init__(self):
#         self.deck = [None] * 56
#         k = 0
#         for j in range(1, 5):
#             for i in range(1, 15):
#                 self.deck[k] = Card(i, j)
#                 k += 1
#     def shuffle(self):
#         random.shuffle(self.deck)
#
#     def get(self, i):
#         if 0 <= i <= 55:
#             answer = self.deck[i].Num
#             answer += ' '
#             answer += self.deck[i].Mastb
#         else:
#             answer = 'В колоде только 56 карт'
#         return answer
#
# deck = DeckOfCards()
# deck.shuffle()
# print('Выбирете карту из колоды 56 карт: ')
# n = int(input())
# if n <= 56:
#     card = deck.get(n-1)
#     print('Вы взяли карту: ', card, end='.\n')
# else:
#     print('В колоде только 56 карт')

# lista = input()
# count = 0
# new_s = ''
#
# l = lista.find('h')
# r = lista.rfind('h')

# print(lista[:l] + lista[r+1:])

# for s in lista:
#     if s == 'h':
#         count += 1
# if count == 1:
#     print(lista.find('f'))
# elif count > 1:
#     print(lista.find('f'))
#     print(lista.rfind('f'))
# else:
#     print('NO')

# 30.10.22

# from random import randint
# from time import sleep
#
# class Hero():
#     def __init__(self, name, health, armor, power, weapon):
#         self.name = name
#         self.health = health
#         self.armor = armor
#         self.power = power
#         self.weapon = weapon
#
#     def print_info(self):
#         print('Поприветствуйте героя ->', self.name)
#         print('Уровень здоровья ->', self.health)
#         print('Класс брони ->', self.armor)
#         print('Сила удара: ->', self.power)
#         print('Оружие ->', self.weapon)
#
#     def strike(self, enemy):
#             print('-> УДАР!')
#             print(self.name, 'атакует', enemy.name, 'используя', self.weapon, '\n')
#             enemy.armor -= self.power
#             if enemy.armor < 0:
#                 enemy.health += enemy.armor
#                 enemy.armor = 0
#
#         print(enemy.name, 'покачнулся(-ась)')
#         print('Класс брони упал до', enemy.armor)
#         print('Уровень здоровья снизился до ', enemy.health, '\n')
#
# knight = Hero('Ричард', 50, 25, 20, 'меч')
# rascal = Hero('Хелен', 100, 10, 15, 'лук')
#
# knight.print_info()
# rascal.print_info()
#
# print('Да начнется битва!')
#
# play = True
#
# while play:
#     if randint(0, 1) == 1:
#         fighters = [knight, rascal]
#     else:
#         fighters = [rascal, knight]
#
#     fighters[0].strike(fighters[1])
#     if fighters[1].health <= 0:
#         play = False
#         print(fighters[1].name, 'пал в суровом бою.')
#     sleep(1)

# class Soda:
#     def __init__(self, ingredient = None):
#         if isinstance(ingredient, str):
#             self.ingredient = ingredient
#         else:
#             self.ingredient = None
#
#     def show_my_drink(self):
#         if self.ingredient:
#             print(f'Газировка и {self.ingredient}')
#         else:
#             print('Обычная газировка')
#
# drink1 = Soda()
# drink2 = Soda('Малина')
# drink3 = Soda(5)
#
# drink1.show_my_drink()
# drink2.show_my_drink()
# drink3.show_my_drink()

# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if isinstance(self.a, str) or isinstance(self.b, str) or isinstance(self.c, str):
#             print('Нужно вводить только числа!')
#         elif self.a < 0 or self.c < 0 or self.b < 0:
#             print('С отрицательными числами ничего не выйдет!')
#         elif self.a + self.b > self.c or self.a + self.c > self.b or self.c + self.b > self.a:
#             print('Треугольник существует')
#         else:
#             print('Жаль, но из этого треугольник не сделать.')
#
# tre1 = TriangleChecker(1, 2, 3)
# tre2 = TriangleChecker(-1, 2, 3)
# tre3 = TriangleChecker(2, "2", 4)
#
# tre1.is_triangle()
# tre2.is_triangle()
# tre3.is_triangle()

# Задача 3. Напишите программу с классом Math. Создайте два атрибута — a и b. Напишите методы addition — сложение,
# multiplication — умножение, division — деление, subtraction — вычитание. При передаче в методы параметров a и b
# с ними нужно производить соответствующие действия и печатать ответ.

# class Math():
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def addition(self):
#         print('При сложении чисел, получился ответ: ', self.a + self.b)
#
#     def multiplication(self):
#         print('При умножении чисел, получился ответ: ', self.a * self.b)
#
#     def devision(self):
#         print('При делении чисел, получился ответ: ', self.a / self.b)
#
#     def subtractio(self):
#         print('При вычитании чисел, получился ответ: ', self.a - self.b)
#
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
#
# Math(a, b).addition()
# Math(a, b).multiplication()
# Math(a, b).devision()
# Math(a, b).subtractio()


# Задача 4. Напишите программу с классом Car. Создайте конструктор класса Car. Создайте атрибуты класса Car — color
# (цвет), type (тип), year (год). Напишите пять методов. Первый — запуск автомобиля, при его вызове выводится
# сообщение «Автомобиль заведен». Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
# Третий — присвоение автомобилю года выпуска. Четвертый метод — присвоение автомобилю типа.
# Пятый — присвоение автомобилю цвета.

# class Car():
#     def __init__(self, color, type, year):
#         self.color = color
#         self.type = type
#         self.year = year
#
#     def powerOn(self):
#         print('Автомобиль заведен.')
#
#     def powerOff(self):
#         print('Автомобиль заглушен.')
#
#     def askyear(self):
#         print('Укажите год автомобиля: ')
#         self.year = input()
#
#     def asktype(self):
#         print('Укажите тип автомобиля: ')
#         self.type = input()
#
#     def askcolor(self):
#         print('Укажите цвет автомобиля: ')
#         self.color = input()
#
#     def print_info(self):
#         print(f'Ваш автомобиль {self.type}, {self.year} года, цвет - {self.color}')
#
# car = Car('', '', '')
# car.powerOn()
# car.powerOff()
# car.askyear()
# car.asktype()
# car.askcolor()
# car.print_info()

# 1.	Создать класс, описывающий человека. Должны быть поля для имени, фамилии и возраста.
# Создать экземпляр и вывести информацию о человеке.

# 2.	Добавить метод greet, вызов которого будет выводить в консоль информацию о человеке в
# формате "Привет! Меня зовут Петров Василий, мне 12 лет".

# 3.	Добавить поле grades, в котором будет храниться список оценок.
# Создать список учеников, заполняя оценки каждого случайными числами.

# from random import randint
#
# class Pupil():
#     def __init__(self, name, surname, old, grades = []):
#         self.name = name
#         self.surname = surname
#         self.old = old
#         self.grades = grades
#
#     def ask_name(self):
#         print('Укажите Ваше имя: ')
#         self.name = input()
#
#     def ask_surname(self):
#         print('Укажите Вашу фамилию: ')
#         self.surname = input()
#
#     def ask_old(self):
#         print('Укажите Ваш возраст: ')
#         self.old = input()
#
#     def print_info(self):
#         print(f'Вы указали Имя: {self.name}, Фамилию: {self.surname} и возраст: {self.old}')
#
#     def greet(self):
#         print(f'Привет! Меня зовут {self.surname} {self.name}, мне {self.old} лет.')
#
#
#     def grades_list(self):
#         print('Укажите кол-во оценок: ')
#         n = int(input())
#         grades = []
#         for i in range(n):
#             score = randint(1, 5)
#             grades.append(score)
#         st = Pupil(self.name, self.surname, self.grades)
#         students = []
#         students.append(st)
#         for st in students:
#             print(grades)
#
#
# person = Pupil('', '', '')
#
# person.ask_name()
# person.ask_surname()
# person.ask_old()
# person.print_info()
# person.greet()
# person.grades_list()

# 06.11.22
#Методы

# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'Точка 2D ({self.x} {self.y})'
#
#     def __add__(self, other): #сложение
#         return Point2D(self.x + other.x, self.y + other.y)
#
#     def __sub__(self, other): #вычитание
#         return Point2D(self.x - other.x, self.y - other.y)
#
#     def __neg__(self): #отрицание
#         return Point2D(-self.x, -self.y)
#
#     def __eq__(self, other): #сравнение
#         return self.x == other.x and self.y == other.y
#
#     def __ne__(self, other): #не равны ли точки
#         return not (self == other)
#
#     def distance(self): #расстояние от точки до центра координат
#         return (self.x ** 2 + self.y ** 2) ** 0.5
#
#
# p1 = Point2D(0, 5)
# p2 = Point2D(-5, 10)
#
# print(p1 + p2)
# print(p1 - p2)
# print(-p2)
# print(p1 == p2, p1 != p2)
# print('Расстояние до центра координат (p1): ', p1.distance())
# print('Расстояние до центра координат (p2): ', p2.distance())


# class Roman:
#     def __init__(self, n, s = 0):
#         self.n = n
#         self.s = s
#
#     def __str__(self):
#         return self.n
#
#     def __add__(self, other):
#         self.s = self.n + other.n
#         return self.checkio()
#
#     def __sub__(self, other):
#         self.s = self.n - other.n
#         return self.checkio()
#
#     def __mul__(self, other):
#         self.s = self.n * other.n
#         return self.checkio()
#
#     def __truediv__(self, other):
#         self.s = self.n / other.n
#         self.s = int(self.s)
#         return self.checkio()
#
#     def checkio(self):
#         result = ''
#
#         for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
#                                  'M     CM    D    CD   C   XC  L   XL  X   IX  V IV I'.split()):
#             result += self.s // arabic * roman
#             self.s %= arabic
#         return result
#
# num = Roman(5)
# num2 = Roman(3)
#
# print(num + num2)
# print(num - num2)
# print(num * num2)
# print(num / num2)

# Класс «Товар»содержит следующие закрытые поля:
# – название товара,
# – название магазина в котором продается товар
# – стоимость товара в рублях
# Класс «Склад» содержит закрытый массив товаров.
# Обеспечить следующие возможности:
# – вывод информации о товаре по номеру с помощью индекса
# – вывод информации о товаре, название которого введено с клавиатуры
# – сортировку товаров по названию магазина, по наименованию и цене;
# – перегруженную операцию сложения товаров, выполняющую сложение их цен.

# class Tovar:
#     def __init__(self, index, title, magazin, price):
#         self.index = index
#         self.title = title
#         self.magazin = magazin
#         self.price = price
#
#
#
# class Sklad():
#     def __init__(self, tovars = []):
#         # super().__init__(index, title, magazin, price)
#         # super().__init__(title)
#         # super().__init__(magazin)
#         # super().__init__(price)
#         self.tovars = tovars
#
#     def print_info(self):
#         for tov in self.tovars:
#             print(tov, end=' ')
#
# tovars = []
# check = input('Ввести товар? ')
# index = 0
# i = 1
# while check != '':
#     title = input('Введите название товара: ')
#     magazin = input('Введите название магазина: ')
#     price = int(input('Введите цену товара: '))
#     index += i
#     tovar = Tovar(index, title, magazin, price)
#     tovars.append(tovar)
#     check = input('Ввести товар? ')
#
# obj = Sklad(tovars)
# obj.print_info()

# s = input()
# count = 0
# ind1 = s.find('h')
# ind2 = s.rfind('h')
# print(s[:ind1], end='')
# print(s[ind2-1:ind1:-1])

# for i in range(len(s)):
#     if s[i] == 'f':
#         ind = i
#         count += 1
#         if count == 2:
#             break
#
#
# if count == 1:
#     print('-1')
# elif count == 0:
#     print('-2')
# else:
#     print(ind)

# 10.11.22

# import re
# from re import *

# s = "Я ищу совпадения  2023 году. И я их найду в 2 счёта. 9578 19_45"
# # reg = r'пад\B'
# reg = r'20*' # шаблон, в данном примере первый символ ищется обязательно,
#             # а ближний символ к звездочке может быть, а может и не быть рядом с первым символом
# reg = r'^\w+\s\w+' # работает во всех языках
# reg = r'\w+\s\w+$' # работает во всех языках
#
# print(re.findall(reg, s))

# Повторения
# + - от 1 до бесконечности повторений
# * - от 0 до бесконечности повторений
# ? - 0 или 1 повторений

# s1 = "Цифры: 7, +17, -42, 0013, 0.3"
# pattern = r'[+-]?\d+\.?\d*' # квадратные скобки указывают возможные символы (либо, либо).
# print(re.findall(pattern, s1))

# s1 = "05-03-1987 # Дата рождения"
#
# # print(re.sub(r'#.*', '', s1)) #метод 'sub' находит и заменяет
# print('Дата рождения:', re.sub(r'-', '.', re.sub(r'#.*', '', s1))) # можно вкладывать методы друг в друга

# s1 = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# pattern = r'\w+\s*=[^;]+'
# print(re.findall(pattern, s1))

# s1 = '12 сентября 2021 года'
# reg1 = r'\d{2,4}'
# print(re.findall(reg1, s1))

# s1 = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
# pattern = r'[+]?7\d{10}'
# print(re.findall(pattern, s1))

# def login(a):
#     return re.findall(r'^[\w!@#$-]{8,25}$', a)
#
# print(login('admin_admin'))
# print(login('*admin_admin'))
# print(login('admin_admin*'))

# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))

# text = """
# one
# two
# """
# print(re.findall(r'one$', text))
# print(re.findall(r'one$', text, re.MULTILINE))

# text = """
# one
# two
# """
# print(re.findall(r'one.\w+', text))
# print(re.findall(r'one.\w+', text, re.DOTALL))

# ДЗ от 10.11.2022
# import re
# print('Пароль должен состоять из цифр, букв ангилйского алфавита,'
#       'символов дефис, собака и подчеркивания. Длина пароля от 6 до 18 символов')
# s = input('Введите пароль для проверки: ')
# pattern = r'[0-9a-zA-Z@-]{6,18}'
# match = re.fullmatch(pattern, s)
# if match:
#       print("Ваш пароль соответствует условию.")
# else:
#       print("Ваш пароль не соответствует условию.")

# 15.11.2022
# import re

# print(re.findall("""
# [A-z.-]+    # комментарий 1
# @           # comment 2
# [a-z_.-]+   # comment 3
# """, 'test@mail.ru', re.VERBOSE))   # данный флаг позволяет добавлять комментарии,
#                                     # а также делать переносы в регулярках. Создан для удобства работы.

# text = 'Hello World'
# print(re.findall(r'\w+', text, re.DEBUG))

# text = """Python,
# python,
# PYTHON"""
# reg = "(?mi)^python"            # (?im) - данное добавление флага идентичено нижнему
# print(re.findall(reg, text))    # flags=re.IGNORECASE|re.MULTILINE

# test = "12345@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
# reg = r'[\w.-]+@[\w.]+[a-z]{2,3}'
# print(re.findall(reg, test))

# text = "<body>Пример жадного соответствия регуляных выражений</body>"
# print(re.findall("<.*>", text)) #данное выражение берет по максимуму все символы, которые соответствуют шаблону
# print(re.findall("<.*?>", text)) #данное выражение берет символы по минимуму, которые соответствуют шаблону

# для ограничения используется знак вопроса '?'
# например *?, +?, ??
# {m,n}?, {,n}?, {m,}?

# t = "2356 564 22 4568"
# reg = r'\d{2,3}?' # в данном случае знак вопроса обозначает минимальное кол-во повторений. Ленивое соответсвие
# print(re.findall(reg, t))

# s = "<p>Изображение <img alt='картинка' src='bg.jpg' title='подсказка'> - фон страницы</p>"
# # reg = r'<img[^>]+>'         # [^>] - означает что мы ищем всё, пока не встретим символ '>'
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+'
# print(re.findall(reg, s))   #нужно получить <img src='bg.jpg'>

# s = "Python (в русском языке встречаются названия питон[16] или пайтон[17] - высокоуровневый язык программирования" \
#     "общего назначения с динамической строгой типизацией и автоматическим управлением памятью[18][19]."
# reg = r"\[\d+\]"
# print(re.findall(reg, s))

# s = 'Петр и Ольга отлично учатся!'
# reg = 'Петр|Виталий|Ольга'
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0, double = 8.0f"
# # reg = r"int\s*=\s*\d[.\w+]*|double\s*=\s*\d[.\w+]*"
# # reg = r"(int|double)\s*=\s*\d[.\w+]*"   # в данном примере круглые скобки являются группирующими сохраняющими и возвращает
#                                         # в данном случае только то что находится в скобках
# reg = r"(?:int|double)\s*=\s*\d[.\w+]*" # в данном случае (?:) скобки не сохраняющие
# print(re.findall(reg,s))

# s = "192.168.8.1"
# # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg = r'(?:\d{1,3}.){3}\d{1,3}'
# print(re.findall(reg, s))

# s = "Word2016, PS6, AI5"
# reg = r'([A-z]+)(\d*)' # в данном примере мы сгруппировали по отдельности буквенные и численные значения
# print(re.findall(reg, s))

# s = "5 + 7*2 - 4"
# # reg = '\s*[+*-]\s*'   # ['5', '7', '2', '4']
# # reg = '\s*([+*-])\s*' # ['5', '+', '7', '*', '2', '-', '4']
# reg = '(\s*[+*-]\s*)'   # ['5', ' + ', '7', '*', '2', ' - ', '4']
# print(re.split(reg, s))

# s = 'Я ищу совпадения в 2023 годуб И я их найду в 2 счёта.'
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[1]) # получили результат первой круглой скобки в шаблоне
# print(m[2]) # получили результат второй круглой скобки в шаблоне
# print(m[0]) # получили результат всего шаблона.

# s = input("Введите дату в формате 'xx-xx-xxxx': ")
# # s = '31-12-1999'
# reg = r"([0-2][0-9]|30|31).([0-1][0-2]).([0-2]0[0-2][0-9]|19[0-9][0-9])"
# print(re.findall(reg, s))

print('Hello')
