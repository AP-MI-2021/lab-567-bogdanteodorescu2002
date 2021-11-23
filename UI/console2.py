import datetime

from Domain.cheltuiala import get_str
from Logic.CRUD import delete, create, update, read_by_nr_apartament
from Logic.funct1 import delete_all_costs_for_apartement
from Logic.funct3 import the_biggest_expense_for_every_type


def read_data(data_str):
    try:
        data = data_str.split('-')
        year = int(data[0])
        month = int(data[1])
        day = int(data[2])
        return datetime.date(year, month, day)
    except ValueError as ve:
        print(f'Eroare: {ve}')
        return None


def run_console(lst_cheltuieli):
    while True:
        print()
        run_command = input('Dati comanda: trebuie separate prin ";", elemntele prin ",",'
                            ' in timp ce data trebuie scrisa sub forma:"year-month-day". ')
        run_command = run_command.split(';')
        if run_command[0] == 'exit':
            break
        for command in run_command:
            command = command.split(',')
            if command[0] == 'add':
                if len(command) == 6:
                    try:
                        id_cheltuiala = command[1]
                        nr_apartament = int(command[2])
                        suma = float(command[3])
                        data = read_data(command[4])
                        if data is None:
                            raise ValueError('Nu ati introdus corect data! ')
                        tipul = command[5]
                        lst_cheltuieli = create(lst_cheltuieli, id_cheltuiala, nr_apartament, suma, data, tipul, [], [])
                    except ValueError as ve:
                        print(f'Eroare: {ve}')
                else:
                    print('Nu ati introdus numarul corect de parametrii ai cheltuielii.')
            elif command[0] == 'showall':
                for cheltuiala in lst_cheltuieli:
                    print(get_str(cheltuiala))
            elif command[0] == 'delete':
                if len(command) == 2:
                    id_cheltuiala = command[1]
                    lst_cheltuieli = delete(lst_cheltuieli, id_cheltuiala, [], [])
                else:
                    print('Nu ati introdus numarul cirect de parametri pentru stergere!')
            elif command[0] == 'read by nr apartment':
                if len(command) == 2:
                    try:
                        nr_apartament = command[1]
                        lst_cheltuieli = read_by_nr_apartament(lst_cheltuieli, nr_apartament)
                    except ValueError as ve:
                        print(f'Eroare: {ve}')
                else:
                    print('Nu ati introdus numarul corect de parametrii ai cheltuielii.')
            elif command[0] == 'update':
                if len(command) == 6:
                    try:
                        id_cheltuiala = command[1]
                        nr_apartament = command[2]
                        suma = command[3]
                        data = command[4]
                        if data is None:
                            raise ValueError('Nu ati introdus corect data! ')
                        tipul = command[5]
                        lst_cheltuieli = update(lst_cheltuieli, id_cheltuiala, nr_apartament, suma, data, tipul, [], [])
                    except ValueError as ve:
                        print(f'Eroare: {ve}')
                else:
                    print('Nu ati introdus numarul corect de parametrii ai cheltuielii.')
            elif command[0] == 'delete all costs':
                if len(command) == 2:
                    try:
                        nr_apartament = command[1]
                        lst_cheltuieli = delete_all_costs_for_apartement(lst_cheltuieli, nr_apartament, [], [])
                    except ValueError as ve:
                        print(f'Eroare: {ve}')
                else:
                    print('Nu ati introdus numarul corect de parametrii ai cheltuielii.')
            elif command[0] == 'biggest expense':
                if len(command) == 1:
                    try:
                        lst_cheltuieli = the_biggest_expense_for_every_type(lst_cheltuieli)
                        print(lst_cheltuieli)
                    except ValueError as ve:
                        print(f'Eroare: {ve}')
            else:
                print('Comanda incorecta, incercati din nou!')
