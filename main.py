import datetime

from Logic.CRUD import create
from Tests.testAll import runAllTests
from UI.console2 import run_console
from UI.console import run_ui


def show_optiuni():
    print('1. Interfata cu comenzi. ')
    print('2. Interfata cu optiuni. ')
    print('x. Iesire. ')


def main():
    cheltuieli = []
    undo_list = []
    redo_list = []
    cheltuieli = create(cheltuieli, 101, 1, 239.42, datetime.date(2021, 10, 28), 'gaz', undo_list, redo_list)
    cheltuieli = create(cheltuieli, 109, 2, 450, datetime.date(2021, 3, 13), 'intretinere', undo_list, redo_list)
    cheltuieli = create(cheltuieli, 111, 3, 44, datetime.date(2021, 11, 9), 'alte cheltuieli', undo_list, redo_list)
    while True:
        show_optiuni()
        optiune = input('Alegeti interfata pe care doriti sa o utilizati: ')
        if optiune == '1':
            run_console(cheltuieli)
        elif optiune == '2':
            run_ui(cheltuieli, undo_list, redo_list)
        elif optiune == 'x':
            break
        else:
            print('Optiune gresita, incercati din nou! ')


if __name__ == '__main__':
    runAllTests()
    main()
