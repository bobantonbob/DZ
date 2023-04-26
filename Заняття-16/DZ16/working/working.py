shtat = {}

def add_new_worker():
    name = input("ВВедіть ПІБ нового працівника: ")
    file = {}
    shtat[name] = file
    nomer = input("ВВедить номер телефону працівника")
    company = input("ВВедить місце роботи працівника")
    payments = input("ВВедить заробітну плату працівника")
    file['Номер'] = nomer
    file['компанія'] = company
    file['Виплати'] = payments
    print(f"Співробітник {name} має номер телефону {shtat[name]['Номер']} та працює у компанії "
          f"{shtat[name]['компанія']}, його заробітна платня становить {shtat[name]['Виплати']} грн..")


def search_worker():
    name = input("ВВедіть ПІБ штатного працівника : ")
    if name in shtat:
        print(
            f"Співробітник {name} має № телефону {shtat[name]['Номер']} працює у компанії {shtat[name]['Виплати']}, його заробітна полатня становить {shtat[name]['Виплати']} грн..")
    else:
        print("Такого працівника в штаті немає ")


def delete_worker():
    name = input("Якого штатного працівника треба видалити? ")
    if name in shtat:
        del shtat[name]
        print(f' Штатний працівник {name} видалений ')
    else:
        print(f" Працівник {name} не знайдений :(")


def replace_telephone_worker():
    name = input("ВВедіть працівника якому потрібно змінити номер телефону : ")
    if name in shtat:
        nomer = input("ВВедить новий номер телефону працівника")
        shtat[name]['Номер'] = nomer
        print(f'Номер телефону працівника {name} змінено на {nomer}')
    else:
        print(f" Працівник {name} не знайдений :(")


def replace_company_worker():
    name = input("ВВедіть працівника якому потрібно змінити місце роботи : ")
    if name in shtat:
        company = input("ВВедить новий емаіл працівника")
        shtat[name]['компанія'] = company
        print(f'Місце роботи працівника {name} змінено на {company}')
    else:
        print(f" Працівник {name} не знайдений :(")


def replace_payments_worker():
    name = input("ВВедіть працівника якому потрібно змінити заробітну платню : ")
    if name in shtat:
        payments = input("ВВедить новий оклад працівника")
        shtat[name]['Виплати'] = payments
        print(f'Оклад працівника {name} змінено на {payments} грн..')
    else:
        print(f" Працівник {name} не знайдений :(")



def menu():
    print("Оберіть один з пунктів: ")
    print("1. ПІБ нового працівника ")
    print("2. Знайти штатного працівника ")
    print("3. Видалити штатного працівника ")
    print("4. Змінити номер телефону працівника ")
    print("5. Змінити місце роботи працівника ")
    print("6. Змінити заробітну плату працівника ")
    print('7. Вихід ')
    for key, value in shtat.items():
        print(f"{key}: {value} ")
    menu()
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
        exit()
    if nomber not in range(1, 8):
        print("Невірний вибір. Смерть ворогам")