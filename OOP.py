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

class Table:
    def __init__(self, width=None, length=None, radius=None):
        if length is None:
            self._width = width
            self._length = self._width
        else:
            self._width = width
            self._length = length
        self._radius = radius

    def area_rect_table(self):
        raise NotImplementedError("В дочернем классе должен быт определен метод area_rect_table()")

    def area_circle_table(self):
        raise NotImplementedError("В дочернем классе должен быт определен метод area_circle_table()")


class RectTable(Table):
    def area_rect_table(self):
        return self._width * self._length
    pass


class CircleTable(Table):
    def area_circle_table(self):
        return round(3.14141414 * (self._radius ** 2), 2)
    pass

table1 = RectTable(20, 10)
print(table1.__dict__)
print(table1.area_rect_table())
table2 = RectTable(20)
print((table2.__dict__))
print(table2.area_rect_table())
table3 = CircleTable(radius=20)
print(table3.__dict__)
print(table3.area_circle_table())


