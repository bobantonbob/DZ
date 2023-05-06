from working.utils import *


print(shtat)
print(companies)


while True:
    menu()
    try:
        nomber = int(input("Ваш вибір: "))
        if nomber == 1: menu_worker()
        if nomber == 2: menu_companies()
        if nomber == 3: exit()
        if nomber not in range(1, 4):
            print("\033[31m Невірний вибір. Смерть ворогам \033[0m ")
    except ValueError:
        print("\033[31m Тілки ЦИФРА \033[0m ")


