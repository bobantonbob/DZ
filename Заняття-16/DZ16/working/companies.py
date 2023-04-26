companies = {}


def add_new_company():
    company = input("ВВедіть назву нової компанії : ")
    file = {}
    companies[company] = file
    number_workers = int(input("ВВедить кідькість працівників "))
    annual_budget = int(input("ВВедить річний бютжет компанії "))
    file['Кіл_Працівників'] = number_workers
    file['Річний_бюджет'] = annual_budget
    print(f"Компанія {company} має  {companies[company]['Кіл_Працівників']} працівнаків, та річний бютжет її склодає  "
          f"{companies[company]['Річний_бюджет']}")


def search_company():
    company = input("ВВедіть для пошуку назву компанії : ")
    if company in companies:
        print(
            f"Компанія {company} має в штаті {companies[company]['Кіл_Працівників']} працівникків, та річтий бютжет складає {companies[company]['Річний_бюджет']} грн..")
    else:
        print("Такої компанії немає в базі ")


def delete_company():
    company = input("Яку компанію треба видалити ? ")
    if company in companies:
        del companies[company]
        print(f' Компанія {company} видалена з бази ')
    else:
        print(f" Компанія {company} не знайдена в базі :(")


def replace_numberworkers_company():
    company = input("ВВедіть назву компанії, для зміни кількості штату ")
    if company in companies:
        number_workers = int(input("ВВедить кількість нового штату "))
        companies[company]['Кіл_Працівників'] = number_workers
        print(f'В компанії {company} змінено штат на  {number_workers} людей ')
    else:
        print(f" Компанія {company} не знайдена в базі :(")


def replace_annualbudget_company():
    company = input("ВВедіть назву компанії, для зміни річного бюджету ")
    if company in companies:
        annual_budget = int(input("ВВедіть новий річний бюджет "))
        companies[company]['Річний_бюджет'] = annual_budget
        print(f'В компанії {company} змінено річний бюджет на  {annual_budget} грн..')
    else:
        print(f" Компанія {company} не знайдена в базі :(")


