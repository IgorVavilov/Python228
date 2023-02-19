# --КЛАССЫ--
# у класса есть свойства (поля, переменная)
# class Point:
#     """Класс для представления координат точек на плоскости"""
#     x = 1
#     y = 1


# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))

# p1 = Point()
# p2 = Point()
# print(p1.x) # выводим значение переменной 'x', экземпляра класса
#
# p1.x = 100 # присваеваем переменной 'x' новое значение, экземпляра класса
# p2.x = 200
#
# print(p1.x)
# print(p2.x)
# print(Point().x)
#
# print(id(p1))
# print(id(p2))
# print(id(Point))

# class Point:
#     x = 1
#     y = 1
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# p1.z = 20
# print(p1.x, p1.y)
# print(p1.__dict__) # __dict__ - отображает свойства класса. У экземпляра класса __dict__ пустой по умаолчанию.

# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self):
#         print(self.__dict__)

# Методы это функции внутри класса. Атрибуты класса - это методы и свойства класса
# Методы могут вызываться только у экземпляра класса.

#
# p1 = Point()
# print(p1.x)
# p1.x = 5
# p1.y = 10
# p1.set_coord()
# Point.set_coord(p1)
# p2 = Point()
# p2.x = 2
# p2.y = 6
# p2.set_coord()

# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# p1.set_coord(5, 10)
# print(p1.__dict__)

# class Human:
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '000-00-00'
#     country = 'counrty'
#     city = 'city'
#     address = 'street, house'
#
#     def print_info(self):
#         print(' Персональные данные '.center(40, "*"))
#         print(f'Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n'
#               f'Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}')
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):   # установить имя
#         if isinstance(name, str):
#             self.name = name
#
#     def get_name(self): # получить имя
#         return self.name
#
# # ДЗ от 06.12.2022
#
#     def set_birthday(self, birthday):
#         self.birthday = birthday
#
#     def get_birthday(self):
#         return self.birthday
#
#     def set_phone(self, phone):
#         self.phone = phone
#
#     def get_phone(self):
#         return self.phone
#
#     def set_country(self, country):
#         self.country = country
#
#     def get_country(self):
#         return self.country
#
#     def set_city(self, city):
#         self.city = city
#
#     def get_city(self):
#         return self.city
#
#     def set_address(self, address):
#         self.address = address
#
#     def get_address(self):
#         return self.address
#
# h1 = Human()
# h1.print_info()
#
# h1.input_info('Юля', '23.05.1986', '45-46-98', 'Россия', 'Москва', 'Чистопрудный бульвар, 1А')
# h1.print_info()
# h1.set_name('Алефтина')
# h1.print_info()
# print(h1.get_name())
# h1.set_city("Питер")
# print(h1.get_city())

# Реализуйте класс "Книга". Необходимо хранить в полях класса: название книги, год выпуска, издателя, жанр,
# автора, цену. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям
# через методы класса.

# class Book:
#     title = "KGBT+"
#     year = "2022"
#     publisher = "Эксмо"
#     genre = "проза"
#     author = "Виктор Пелевин"
#     price = "945"
#
#     def print_info(self):
#         print('=' * 50)
#         print(f'Название книги: {self.title}\nГод выпуска: {self.year}\nИздатель: {self.publisher}\n'
#               f'Жанр: {self.genre}\nАвтор: {self.author}\nЦена: {self.price}')
#
#     def input_info(self, title, year, publisher, genre, author, price):
#         self.title = title
#         self.year = year
#         self.publisher = publisher
#         self.genre = genre
#         self.author = author
#         self.price = price
#
#     def set_title(self, title):
#         self.title = title
#
#     def get_title(self):
#         return self.title
#
#     def set_year(self, year):
#         self.year = year
#
#     def get_year(self):
#         return self.year
#
#     def set_publisher(self, publisher):
#         self.publisher = publisher
#
#     def get_publisher(self):
#         return self.publisher
#
#     def set_genre(self, genre):
#         self.genre = genre
#
#     def get_genre(self):
#         return self.genre
#
#     def set_author(self, author):
#         self.author = author
#
#     def get_author(self):
#         return self.author
#
#     def set_price(self, price):
#         self.price = price
#
#     def get_price(self):
#         return self.price
#
#
# b1 = Book()
# b1.print_info()
# b1.input_info('Боги и Чудовища', '2022', 'АСТ', 'Фэнтези', 'Шелби Махёрин', '865')
# b1.print_info()
# b1.set_price('999')
# b1.print_info()
# print(b1.get_price())

# ДЗ от 01.12.2022

# with open('one.txt', 'r') as f_one:
#     list_one = f_one.readlines()
#
# with open('two.txt', 'r') as f_two:
#     list_two = f_two.readlines()
#
# with open('three.txt', 'w') as f_three:
#     list_three = list_one + list_two
#     for item in list_three:
#         f_three.write(item)

# 08/12/2022

# class Person:
#     skill = 10
#
#     def __init__(self, name, surname): # инициализатор, отрабатывает в момент, когда создаем экземпляр класса
#         self.name = name
#         self.surname = surname
#
#     def print_info(self):
#         print('Данные сотрудника: ', self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print('Квалификация сотрудника: ', self.skill, '\n')
#
# p1 = Person('Viktor', 'Reznik')
# p1.print_info()
# p1.add_skill(3)
#
# p2 = Person('Anna', 'Dolgih')
# p2.print_info()
# p2.add_skill(2)

# class Point:
#     # def __new__(cls, *args, **kwargs): # конструктор класса, обычно не используется при создании классов
#     #     print('Конструктор')
#     #     return super().__new__(cls)
#
#     def __init__(self, x, y):
#         print('Инициализатор')
#         self.x = x
#         self.y = y
#
#     def __del__(self):  # удаление экземпляра класса, обычно не используется
#         print('Удаление экземпляра', self.__class__.__name__)
#
#     def print_coord(self):
#         print(f'x: {self.x}, y: {self.y}')
#
# p1 = Point(5, 10)
# p1.print_coord()
# print(id(p1))
#
# p2 = Point(2, 7)
# p2.print_coord()
# print(id(p2))


# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
# p1 = Point(5, 10)
# print(p1.count)
# p2 = Point(7, 2)
# print(p2.count)
# p3 = Point(3, 6)
# print(p2.count)

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print('Инициализация робота: ', self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, 'выключается!')
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, 'был последним')
#             # print('Численость роботов', Robot.k)
#         else:
#             print('Работающих роботов осталось:', Robot.k)
#
#     def say_hi(self):
#         print('Приветствую! Меня зовут', self.name)
#
#
# droid1 = Robot("R2-D1")
# droid1.say_hi()
# print('Численность роботов:', Robot.k)
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print('Численность роботов:', Robot.k)
#
# print('\nЗдесь роботы могут проделать какую-то работу\n')
# print('Роботы закончили свою работу. Давайте их выключим.')
# del droid1
# del droid2
# print('Численность роботов:', Robot.k)

# --ИНКАПСУЛЯЦИЯ--

# class Point:
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print('Координаты должны быть числами.')
#
#     def get_coord(self):
#         return self.__x, self.__y
#
# p1 = Point('5', 10)
# print(p1.get_coord())
# p1.set_coord(3, 3.6)
# print(p1.get_coord())
# p1.__x = 100
# p1.__y = 'abc'
# # print(p1.x, p1.y)
# print(p1.__dict__)

# Модификаторы доступа:
# public (self.x) -
# protected (self._x) - используется при наследовании
# privat (self.__x)

# ДЗ от 08.12.2022
# Создать класс Rectangle, описывающий прямоугольник.
# В классе должны быть все необходимые методы, а так же методы вычисления площади,
# периметра и диагонали, и метод, который рисует прямоугольник.

# class Rectangle:
#
#     def __init__(self, dlinna, shirina):
#         self.__dlinna = self.__shirina = 0
#         if Rectangle.__check_value(shirina) and Rectangle.__check_value(dlinna):
#             self.__dlinna = dlinna
#             self.__shirina = shirina
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_param(self, dlinna, shirina):
#         if Rectangle.__check_value(dlinna) and Rectangle.__check_value(shirina):
#             self.__dlinna = dlinna
#             self.__shirina = shirina
#         else:
#             print('Параметры прямоугольника должны быть числовыми.')
#
#     def get_param(self):
#         print('Длинна прямоугольника:', self.__dlinna)
#         print('Ширина прямоугольника:', self.__shirina)
#
#     def ploshad(self):
#         print('Площадь прямоугольника:', self.__dlinna * self.__shirina)
#
#     def perimetr(self):
#         print('Периметр прямоугольника:', (self.__dlinna * 2) + (self.__shirina * 2))
#
#     def gipotenuza(self):
#         c = ((self.__dlinna ** 2) + (self.__shirina ** 2)) ** 0.5
#         print('Гипотенуза прямоугольника:', round(c, 2))
#
#     def drow_rectangle(self):
#         for i in range(self.__dlinna):
#             print('*' * self.__shirina)
#
# r1 = Rectangle('8', 10)
# r1.get_param()
# r1.set_param(3, 9)
# r1.get_param()
# r1.ploshad()
# r1.perimetr()
# r1.gipotenuza()
# r1.drow_rectangle()

# ---13.12.2022---

# class Point:
#     __slots__ = ['__x', '__y', 'z'] #ограничиваем свойства, которые используются в классе. И не можем добовлять из вне.
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print('Координаты должны быть числами.')
#
#     def get_coord(self):
#         return self.__x, self.__y

# p1 = Point('5', 10)
# p1.z = 15
# print(p1.z)
# print(p1.get_coord())
# p1.set_coord(3, 3.6)
# print(p1.get_coord())
# p1.__x = 100
# p1.__y = 'abc'
# # print(p1.x, p1.y)
# print(p1.__dict__)

# class Point:
#     def __init__(self, x = 0, y = 0):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         print("Вызов __set_x")
#         self.__x = x
#
#     def __get_x(self):
#         print("Вызов __get_x")
#         return self.__x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     x = property(__get_x, __set_x, __del_x) # свойства прописываются строго в такой последовательности.
#
# p1 = Point(5, 10)
# p1.x = 3
# print(p1.x)
# del p1.x

# -- нижний код повторяет код прописанный выше---

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     @property  # декоратор
#     def x(self):  # __get_x
#         print("Вызов __get_x")
#         return self.__x
#
#     @x.setter
#     def x(self, x):  # __set_x
#         print("Вызов __set_x")
#         self.__x = x
#
#     @x.deleter
#     def x(self):  # __del_x
#         print("Удаление свойства")
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x) # свойства прописываются строго в такой последовательности.
#
#
# p1 = Point(5, 10)
# p1.x = 3
# print(p1.x)
# del p1.x

# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются только числами.")
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, "кг =>", end=' ')
# print(weight.to_pounds(), 'фунтов')
# weight.kg = 41
# print(weight.kg, "кг =>", end=' ')
# print(weight.to_pounds(), 'фунтов')
# weight.kg = 'десять'
# print(weight.kg, "кг =>", end=' ')
# print(weight.to_pounds(), 'фунтов')

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def age(self):
#         return self.age
#
#     @age.setter
#     def age(self, age):
#         self.__age = age
#
#     @age.deleter
#     def age(self):
#         del self.__age
#
# p1 = Person("Petr", 39)
# print(p1.__dict__)
# p1.name = 'Igor'
# p1.age = 26
# print(p1.__dict__)
# del p1.name
# print(p1.__dict__)

# class Point:
#     __count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point(5, 10)
# p2 = Point(4, 2)
# p3 = Point(4, 9)
#
# print(Point.get_count())

# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
# print(Change.inc(10), Change.dec(10))   # К статическим методам мы можем обращасть как через метод,
#                                         # татк и через экземпляр класса

# class Matim:
#     @staticmethod
#     def max(*args):
#         x = args[0]
#         for i in args:
#             if i > x:
#                 x = i
#         return i
#
#     @staticmethod
#     def min(*args):
#         return min(args)
#
#     @staticmethod
#     def arf(*args):
#         return sum(args) / len(args)
#
#     @staticmethod
#     def factorial(a):
#         x = 1
#         for i in range(1, a+1):
#             x *= i
#         return x
#
# print(Matim.max(3, 5, 7, 9, 8, 11))
# print(Matim.arf(3, 5, 7, 9))
# print(Matim.factorial(5))

# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('.'))
#         date1 = cls(day, month, year)
#         return date1
#
#
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#
# string_date = Date.from_string('23.11.2022')
# print(string_date.string_to_db())
# string_date1 = Date.from_string('21.01.2022')
# print(string_date1.string_to_db())

# ДЗ от 13.12.2022
#
# class Figure:
#     count = 0
#
#     @staticmethod
#     def triangle_area_geron(a, b, c):
#         p = (a+b+c)/2
#         s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#         Figure.count += 1
#         return s
#
#     @staticmethod
#     def triangle_area_base_hight(a, h):
#         Figure.count += 1
#         return a * h * 0.5
#
#     @staticmethod
#     def square_area(a):
#         Figure.count += 1
#         return a ** 2
#
#     @staticmethod
#     def rectangular_area(a, b):
#         Figure.count += 1
#         return a * b
#
#     @staticmethod
#     def count_def_sqr():
#         return Figure.count
#
#
# print('Площадь треугольника по формуле Герона:', Figure.triangle_area_geron(3, 4, 5))
# print('Площадь треугольника через основание и высоту:', Figure.triangle_area_base_hight(6, 7))
# print('Площадь квадрата:', Figure.square_area(7))
# print('Площадь прямоугольника:', Figure.rectangular_area(2, 6))
# print('Количество подсчета площади:', Figure.count_def_sqr())

# --- 15.12.2022 ---

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт')
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eru_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def print_balance(self):
#         print(f"Текущий банас {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print('Информация о счете')
#         print('-' * 20)
#         print(f'#{self.num}')
#         print(f'Владелец: {self.surname}')
#         self.print_balance()                    # вызываем другой метод внутри класса
#         print(f'Проценты: {self.percent:.1%}')  # превращение десятичного числа в проценты,
#                                                 # число указывает кол-во знаков после запятой
#         print('-' * 20)
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print('Проценты были успешно начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f'К сожалению у Вас нет {val} {Account.suffix}')
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} была успешна снята!')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}')
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# Account.set_eru_rate(3)
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.edit_owner('Дюма')
# acc.print_info()
# print()
# acc.add_percents()
# print()
# acc.withdraw_money(1000)
# print()
# acc.add_money(5000)

# дз от 15.12.2022 через set/get

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт.")
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.__num} принадлежащий {self.__surname} был закрыт')
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eru_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def print_balance(self):
#         print(f"Текущий банас {self.__value} {Account.suffix}")
#
#     def print_info(self):
#         print('Информация о счете')
#         print('-' * 20)
#         print(f'#{self.__num}')
#         print(f'Владелец: {self.__surname}')
#         self.print_balance()                    # вызываем другой метод внутри класса
#         print(f'Проценты: {self.__percent:.1%}')  # превращение десятичного числа в проценты,
#                                                 # число указывает кол-во знаков после запятой
#         print('-' * 20)
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def set_num(self, num):
#         self.__num = num
#
#     def get_num(self):
#         return self.__num
#
#     def set_surname(self, surname):
#         self.__surname = surname
#
#     def get_surname(self):
#         return self.__surname
#
#     def set_percent(self, percent):
#         self.__percent = percent
#
#     def get_percent(self):
#         return self.__percent
#
#     def set_value(self, value):
#         self.__value = value
#
#     def get_value(self):
#         return self.__value
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print('Проценты были успешно начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f'К сожалению у Вас нет {val} {Account.suffix}')
#         else:
#             self.__value -= val
#             print(f'{val} {Account.suffix} была успешна снята!')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}')
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# Account.set_eru_rate(3)
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.set_surname('Дюма')
# acc.print_info()
# print()
# acc.add_percents()
# print()
# acc.withdraw_money(1000)
# print()
# acc.add_money(5000)

# --через Декораторы--

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт.")
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.__num} принадлежащий {self.__surname} был закрыт')
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eru_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def print_balance(self):
#         print(f"Текущий банас {self.__value} {Account.suffix}")
#
#     def print_info(self):
#         print('Информация о счете')
#         print('-' * 20)
#         print(f'#{self.__num}')
#         print(f'Владелец: {self.__surname}')
#         self.print_balance()  # вызываем другой метод внутри класса
#         print(f'Проценты: {self.__percent:.1%}')  # превращение десятичного числа в проценты,
#         # число указывает кол-во знаков после запятой
#         print('-' * 20)
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @property
#     def num(self):
#         return self.__num
#
#     @num.setter
#     def num(self, num):
#         self.__num = num
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, surname):
#         self.__surname = surname
#
#     @property
#     def percent(self):
#         return self.__percent
#
#     @percent.setter
#     def percent(self, percent):
#         self.__percent = percent
#
#     @property
#     def value(self):
#         return self.__value
#
#     @value.setter
#     def value(self, value):
#         self.__value = value
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print('Проценты были успешно начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f'К сожалению у Вас нет {val} {Account.suffix}')
#         else:
#             self.__value -= val
#             print(f'{val} {Account.suffix} была успешна снята!')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}')
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# Account.set_eru_rate(3)
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.surname = 'Дюма'
# acc.num = '345789'
# acc.print_info()
# print()
# acc.add_percents()
# print()
# acc.withdraw_money(1000)
# print()
# acc.add_money(5000)

# import re
#
#
# class UserData:
#
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_weight(weight)
#         # self.verify_ps(ps)
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")  # выбрасывает исключение
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError('Неверный форма ФИО')
#         letters = "".join(re.findall('[a-zа-яё-]', fio, flags=re.IGNORECASE))
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError('Возраст должен быть числом в диапазоне от 14 до 120 лет.')
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError('Вес должен быть вещественным числом от 20 кг и выше.')
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError('Паспорт должен быть строкой')
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError('Неверный формат паспорта')
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError('Серия и номер паспорта должны состоять из цифр')
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
# # Урок 20.12.2022
#
# p1 = UserData('Волков Игорь Николаевич', 25, '1234 567890', 80.8)
# p1.fio = "Быков Игорь Николаевич"
# print(p1.fio)

# --НАСЛЕДОВАНИЯ--


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         print('Инициализатор базового класса')
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         # Point.__init__(self, *args)
#         print("Переопределенный инициализатор Line")
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}')
#
#
# class Rect(Prop):
#     def __init__(self, sp, ep, color, width, bg='yellow'):
#         super().__init__(sp, ep, color, width)
#         self._background = bg
#
#     def draw_rect(self):
#         print(
#             f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self.get_width()}, {self._background}')
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# rect = Rect(Point(30, 40), Point(70, 80), 'red', 10)
# rect.draw_rect()

# DRY (Don't Repeat Yourself) - Не повторяйся

# --22.12.2022--


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     def __str__(self):
#         return f'{self.__color}'
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.width = width
#         self.height = height
#
#     def __str__(self):
#         return f"{self.__width}, {self.__height}, {self.color}"
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError('Укажите положительное число')
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError('Укажите положительное число')
#
#     def area(self):
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, 'green')
# print(rect.width)
# print(rect.height)
# print(rect.color)
# rect.color = 'red'
# print(rect)
# rect.width = 5
# rect.height = 8
# print(rect)
# print(rect.area())


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f'Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}')
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         self.fon = background
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print('Фон:', self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         self.border = border
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print('Рамка: ', self.border)
#
#
# class RectFonBorder(RectFon):
#     def __init__(self, width, height, background, border):
#         super().__init__(width, height, background)
#         self.border = border
#
#     def show_rect(self):
#         super().show_rect()
#         print('Рамка: ', self.border)
#
#
# shape = Rect(100, 200)
# shape.show_rect()
# print()
# shape1 = RectFon(400, 300, 'yellow')
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 500, '1px solid red')
# shape2.show_rect()
# print()
# shape3 = RectFonBorder(300, 400, 'black', '2px solid red')
# shape3.show_rect()


# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))

# --Перегрузка методов--

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print('Координаты должны быть целочисленными')
#             return False
#         return True
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         print('Инициализатор базового класса')
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#
#
# class Line(Prop):
#
#     def draw_line(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(20, 40), Point(50, 60))
# line.draw_line()
# line.set_coords(Point(200, 400))
# line.draw_line()

# --Абстрактные методы--

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print('Координаты должны быть целочисленными')
#             return False
#         return True
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         print('Инициализатор базового класса')
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw_line(self):
#         raise NotImplementedError('В дочернем классе должен быт определен метод draw()')
#
#
# class Line(Prop):
#
#     def draw_line(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#     pass
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()

# дз от 22.12.2022

# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if length is None:
#             self._width = width
#             self._length = self._width
#         else:
#             self._width = width
#             self._length = length
#         self._radius = radius
#
#     def area_rect_table(self):
#         raise NotImplementedError("В дочернем классе должен быт определен метод area_rect_table()")
#
#     def area_circle_table(self):
#         raise NotImplementedError("В дочернем классе должен быт определен метод area_circle_table()")
#
#
# class RectTable(Table):
#     def area_rect_table(self):
#         return self._width * self._length
#     pass
#
#
# class CircleTable(Table):
#     def area_circle_table(self):
#         return round(3.14141414 * (self._radius ** 2), 2)
#     pass
#
# table1 = RectTable(20, 10)
# print(table1.__dict__)
# print(table1.area_rect_table())
# table2 = RectTable(20)
# print((table2.__dict__))
# print(table2.area_rect_table())
# table3 = CircleTable(radius=20)
# print(table3.__dict__)
# print(table3.area_circle_table())

# Lesson -- 27.12.2022 --

# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self._width = width
#                 self._length = self._width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def area_table(self):
#         raise NotImplementedError("В дочернем классе должен быт определен метод area_table()")
#
#
# class RectTable(Table):
#     def area_table(self):
#         return self._width * self._length
#
#
# class CircleTable(Table):
#     def area_table(self):
#         return round(3.14141414 * self._radius ** 2, 2)
#
#
# table1 = RectTable(20, 10)
# print(table1.__dict__)
# print(table1.area_table())
# table2 = RectTable(20)
# print(table2.__dict__)
# print(table2.area_table())
# table3 = CircleTable(radius=20)
# print(table3.__dict__)
# print(table3.area_table())

# Импорт абстракт-методов

# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         # print("Переместил шахматную фигуру")
#         pass
#
#
# class Queen(Chess):
#     def move(self):
#         print("Переместил шахматную фигуру")
#
#
# q = Queen()
# q.draw()
# q.move()

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=' ')
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         rub = self.value * Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# print('*' * 50)
# for elem in d:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')
# print()
#
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print('*' * 50)
# for elem in e:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')

# -- ИНТЕРФЕЙСЫ -- интерфейсный класс - это абстрактный класс, который состоит только из абстрактных методов

# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Дочерний класс")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("Внучатый класс")
#
#
# gc = GrandChild()
# gc.display2()
# gc.display1()

# -- ВЛОЖЕННЫЕ КЛАССЫ --

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_class_method():
#         print("Я метод внешнего класса")
#
#     def outer_obj_method(self):
#         print('Я - связующий метод')
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print('Я метод вложенного класса', MyOuter.age, self.obj.name)
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter('внешний')
# print(out.name)
# inner = out.MyInner('внутренний', out)
# print(inner.inner_name)
# inner.inner_method()

# class Color:
#     def __init__(self):
#         self.name = 'Green'
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print('Name:', self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = "Light green"
#             self.code = '021sdf'
#
#         def display(self):
#             print('Name:', self.name)
#             print('Code:', self.code)
#
#
# outer = Color()
# outer.show()
#
# g = outer.lg
# g.display()

# дз от 27.12.2022

# class Student:
#     def __init__(self):
#         self.name = "Roman"
#         self.nb = self.Notebook()
#
#     def print_info(self):
#         print(self.name, '=>', end=' ')
#         self.nb.print_info()
#
#     class Notebook:
#         def __init__(self):
#             self.model = 'HP'
#             self.cpu = 'i7'
#             self.memory = '16'
#
#         def print_info(self):
#             print(f'{self.model}, {self.cpu}, {self.memory}')
#
#
# st = Student()
# st.print_info()
# st.name = 'Vladimir'
# st.print_info()


# дз от 20.12.2022


# class Automobile:
#
#     def __init__(self, model_name, year, product, power, color, price):
#         self.model_name = model_name
#         self.year = year
#         self.product = product
#         self.power = power
#         self.color = color
#         self.price = price
#
#     @staticmethod
#     def verify_model_name(model_name):
#         if not isinstance(model_name, str):
#             raise TypeError("Название модели должно быть строкой")
#
#     @staticmethod
#     def verify_year(year):
#         if not isinstance(year, int):
#             raise TypeError('Год должен быть числом')
#
#     @staticmethod
#     def verify_product(product):
#         if not isinstance(product, str):
#             raise TypeError("Производитель модели должно быть строкой")
#
#     @staticmethod
#     def verify_price(price):
#         if not isinstance(price, int):
#             raise TypeError('Цена должна быть числом')
#
#     @property
#     def model_name(self):
#         return self.__model_name
#
#     @model_name.setter
#     def model_name(self, model_name):
#         self.verify_model_name(model_name)
#         self.__model_name = model_name
#
#     @property
#     def year(self):
#         return self.__year
#
#     @year.setter
#     def year(self, year):
#         self.verify_year(year)
#         self.__year = year
#
#     @property
#     def product(self):
#         return self.__product
#
#     @product.setter
#     def product(self, product):
#         self.verify_product(product)
#         self.__product = product
#
#     @property
#     def power(self):
#         return self.__power
#
#     @power.setter
#     def power(self, power):
#         self.__power = power
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, color):
#         self.__color = color
#
#     @property
#     def price(self):
#         return self.__price
#
#     @price.setter
#     def price(self, price):
#         self.verify_price(price)
#         self.__price = price
#
#     def print_info(self):
#             print('*' * 11, 'Данные автомобиля', '*' * 11)
#             print(f'Название модели: {self.model_name}')
#             print(f'Год выпуска: {self.year}')
#             print(f'Производитель: {self.product}')
#             print(f'Мощность двигателя: {self.power}')
#             print(f'Цвет: {self.color}')
#             print(f'Цена: {self.price}')
#             print('=' * 42)
#
#
# a1 = Automobile('X7 M50i', 2021, 'BMW', '530 л.с.', 'white', 107900000)
# a1.print_info()
# a1.model_name = 'Cadilac'
# print()
# a1.print_info()

# Урок от 29.12.2022

# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print('Name:', self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = "Smith"
#             self.id = "657"
#
#         def display(self):
#             print('Name:', self.name)
#             print('Id:', self.id)
#
#     class Head:
#         def __init__(self):
#             self.name = "Alba"
#             self.id = "007"
#
#         def display(self):
#             print('Name:', self.name)
#             print('Id:', self.id)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# print()
# d1.display()
# d2 = outer.head
# print()
# d2.display()

# class Computer:
#     def __init__(self, name, os1, brand):
#         self.name = name
#         self.os = self.OS(os1)
#         self.cpu = self.CPU(brand)
#
#     class OS:
#         def __init__(self, title):
#             self.title = title
#
#         def system(self):
#             return self.title
#
#     class CPU:
#         def __init__(self, brand):
#             self.brand = brand
#
#         def make(self):
#             return self.brand
#
#         def model(self, model):
#             return model
#
#
# comp = Computer('PC001', 'Windows-7', "Intel")
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model('Core-i7'))


# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print('In Base Class')
#
#     class Inner:
#         def display1(self):
#             print("Inner of Base Class")
#
#
# class SubClass(Base):
#     def __init__(self):
#         print("In SubClass")
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print("Inner of SubClass")
#
#
# a = SubClass()
# a.display()
#
# # b = a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()

###################################################
# --МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ-- когда дочерние классы могут наследоваться от нескольких родительских классов

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + ' is sleeping')
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + ' is playing')
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + ' is barking')
#
#
# beast = Dog('Buddy')
# beast.bark()
# beast.sleep()
# beast.play()

# class MyClass:
#     pass
# obj = MyClass()
# obj.a = 1
# obj.b = 2
# obj.i = 3
# obj.ireal = 3.5
# obj.integer = 4
# obj.z = 5
#
# def incIntsI(obj):
#     for name in obj.__dict__.keys():
#         if name.startswith('i'):
#             val = getattr(obj, name)
#             if isinstance(val, int):
#                 setattr(obj, name, val + 1)
# print(obj.__dict__)
# incIntsI(obj)
# print(obj.__dict__)

# class A:
#     def __init__(self):
#         print("A")
#
#
# class AA:
#     pass
#
#
# class B(A):
#     # def __init__(self):
#     #     print('B')
#
#     def hi(self):
#         print('B_hi')
#
#
# class C(AA):
#     # def __init__(self):
#     #     print('C')
#
#     def hi(self):
#         print('C_hi')
#
#
# class D(B, C):
#     # def __init__(self):
#     #     B.__init__(self)
#     #     C.__init__(self)
#     #     print('D')
#
#     def hi(self):
#         C.hi(self)
#         print('D_hi')
#
#
# d = D()
# d.hi()
# print(D.mro())
# print(D.__mro__)

# class B:
#     def __init__(self):
#         print('B')
#
#
# class C:
#     def __init__(self):
#         print('C')
#
#
# class D(B, C):
#     def __init__(self):
#         B.__init__(self)
#         C.__init__(self)
#         print('D')
#
#
#
# d = D()
# print(D.mro())
# print(D.__mro__)

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#
# class Style:
#     def __init__(self, color = 'red', width=1):
#         print('Инициализатор Style')
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print('Инициализатор Pos')
#         self._sp = sp
#         self._ep = ep
#         Style.__init__(self, *args)     # super().__init__(*args)
#
#
# class Line(Pos, Style):
#     # def __init__(self, sp: Point, ep: Point, color = 'red', width=1):
#     #     Pos.__init__(self, sp, ep)
#     #     Style.__init__(self, color, width)
#
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), 'green', 5)
# l1.draw()
# print(Line.mro())

# ------ Миксин (примеси) -------

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename='subclasslog.txt')
#
#
# sub = MySubClass()
# sub.display("Строка будет отображаться и регистрироваться в файле")

# ---Урок 10.01.2023---

# class Goods:
#     def __init__(self, name, weight, price):
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#         super().__init__(name, weight, price)
#
#     def print_info(self):
#         print(f'{self.name}, {self.weight}, {self.price}')
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self, name, weight, price):
#         super().__init__(name, weight, price)
#         print("Init MixinLog")
#         MixinLog.ID += 1
#         self.id = self.ID
#         self.goods = Goods(name, weight, price)
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 00:00 {self.goods.name}")
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook('HP', 1.5, 35000)
# # p = NoteBook('RR', 2.0, 45000)
# n.print_info()
# n.save_sell_log()


# ---Перегрузка операторов---

# 24 * 60 * 60 = 86400 (кол-во секунд в одном дне)

# class Clock:
#     DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.sec = sec % self.DAY
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec + other.sec)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec - other.sec)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec * other.sec)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec // other.sec)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec % other.sec)
#
#     def __eq__(self, other):
#         if self.sec == other.sec:
#             return True
#         return False
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#
# c1 = Clock(100)
# c2 = Clock(200)
# c4 = Clock(300)
# c3 = c1 + c2 + c4
# print(c1.get_format_time())
# print(c2.get_format_time())
# if c1 == c2:
#     print("Время равно")
# else:
#     print("Время разное")
# print(c4.get_format_time())
# print(c3.get_format_time())
# c3 = c4 - c1
# print(c3.get_format_time())
# c3 = c4 // c1
# print(c3.get_format_time())
# c3 = c4 * c1
# print(c3.get_format_time())
# c3 = c1 % c2
# print(c3.get_format_time())


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError('Неверный индекс')
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым не отрицательным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student('Сергей', [5, 4, 5, 6, 4, 3])
# print(s1[3])
# s1[10] = 2
# del s1[2]
# # print(s1.marks[3])
# print(s1.marks)

# class Clock:
#     DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.sec = sec % self.DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == 'hour':
#             return (self.sec // 3600) % 24
#         elif item == 'min':
#             return (self.sec // 60) % 60
#         elif item == 'sec':
#             return self.sec % 60
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if not isinstance(value, int):
#             raise ValueError('Значение должно быть целым числом')
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == 'hour':
#             self.sec = s + 60 * m + value * 3600
#         elif key == 'min':
#             self.sec = s + 60 * value + h * 3600
#         elif key == 'sec':
#             self.sec = value + 60 * m + h * 3600
#
#         return "Неверный ключ"
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# c1['hour'] = 10
# c1['min'] = 10
# c1['sec'] = 15
# print(c1['hour'], c1['min'], c1['sec'])
# print(c1.get_format_time())

# дз от 10.01.2023
# import random
#
#
# class Cat:
#     child_sex = ['М', 'Ж']
#     child_name = 'No name'
#     child_age = 0
#     child_lst = []
#
#     def __init__(self, name, sex):
#         self.name = name
#         self.sex = sex
#
#     def print_info(self):
#         if self.sex == 'М':
#             return f'{self.name} хороший мальчик.'
#         elif self.sex == 'Ж':
#             return f'{self.name} хорошая девочка.'
#
#     def __add__(self, other):
#         if (not self.sex == 'М' or not other.sex == 'Ж') and (not self.sex == 'Ж' or not other.sex == 'М'):
#             raise ValueError("Питомцы должны быть разнополыми")
#         return self.make_child()
#
#     def make_child(self):
#         for i in range(random.randint(1, 7)):
#             child_sex = random.choice(Cat.child_sex)
#             child = f'Cat(name={Cat.child_name}, age={Cat.child_age}, sex={child_sex})'
#             Cat.child_lst.append(child)
#         return Cat.child_lst
#
# cat1 = Cat('Мурзик', 'М')
# cat2 = Cat('Майка', 'Ж')
# print(cat1.print_info())
# print(cat2.print_info())
# cat3 = cat1 + cat2
# print(cat3)

# import random
#
# class Cat:
#     def __init__(self, name, pol, age):
#         self.name = name
#         self.pol = pol
#         self.age = age
#
#     def __str__(self):
#         if self.pol == 'M':
#             return f'{self.name} is good boy!!!'
#         elif self.pol == 'F':
#             return f'{self.name} is good girl!!!'
#         else:
#             return f'{self.name} is good Kitty!!!'
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, sex='{self.pol}')"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat('No name', random.choice(['M', 'F']), 0) for _ in range(random.randint(1, 3))]
#         else:
#             return "Types are not support!"
#
#
# cat1 = Cat('Tom', 4, 'M')
# print(cat1)
# cat2 = Cat('Elsa', 5, 'F')
# print(cat2)
# print(cat1 + cat2)
# cat3 = Cat('Ron', 6, 'M')
# print(cat3)
# print(cat1 + cat3)


# ---Урок от 12.01.2023---

# --Полиморфизм--

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# # print(r1.get_per_rect(), r2.get_per_rect())
# # print()
#
# s1 = Square(10)
# s2 = Square(20)
#
# # print(s1.get_per_sq(), s2.get_per_sq())
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimetr())


# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
#
# t1 = Number(10)
# t2 = Text('Python')
#
# print(t1.total(35))
# print(t2.total(35))


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f'Я кот. Меня зовут {self.name}. Мой возраст {self.age}'
#
#     def make_sound(self):
#         return f'{self.name} мяукает'
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f'Я собака. Меня зовут {self.name}. Мой возраст {self.age}'
#
#     def make_sound(self):
#         return f'{self.name} гавкает'
#
#
# cat1 = Cat('Пушок', 2.5)
# dog1 = Dog('Мухтар', 4)
#
# animals = [cat1, dog1]
#
# for a in animals:
#     print(a.info())
#     print(a.make_sound())


# class Human:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f'{self.surname}, {self.name}, {self.age}'
#
#
# class Student(Human):
#     def __init__(self, surname, name, age, spec, group, rate):
#         super().__init__(surname, name, age)
#         self.spec = spec
#         self.group = group
#         self.rate = rate
#
#     def info(self):
#         return f'{super().info()}, {self.spec}, {self.group}, {self.rate}'
#
#
# class Teacher(Human):
#     def __init__(self, surname, name, age, sub, rate):
#         super().__init__(surname, name, age)
#         self.sub = sub
#         self.rate = rate
#
#     def info(self):
#         return f'{super().info()}, {self.sub}, {self.rate}'
#
#
# class Graduate(Student):
#     def __init__(self, surname, name, age, spec, group, rate, top):
#         super().__init__(surname, name, age, spec, group, rate)
#         self.top = top
#
#     def info(self):
#         return f'{super().info()}, {self.top}'
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
#
# for i in group:
#     print(i.info())


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'{self.__class__}: {self.name}'
#
#     def __str__(self):
#         return f'{self.name}'
#
# cat = Cat('Пушок')
# print(cat)


# class Point:
#     def __init__(self, *args):
#         self.__coord = args
#
#     def __len__(self):
#         return len(self.__coord)
#
#
# p = Point(2, 7)
# print(len(p))

# import math
#
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# pt = Point(1, 2)
# print(pt.length)
# pt.z = 3
# print(pt.__dict__)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# pt2 = Point2D(1, 2)
# print('pt =', pt.__sizeof__())
# print('pt2 =', pt2.__sizeof__() + pt2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ('x', 'y') # slots создает список либо кортеж элементов. при этом мы не можем в объект
#                             # ничего добавить. Как бы создается закрытый список. В таких объектах
#                             # отсутствует __dict__
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z', # запятая в конце означает кортеж. slots должен быть либо кортежем, либо списком
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt = Point(1, 2)
# pt3 = Point3D(10, 20, 30)
# # pt3.z = 30
# print(pt3.x, pt3.y, pt3.z)
# # print(pt3.__dict__)


# ---Функторы---    делает из экземпляра класса функцию. экземпляр можно вызывать как функцию

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         print(self.__counter)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()
# c2 = Counter()
# с2()
# с2()


# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError('Аргумент должен быть строкой')
#
#         return args[0].strip(self.__chars)
#
#
#
# s1 = StripChars("?:!.; ")
# print(s1(" !?Hello World!;. "))
#
# def strip_chars(chars):
#     def wrap(*args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError('Аргумент должен быть строкой')
#
#         return args[0].strip(chars)
#
#     return wrap
#
# s1 = strip_chars("?:!.; ")
# print(s1(" !?Hello World!;. "))

# дз от 12.01.2023
# Создать класс Shape и три дочерних класса: Square, Rectangle, Triangle. Родительский класс должен
# иметь астрактные методы нахождения периметра, площади, рисования фигуры и вывода информации.
# С помощью полиморфизма реализуйте вывод информации о дочерних фигурах.
#
# from abc import ABC, abstractmethod
# from math import sqrt
#
#
# class Shape(ABC):
#     def __init__(self, color):
#         self.color = color
#
#     @abstractmethod
#     def perimetr(self):
#         ...
#
#     @abstractmethod
#     def area(self):
#         ...
#
#     @abstractmethod
#     def print_figure(self):
#         ...
#
#     @abstractmethod
#     def print_info(self):
#         ...
#
#
# class Square(Shape):
#     def __init__(self, side, color):
#         super().__init__(color)
#         self.side = side
#
#     def perimetr(self):
#         return self.side * 4
#
#     def area(self):
#         return self.side ** 2
#
#     def print_figure(self):
#         for i in range(self.side):
#             print('*' * self.side)
#
#     def print_info(self):
#         print('===Квадрат===')
#         print('Сторона:', self.side)
#         print('Цвет:', self.color)
#         print('Площадь:', self.area())
#         print('Периметр', self.perimetr())
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.width = width
#         self.height = height
#
#     def perimetr(self):
#         return (self.width + self.height) * 2
#
#     def area(self):
#         return self.width * self.height
#
#     def print_figure(self):
#         for i in range(self.width):
#             print('*' * self.height)
#
#     def print_info(self):
#         print('===Прямоугольник===')
#         print('Длинна:', self.width)
#         print('Ширина:', self.height)
#         print('Цвет:', self.color)
#         print('Площадь:', self.area())
#         print('Периметр', self.perimetr())
#
#
# class Triangle(Shape):
#     def __init__(self, side1, side2, side3, color):
#         super().__init__(color)
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3
#
#     def perimetr(self):
#         p = self.side1 + self.side2 + self.side3
#         return p
#
#     def area(self):
#         p = (self.side1 + self.side2 + self.side3) / 2
#         return sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))
#
#     def print_figure(self):
#         max_side = max(self.side1, self.side2, self.side3)
#         min_side = min(self.side1, self.side2, self.side3)
#         space_qtn = max_side // 2
#         star_qtn = 1
#         for i in range(min_side):
#             print(' ' * (min_side - i - 1) + '*' * (2 * i + 1)) # метод преподавателя
#             if i > 0:
#                 star_qtn += 2
#                 print(' ' * (space_qtn - i), end='')
#                 print('*' * star_qtn)
#             else:
#                 print(' ' * (space_qtn - i), end='')
#                 print('*' * star_qtn)
#
#
#     def print_info(self):
#         print('===Треугольник===')
#         print('Сторона 1:', self.side1)
#         print('Сторона 2:', self.side2)
#         print('Сторона 3:', self.side3)
#         print('Цвет:', self.color)
#         print('Площадь:', round(self.area(), 2))
#         print('Периметр', self.perimetr())
#
#
# square = Square(3, 'red')
# rectangle = Rectangle(3, 7, 'green')
# triangle = Triangle(11, 6, 6, 'yellow')
#
# fig = [square, rectangle, triangle]
# for k in fig:
#     k.print_info()
#     k.print_figure()
#     print()

# Урок 17.01.2023
# Класс как декоратор

# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, a, b):
#         print('перед вызовом функции')
#         res = self.func(a, b)
#         # print('после вызова функции')
#         return str(res) + '\nпосле вызова функции'

# def MyDecorator(fn):
#     def wrap():
#         print('перед вызовом функции')
#         fn()
#         print('после вызова функции')
#
#     return wrap

# @MyDecorator
# def func(a, b):
#     return a * b
#
# print(func(2, 5))

# class Power:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, a, b):
#         return self.func(a, b) ** 2
#
#
# @Power
# def func(a, b):
#     return a * b
#
# print(func(2, 3))


# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, *args, **kwargs):
#         print('перед вызовом функции')
#         res = self.func(*args, **kwargs)
#         return str(res) + '\nпосле вызова функции'

# @MyDecorator
# def func(a, b):
#     return a * b
#
# @MyDecorator
# def func1(a, b, c):
#     return a * b * c
#
# @MyDecorator
# def func2(a, b, c):
#     return a * b * c

# print(func(2, 5))
# print(func1(2, 5, 2))
# print(func2(2, 5, c=3))


# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, fn):
#         def wrap(a, b):
#             print('перед вызовом функции')
#             print(self.name)
#             fn(a, b)
#             print("после вызова функции")
#
#         return wrap
#
#
# @MyDecorator('test2')
# def func(a, b):
#     print(a * b)
#
#
# func(2, 5)


# ===Декорирование методов===

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print('*' * 20)
#         fn(*args, **kwargs)
#         print('*' * 20)
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f'{self.name} {self.surname}')
#         print(f'{self.name} {self.surname}')
#
#
# p1  = Person("Vitaliy", "Ivanov")
# p1.info()


# +++Дескрипторы+++
# __get__, __set__, __delete__


# class StringD:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = StringD(name)
#         self.surname = StringD(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     self.__nsurame = value
#
#
# p = Person('Ivan', 'Ivanov')
# p.name.set("Igor")
# print(p.name.get(), p.surname.get())


# class ValidateString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f'{self.__name} должно быть строкой')
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidateString()
#     surname = ValidateString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person('Ivan', 'Petrov')
# p.name = 12
# print(p.name)
# print(p.surname)

# ДЗ от 17.01.2023
# Создать класс Power, который будет декорировать функцию. Функция возвращает результат
# умножения двух чисел (a = 2, b = 2), а класс возводит их в степень, которую принимает декоратор.
# Результат: 64
#
#
# class Power:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, fn):
#         def wrap(a, b):
#             fn(a ** self.name, b ** self.name)
#         return wrap
#
#
# @Power(4)
# def func(a, b):
#     print(a * b)
#
#
# func(2, 2)


# --Урок 19.01.2023---

# Создать дескриптор класса Order, который задает имя товара, его цену и количество. В дескрипторе
# должна быть реализована проверка на ввод положительных значений цены и количества товара.
# Тест: Order('apple', 5, 10)

# class NonNegative:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError(f'Значение {self.__name} должно быть положительным')
#         instance.__dict__[self.__name] = value
#
#
# class Order:
#     price = NonNegative()
#     qty = NonNegative()
#
#     def __init__(self, name, price, qty):
#         self.name = name
#         self.price = price
#         self.qty = qty
#
#     def total(self):
#         return self.price * self.qty
#
#
# a = Order('apple', 5, 10)
# print(a.total())
# a.price = 20
# print(a.total())

# Создать дескриптор для класса Point3D (создание точки в трехмерном пространстве) с проверкой на
# ввод координат точки только целочисленных значений
# {'_x': 1, '_y': 2, '_z': 3}

# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise TypeError(f'Координата {coord} должна быть целым числом')
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         instance.__dict__[self.name] = value
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# print(p1.__dict__)
# print(p1.y) # обращаемся к Гетеру (в данном случае 'y' это имя геттера)
# print(p1._y) # обращение к переменной

# Вариант 2

# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise TypeError(f'Координата {coord} должна быть целым числом')
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
#
#     def __delete__(self, instance):
#         # del instance.__dict__[self.name]
#         delattr(instance, self.name)
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# del p1.x
# print(p1.__dict__)
# print(p1.y) # обращаемся к Гетеру (в данном случае 'y' это имя геттера)
# print(p1._y) # обращение к переменной

# другой пример
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# print(getattr(p1, 'x'))
# setattr(p1, 'x', 6)
# print(p1.__dict__)
# print(p1.x)
# print(hasattr(p1, 'z'))

# Дескрипторы бывают двух типов data descriptor и non-data descriptor

# class Integer:
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# print(p1.__dict__)
# print(p1.y) # обращаемся к Гетеру (в данном случае 'y' это имя геттера)


# ===Создание модулей===

# import geometry.rect
# import geometry.trian
# import geometry.sq
# from geometry import rect, trian, sq
# # from geometry import *  # для данной записи необходимо прописать информацию в __init__.py
#
# r1 = rect.Rectangle(1, 2)
# r2 = rect.Rectangle(3, 4)
#
# s1 = sq.Square(10)
# s2 = sq.Square(20)
#
# t1 = trian.Triangle(1, 2, 3)
# t2 = trian.Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimetr())

# ДЗ от 19.01.2023
# Создать класс "Треугольник", свойства - длины трех сторон. Правильность задания свойств должны
# проверяться через дескриптор на ввод положительных целых числовых значений. Предусмотреть в классе
# методы проверки существования треугольника.

# class Integer:
#     @staticmethod
#     def verify_num(side):
#         if not isinstance(side, int):
#             raise TypeError('Значение стороны треугольника должно быть целым числом')
#         elif side < 0:
#             raise ValueError('Значение стороны треугольника должно быть положительным числом')
#
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         self.verify_num(value)
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
#
#
# class Triangle:
#     a = Integer()
#     b = Integer()
#     c = Integer()
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def check_triangle(self):
#         if (self.a + self.b) > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
#             return f'Треугольник со сторонами ({self.a}, {self.b}, {self.c}) существует.'
#         else:
#             return f'Треугольник со сторонами ({self.a}, {self.b}, {self.c}) не существует.'
#
# t1 = Triangle(2, 5, 6)
# t2 = Triangle(5, 2, 8)
# t3 = Triangle(7, 3, 6)
# print(t1.__dict__)
#
# tr_list = [t1, t2, t3]
# for tr in tr_list:
#     print(tr.check_triangle())

# ---Урок 24.01.2023 ---

# from car import electrocar
# import random
#
# def main():
#     e_car = electrocar.ElectroCar('Tesla', 'T', 2020, 50000)
#     e_car.show_car()
#     e_car.description_battery()
#
# if __name__ == '__main__':
#     main()

# ---Упаковка данных---
# Кодирование (сериализация) - запись данных
# Декодирование (десериализация) - извлечение данных

# 1. marshal
# 2. pickle
# 3. json

# Методы у pickle и json есть 4 одинаковые методы.
# dump() - сохраняет данные в файл
# load() - считывание данных из открытого файла

# dumps() - сохраняет данные в строку (в оперативную память) - сериализует
# loads() - считывает данные из строки (из оперативной памяти) - десериализует

# import pickle


# filename = "basket.txt"
#
# shop_list = {
#     "фрукты": ["яблоки", "манго"],
#     "овощи": ["морковь"],
#     "бюджет": 1000
# }
#
# # with open(filename, 'wb') as fn:
# #     pickle.dump(shop_list, fn)
#
# with open(filename, 'rb') as fn:
#     shop = pickle.load(fn)
#
# print(shop)


# class Test:
#     num = 35
#     st = "Привет"
#     lst = [1, 2, 3]
#     d = {'first': 'a', "second": 2}
#     tpl = (22, 33)
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.st}\nСписок: {Test.lst}\n" \
#                f"Словарь: {Test.d}\nКортеж: {Test.tpl}"
#
#
# obj = Test()
#
# my_obj = pickle.dumps(obj)
# print(f'Сериализация в строку: \n{my_obj}\n')
#
# l_obj = pickle.loads(my_obj)
# print(f'Десериализация в строку: \n{l_obj}\n')

# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x * x    # pickle не может обработать вложенные функции
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     # данный метод нужен для сериализации вложенных функций методом pickle (либо других данных,
#     # которые не могут сериализоваться). Данный метод позволяет сохранить данные, которые можно сохранить.
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     # данный метод используется для совмещения десериализованных данных с данными, которые нельзя было сериализовать
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)

# Метод pickle используется только в программах Python.
# JSON метод можно использовать и с другими технологиями.
# import json
#
# data = {
#     'name': 'Игорь',
#     'hobbies': ('running', 'sky diving'),
#     'age': 20,
#     'children': [
#         {
#             'firstname': 'Alice',
#             'age': 5
#         },
#         {
#             'firstname': 'Bob',
#             'age': 8
#         }
#     ]
# }
#
# # with open('data_file.json', 'w') as fw:
# #     json.dump(data, fw, indent=4)   # indent - кол-во пробелов во вложенных элементах
# #
# # with open('data_file.json', 'r') as fr:
# #     data = json.load(fr)
# #     print(data)
#
# json_string = json.dumps(data, ensure_ascii=False) # ensure_ascii преобразовывает русский алфавит из кодировки
# print(json_string)
# data = json.loads(json_string)
# print(data)


# Создать класс (любой). Свойства класса сохранить в JSON объект.
# ДЗ от 24.01.2023
# import json
#
#
# class Test:
#     def __init__(self):
#         self.num = 35
#         self.st = "Привет"
#         self.lst = [1, 2, 3]
#         self.d = {'first': 'a', "second": 2}
#         self.tpl = (22, 33)
#
#     def __str__(self):
#         return f"Число: {self.num}\nСтрока: {self.st}\nСписок: {self.lst}\n" \
#                f"Словарь: {self.d}\nКортеж: {self.tpl}"
#
#
# obj = Test()
#
# my_obj = json.dumps(obj.__dict__)
# print(f'Сериализация в строку: \n{my_obj}\n')
#
# l_obj = json.loads(my_obj)
#
# print(f'Десериализация в строку: \n{l_obj}\n')

# ---Урок 26.01.2023----

# import json
# from random import choice


# def get_person():
#     name = ''
#     tel = ''
#
#     letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letter)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     # print(tel)
#
#     person = {
#         "name": name,
#         "tel": tel
#     }
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(get_person())

# ============================================
# ============================================
# ДЗ от 26.01.2023

# def get_person():
#     name = ''
#     tel = ''
#
#     letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letter)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     # print(tel)
#
#     person = {
#         "name": name,
#         "tel": tel
#     }
#     return person
#
#
# def dict_index():
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     dict_id = ''
#
#     while len(dict_id) != 10:
#         dict_id += choice(nums)
#
#     return dict_id
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = {}
#
#     data[dict_index()] = person_dict
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(get_person())

# ==========================================================
# ==========================================================
# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         # a = ""
#         # for i in self.marks:
#         #     # a += f"{i}, "
#         #     a += str(i) + ", "
#         a = ", ".join(map(str, self.marks))
#         return f"Студент: {self.name}: {a}"  # [:-2]
#
#     def add_marks(self, mark):
#         self.marks.append(mark)
#
#     def del_marks(self, index):
#         self.marks.pop(index)
#
#     def edit_marks(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_marks(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     @staticmethod
#     def dump_to_json(stud, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = []
#
#         data.append({"name": stud.name, "marks": stud.marks})
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def load_from_file(filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         # a = ''
#         # for i in self.students:
#         #     a += str(i) + '\n'
#         a = '\n'.join(map(str, self.students))
#         return f'Группа: {self.group}\n{a}'
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def del_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(group1, group2, index):
#         return group2.add_student(group1.del_student(index))
#
#     @staticmethod
#     def dump_group(file, group):
#         try:
#             data = json.load(open(file))
#         except FileNotFoundError:
#             data = []
#
#         with open(file, 'w') as f:
#             stud_list = []
#             for i in group.students:
#                 stud_list.append([i.name, i.marks])
#             data.append(stud_list)
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def load_journal(file):
#         with open(file, 'r') as f:
#             print(json.load(f))
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# # print(st1)
# # st1.add_marks(2)
# # print(st1)
# # st1.del_marks(2)
# # print(st1)
# # st1.edit_marks(-1, 5)
# # Student.dump_to_json(st1, 'student.json')
# # Student.load_from_file('Student.json')
# # print(st1)
# # print(st1.average_marks())
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# # Student.dump_to_json(st2, 'student.json')
# # Student.load_from_file('Student.json')
# st3 = Student('Birukov', [2, 3, 5, 4, 2, 5])
# # Student.dump_to_json(st3, 'student.json')
# # Student.load_from_file('Student.json')
# sts = [st1, st2]
# my_group = Group(sts, 'ГК Python')
# # # print(my_group)
# # # print()
# # my_group.add_student(st3)
# # # print(my_group)
# # # print()
# # my_group.del_student(1)
# # print(my_group)
# # print()
# group22 = [st3]
# my_group2 = Group(group22, 'ГК Web')
# Group.dump_group('group.json', my_group)
# Group.dump_group('group.json', my_group2)
# Group.load_journal('group.json')
# # print(my_group2)
# # print()
# # Group.change_group(my_group, my_group2, 0)
# # print(my_group)
# # print()
# # print(my_group2)

# ==============================
# Урок от 31.01.2023

# СОЗДАНИЕ МОДУЛЕЙ

# import requests
# import json
#
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# todos = json.loads(response.text)
#
# # print(todos[:10])
# # print(type(todos))
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
#
# print(todos_by_user)
#
# # сортировка словаря по значению
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# # print(users)
# max_users = ' and '.join(users)
#
# s = "s" if len(users) > 1 else ""
# print(f"user{s} {max_users} completed {max_complete} TODOs")
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count = str(todo['userId']) in users
#     return is_complete and has_max_count    # возвращает True если если оба элемента равны True
#
#
# with open('filtered_data_file.json', 'w') as f:
#     # Записываем данные в файл если функция 'filter' возвращает значение True
#     filtered_todos = list(filter(keep, todos))
#     json.dump(filtered_todos, f, indent=2)
#
# with open('filtered_data_file.json', 'r') as f:
#     data = json.load(f)
#     print(data)

# ===============================================================
# ДЗ от 31.01.2023
# Есть некоторый словарь, который хранит название стран и столиц.
# Название стран используется в качестве ключа, название столицы в качестве значения.
# Необходимо реализовать: добавление, удаление, поиск, редактирование и просмотр данных
# (используя упаковку и распаковку данных)
#
# import json
#
#
# class Country:
#
#     @staticmethod
#     def add_data(country, capital):
#         try:
#             country_dict = json.load(open('country.json'))
#         except FileNotFoundError:
#             country_dict = {}
#
#         country_dict[country] = capital
#         with open('country.json', 'w', encoding='utf-8') as f:
#             json.dump(country_dict, f, indent=2)
#
#     @staticmethod
#     def remove_data(country):
#         country_dict = json.load(open('country.json'))
#         del country_dict[country]
#
#         with open('country.json', 'w') as f:
#             json.dump(country_dict, f, indent=2)
#
#     @staticmethod
#     def search_data(country):
#         country_dict = json.load(open('country.json'))
#         print(f'{country}: {country_dict[country]}')
#
#     @staticmethod
#     def edit_data(country, capital):
#         country_dict = json.load(open('country.json'))
#         country_dict[country] = capital
#         with open('country.json', 'w', encoding='utf-8') as f:
#             json.dump(country_dict, f, indent=2)
#
#     @staticmethod
#     def prev_data():
#         country_dict = json.load(open('country.json'))
#         print(country_dict)
#
#
# print('*' * 50)
# i = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n"
#           "3 - поиск данных\n4 - редактирование данных\n"
#           "5 - просмотр данных\n6 - завершение работы\nВвод: ")
#
# while i != '6':
#     c1 = Country()
#     if i == '1':
#         country = input("Введите название страны (с заглавной буквы): ")
#         capital = input("Введите название столицы (с заглавной буквы): ")
#
#         c1.add_data(country, capital)
#         print("Файл сохранен")
#         print('*' * 50)
#         i = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
#                   "4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\nВвод: ")
#
#     elif i == '2':
#         country = input("Введите название страны, которую хотите удалить (с заглавной буквы): ")
#         c1.remove_data(country)
#         print("Данные удалены")
#         print("Файл сохранен")
#         print('*' * 50)
#         i = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
#                   "4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\nВвод: ")
#
#     elif i == '3':
#         country = input("Введите название страны, которую хотите найти (с заглавной буквы): ")
#         c1.search_data(country)
#         print('*' * 50)
#         i = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
#                   "4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\nВвод: ")
#
#     elif i == '4':
#         country = input("Введите название страны, которую хотите изменить (с заглавной буквы): ")
#         capital = input("Введите название нового города (с заглавной буквы): ")
#         c1.edit_data(country, capital)
#         print("Файл изменен")
#         print('*' * 50)
#         i = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
#                   "4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\nВвод: ")
#
#     elif i == '5':
#         c1.prev_data()
#         print('*' * 50)
#         i = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
#                   "4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\nВвод: ")
#
#     else:
#         print('Вводите пожалуйста только цифры от 1 до 6')
#         print('*' * 50)
#         i = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
#                   "4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\nВвод: ")
#
# print('До скорых встреч.')


#   ===============================================
# Урок от 02.02.2023

# csv (Comma Separated Values) - переменные, разделенные запятыми.

# import csv

# with open('data.csv', 'r') as r_file:   # если не указывать второй параметр, то файл откроется в режиме чтения
#     file_reader = csv.reader(r_file, delimiter=";")   # работа со списком в режиме чтения
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"    {row[0]} - {row[1]}. Родился в {row[2]} году.")
#         count += 1
#
#     print(f"Всего в файле {count} строки.")

# with open('data1.csv', 'r') as r_file:   # если не указывать второй параметр, то файл откроется в режиме чтения
# #     f_names = ["Имя", "Профессия", "Год рождения"]
# #     # параметр fieldnames задает название полей в ручном режиме, если этой инфы нет в файле
# #     file_reader = csv.DictReader(r_file, delimiter=";", fieldnames=f_names) # работа со словарем в режиме чтения
# #     count = 0
# #     for row in file_reader:
# #         if count == 0:
# #             print(f"Файл содержит столбцы: {', '.join(row)}")
# #         print(f"    {row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году.")
# #         count += 1
# #
# #     print(f"Всего в файле {count} строки.")

# with open('student.csv', mode='w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator="\r")    # метод для записи
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", "5", "12"])
#     writer.writerow(["Маша", "11", "17"])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('data_sw.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#
# with open('data_sw.csv', 'r') as f:
#     print(f.read())


# Запись данных в файл при помощи словаря
# with open('stud.csv', 'w') as f:
#     names = ["Имя", "Возраст"]
#     file_writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=names)
#     file_writer.writeheader()   # запись заголовочной строки
#     file_writer.writerow({"Имя": "Саша", "Возраст": "6"})
#     file_writer.writerow({"Имя": "Маша", "Возраст": "15"})
#     file_writer.writerow({"Имя": "Вова", "Возраст": "14"})

# import csv
#
# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open("dictwriter.csv", 'w') as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator='\r', fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)

# ==============================
# Парсинг

# from bs4 import BeautifulSoup
#
#
# def get_copywriter(tag):
#     whois = tag.find("div", class_="whois").text.strip()
#     if "Copywriter" in whois:
#         return tag
#     return None
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, "html.parser")
# copywriter = []
# row = soup.find_all('div', class_='row')
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)

# row = soup.find('div', class_='name').text
# row = soup.find_all("div", class_='name')
# for d in row:
#     print(d.text)
# print(row)

# row = soup.find_all('div', class_='row')[1].find('div', class_='links') # по индексу можно найти один элемент
# print(row)

# row = soup.find_all("div", {"data-set": "salary"})  # пользовательские данные с сайта указываются в виде словаря
# print(row)

# row = soup.find("div", string='Alena').find_parent(class_='row')   # поиск по тексту
# print(row)

# row = soup.find("div", id="whois3").find_next_sibling() # следующий элемент на одном уровне
# print(row)
# row = soup.find("div", id="whois3").find_previous_sibling() # предыдущий элемент на одном уровне
# print(row)

# =============

# import re
# from bs4 import BeautifulSoup
#
#
# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.search(pattern, s).group()   # group() - возвращает объект совпадения (match)
#     res = re.findall(pattern, s)[0]
#     print(res)
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, "html.parser")
#
# salary = soup.find_all("div", {"data-set": "salary"})
# for i in salary:
#     get_salary(i.text)
#
# =========================================
# ДЗ от 02.02.2023

# Считать данные из файла data2.csv

# import csv
#
#
# with open("data2.csv", "r") as f:
#     file_reader = csv.reader(f, delimiter=";")
#     for i in file_reader:
#         print(i)

#==========================================
# Урок 07.02.2023
# import csv
#
# import requests
# from bs4 import BeautifulSoup
# import re

# r = requests.get("https://ru.wordpress.org")
# print(r.headers)
# print(r.headers['content-Type'])
# print(r.content)  # Возвращает содержимое страницы в бинарном виде
# print(r.text)   # возвращает содержимое страницы в обычном виде


# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml") # lxml - парсер, рекомендуется использовать разработчиками
#     p1 = soup.find("header", id="masthead").find("p", class_="site-title").text
#     return p1
#
#
# def main():
#     url = "https://ru.wordpress.org"
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()

# ==========================
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     res = re.sub(r"\D+", "", s)
#     return res
#
#
# def write_csv(data):
#     with open("plugins.csv", "a") as f:
#         writer = csv.writer(f, lineterminator="\r", delimiter=";")
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml") # lxml - парсер, рекомендуется использовать разработчиками
#     p1 = soup.find_all("section", class_="plugin-section")[3]
#     plugins = p1.find_all("article")
#
#     for plugin in plugins:
#         name = plugin.find("h3").text
# #       url = plugin.find("h3").find("a")["href"] # выводим ссылку, обращаясь к атрибуту.
#         url = plugin.find("h3").find("a").get("href") # выдает также верхний результат
#         rating = plugin.find("span", class_="rating-count").find('a').text
#         r = refined(rating)
#         data = {'name': name, "url": url, "rating": r}
#         write_csv(data)
#     # return len(plugins)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# ===============================
# import csv
#
# import requests
# from bs4 import BeautifulSoup
# import re
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refine_cy(c):
#     return c.split()[-1]
#
#
# def refine_snippet(s):
#     return re.sub(r"[🐰✅]", "", s)
#
#
# def write_csv(data):
#     with open("plugins1.csv", "a") as f:
#         writer = csv.writer(f, lineterminator="\r", delimiter=";")
#         writer.writerow((data['name'], data['url'], data['snippet'], data['cy']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml") # lxml - парсер, рекомендуется использовать разработчиками
#     elements = soup.find_all("article", class_="plugin-card")
#     for el in elements:
#         try:
#             name = el.find("h3").text
#         except ValueError:
#             name = ""
#
#         try:
#             url = el.find("h3").find("a").get("href")
#         except ValueError:
#             url = ""
#
#
#         try:
#             snippet = el.find("div", class_="entry-excerpt").text.strip()
#             snippet1 = refine_snippet(snippet)
#         except ValueError:
#             snippet1 = ""
#         # print(snippet1)
#
#
#         try:
#             c = el.find("span", class_="tested-with").text.strip()
#             cy = refine_cy(c)
#         except ValueError:
#             cy = ""
#
#
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet1,
#             'cy': cy
#         }
#
#         write_csv(data)
#
#
# def main():
#     for i in range(12, 13):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# =================================
# дз от 07.02.2023
# Реализовать парсинг данных из любого интернет ресурса с однотипными данными и сохранить их в формат csv

# import csv
# import re
# import requests
# from bs4 import BeautifulSoup
#
#
# def refined(d):
#     res = re.sub(r"\D+", "", d)
#     return res
#
#
# def refined_snippet(s):
#     return re.sub(r"[\xd7\xf8\xd8\u2033]", "", s)
#
#
# def write_csv(data):
#     with open("caminfo.csv", "a") as f:
#         writer = csv.writer(f, lineterminator="\r", delimiter=";")
#         writer.writerow((data['name'], data['url'], data['cod'], data['prev_text'], data["price"]))
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     s = BeautifulSoup(html, "lxml")
#     items = s.find_all("div", class_="list_item_wrapp item_wrap item")
#
#     for item in items:
#         try:
#             name = item.find("div", class_="item-title").text.strip()
#         except ValueError:
#             name = ""
#
#         try:
#             url = item.find("div", class_="item-title").find("a")["href"]
#             url = "https://sv22.ru" + url
#         except ValueError:
#             url = ""
#
#         try:
#             cod = item.find("div", class_="item-stock").text.strip()
#             cod_ref = refined(cod)
#         except ValueError:
#             cod_ref = ""
#
#         try:
#             prev_text = item.find("div", class_="preview_text").text.strip()
#             prev_text_ref = refined_snippet(prev_text)
#         except ValueError:
#             prev_text_ref = ""
#
#         try:
#             price = item.find("div", class_="price").text.strip()
#             price_ref = refined(price)
#         except ValueError:
#             price_ref = ""
#
#         data = {
#                 "name": name,
#                 "url": url,
#                 "cod": cod_ref,
#                 "prev_text": prev_text_ref,
#                 "price": price_ref
#                 }
#         write_csv(data)
#
#
# def main():
#     url = "https://sv22.ru/catalog/323/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# =========================
# Урок 09.02.2023

# from parsers import Parsers
#
# def main():
#     pars = Parsers("https://www.ixbt.com/live/index/news", "new.txt")
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()

# ===============================
# MVC - Model Controller View
# Model -
# View -
# Controller - Связующее звено между моделью и видом

# создадим папку articles:
#       project_articles.py
#       controller.py
#       view.py
#       model.py

# ===============================
# урок 14.02.2023
# ======== БАЗА ДАННЫХ ==========
# Реляционная модель данных используется чаще всего

# Столбцы (поля, атрибуты)
# Строки (записи, кортежи)
# SQLite
# *.db, *.db3, *.sqlite, *.sqlite3 - расширения файлов SQLite


# import sqlite3

# con = sqlite3.connect('profile.db') # Обязательный метод, для соединения
# cur = con.cursor()  # Обязательный метод.
#
# cur.execute("""
# """)
#
# con.close() # Обязательный метод для закрытия соединения

# нижний код аналогичен вышеуказаному
# with sqlite3.connect('profile.db') as con:
#     cur = con.cursor()
    # cur.execute("""CREATE TABLE IF NOT EXISTS users(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # summa REAL,
    # data BLOB
    # )""")
    # cur.execute("DROP TABLE users")

# ================================
# Lesson 16.02.2023

import sqlite3

with sqlite3.connect('users.db') as con:
    cur = con.cursor()


    # cur.execute("""
    #     DROP TABLE person_table
    #     """)

    # cur.execute("""
    #     ALTER TABLE person_table
    #     DROP COLUMN home_address
    #     """)

    # cur.execute("""
    #     ALTER TABLE person_table
    #     RENAME COLUMN address TO home_address;
    #     """)

    # cur.execute("""
    #     ALTER TABLE person_table
    #     ADD COLUMN address TEXT NOT NULL DEFAULT "street"
    #     """)

    # cur.execute("""
    # ALTER TABLE person
    # RENAME TO person_table;
    # """)

    # cur.execute("""
    # CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT '+79090000000',
    # age INTEGER NOT NULL CHECK(age>15 AND age<70),
    # email TEXT UNIQUE
    # )""")


