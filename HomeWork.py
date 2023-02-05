# Есть некоторый словарь, который хранит название стран и столиц.
# Название стран используется в качестве ключа, название столицы в качестве значения.
# Необходимо реализовать: добавление, удаление, поиск, редактирование и просмотр данных
# (используя упаковку и распаковку данных)


import json


class Country:

    @staticmethod
    def add_data(country, capital):
        try:
            country_dict = json.load(open('country.json'))
        except FileNotFoundError:
            country_dict = {}

        country_dict[country] = capital
        with open('country.json', 'w', encoding='utf-8') as f:
            json.dump(country_dict, f, indent=2)

    @staticmethod
    def remove_data(country):
        country_dict = json.load(open('country.json'))
        del country_dict[country]

        with open('country.json', 'w') as f:
            json.dump(country_dict, f, indent=2)

    @staticmethod
    def search_data(country):
        country_dict = json.load(open('country.json'))
        print(f'{country}: {country_dict[country]}')

    @staticmethod
    def edit_data(country, capital):
        country_dict = json.load(open('country.json'))
        country_dict[country] = capital
        with open('country.json', 'w', encoding='utf-8') as f:
            json.dump(country_dict, f, indent=2)

    @staticmethod
    def prev_data():
        country_dict = json.load(open('country.json'))
        print(country_dict)


print('*' * 50)
i = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n"
          "3 - поиск данных\n4 - редактирование данных\n"
          "5 - просмотр данных\n6 - завершение работы\nВвод: ")

while i != '6':
    c1 = Country()
    if i == '1':
        country = input("Введите название страны (с заглавной буквы): ")
        capital = input("Введите название столицы (с заглавной буквы): ")

        c1.add_data(country, capital)
        print("Файл сохранен")
        print('*' * 50)
        i = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
                  "4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\nВвод: ")

    elif i == '2':
        country = input("Введите название страны, которую хотите удалить (с заглавной буквы): ")
        c1.remove_data(country)
        print("Данные удалены")
        print("Файл сохранен")
        print('*' * 50)
        i = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
                  "4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\nВвод: ")

    elif i == '3':
        country = input("Введите название страны, которую хотите найти (с заглавной буквы): ")
        c1.search_data(country)
        print('*' * 50)
        i = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
                  "4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\nВвод: ")

    elif i == '4':
        country = input("Введите название страны, которую хотите изменить (с заглавной буквы): ")
        capital = input("Введите название нового города (с заглавной буквы): ")
        c1.edit_data(country, capital)
        print("Файл изменен")
        print('*' * 50)
        i = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
                  "4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\nВвод: ")

    elif i == '5':
        c1.prev_data()
        print('*' * 50)
        i = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
                  "4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\nВвод: ")

    else:
        print('Вводите пожалуйста только цифры от 1 до 6')
        print('*' * 50)
        i = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
                  "4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\nВвод: ")

print('До скорых встреч.')

