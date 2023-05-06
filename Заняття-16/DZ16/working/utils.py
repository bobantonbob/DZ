from .worker import *
from .companies import *


def menu_worker():
    print("Оберіть один з пунктів: ")
    print("1. ПІБ нового працівника ")
    print("2. Знайти штатного працівника ")
    print("3. Видалити штатного працівника ")
    print("4. Змінити номер телефону працівника ")
    print("5. Змінити місце роботи працівника ")
    print("6. Змінити заробітну плату працівника ")
    print('\033[31m7. Вихід \033[0m ')
    for key, value in shtat.items():
        print(f"{key}: {value} ")

    nomber = int(input("Ваш вибір: "))
    if nomber == 1:
        add_new_worker()
    if nomber == 2:
        search_worker()
    if nomber == 3:
        delete_worker()
    if nomber == 4:
        replace_telephone_worker()
    if nomber == 5:
        replace_company_worker()
    if nomber == 6:
        replace_payments_worker()
    if nomber == 7:
        menu()
    if nomber not in range(1, 8):
        print("Невірний вибір. Смерть ворогам")

def menu_companies():
    print("Оберіть один з пунктів: ")
    print("1. ВВедіть назву нової компанії ")
    print("2. Пощук компанії ")
    print("3. Видалити компанію ")
    print("4. В якої компанії треба змінити штат ")
    print("5. В якої компанії треба змінити річний бюджет ")
    print('\033[31m6. Вихід \033[0m ')
    for key, value in companies.items():
        print(f"{key}: {value} ")

    nomber = int(input("Ваш вибір: "))
    if nomber == 1:
        add_new_company()
    if nomber == 2:
        search_company()
    if nomber == 3:
        delete_company()
    if nomber == 4:
        replace_numberworkers_company()
    if nomber == 5:
        replace_annualbudget_company()
    if nomber == 6:
        menu()
    if nomber not in range(1, 7):
        print("Невірний вибір. Смерть ворогам")


def menu():
    print("Оберіть один з двох пунктів ")
    print("\033[34m1. Якщо вас цікавить інформація стосовно працівника \033[0m ")
    print("\033[34m2. Якщо вас цікавить інформація стосовно компанії \033[0m ")
    print('\033[31m3. Вихід \033[0m ')
    for key, value in shtat.items():
        print(f"{key}: {value} ")
    for key, value in companies.items():
        print(f"{key}: {value} ")
