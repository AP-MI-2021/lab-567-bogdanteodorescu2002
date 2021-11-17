import datetime

from Domain.cheltuiala import get_suma
from Logic.CRUD import create, read, read_by_nr_apartament
from Logic.funct1 import delete_all_costs_for_apartement
from Logic.funct2 import add_sum_to_all_expense_by_date
from Logic.funct6 import do_undo, do_redo

def test_undo_redo():
    # 1 lista initiala goala
    lst_cheltuieli = []
    undo_list = []
    redo_list = []
    assert len(lst_cheltuieli) == 0

    # 2 adaugam un obiect
    lst_cheltuieli = create(lst_cheltuieli, 101, 1, 239, datetime.date(2019, 10, 9), 'canal', undo_list, redo_list)

    # 3 adaugam inca un obiect
    lst_cheltuieli = create(lst_cheltuieli, 102, 2, 456, datetime.date(2021, 3, 24), 'alte cheltuieli', undo_list, redo_list)

    # 4 adaugam inca un obiect
    lst_cheltuieli = create(lst_cheltuieli, 103, 3, 800, datetime.date(2020, 9, 11), 'intretinere', undo_list, redo_list)
    assert len(lst_cheltuieli) == 3

    # 5 undo scoate ultimul obiect
    if len(undo_list) > 0:
        lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 2
    assert read(lst_cheltuieli, 101) is not None
    assert read(lst_cheltuieli, 102) is not None
    assert read(lst_cheltuieli, 103) is None

    # 6 inca un undo scoate penultimul obiect adaugat
    if len(undo_list) > 0:
        lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 1
    assert read(lst_cheltuieli, 101) is not None
    assert read(lst_cheltuieli, 102) is None
    assert read(lst_cheltuieli, 103) is None

    # 7 inca un undo si primul element adaugat
    if len(undo_list) > 0:
        lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 0
    assert read(lst_cheltuieli, 101) is None
    assert read(lst_cheltuieli, 102) is None
    assert read(lst_cheltuieli, 103) is None

    # 8 inca un undo si nu face nimic
    if len(undo_list) > 0:
        lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert read(lst_cheltuieli, 101) is None
    assert read(lst_cheltuieli, 102) is None
    assert read(lst_cheltuieli, 103) is None

    # 9 adaugam trei obiecte
    lst_cheltuieli = create(lst_cheltuieli, 104, 4, 111, datetime.date(2020, 9, 23), 'alte cheltuieli', undo_list, redo_list)
    lst_cheltuieli = create(lst_cheltuieli, 105, 5, 22, datetime.date(2021, 10, 7), 'alte cheltuieli', undo_list, redo_list)
    lst_cheltuieli = create(lst_cheltuieli, 106, 6, 247, datetime.date(2021, 8, 12), 'intretinere', undo_list, redo_list)
    assert len(lst_cheltuieli) == 3
    assert read(lst_cheltuieli, 104) is not None
    assert read(lst_cheltuieli, 105) is not None
    assert read(lst_cheltuieli, 106) is not None

    # 10 redo nu face nimic
    if len(redo_list) > 0:
        lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 3
    assert read(lst_cheltuieli, 104) is not None
    assert read(lst_cheltuieli, 105) is not None
    assert read(lst_cheltuieli, 106) is not None

    # 11 doua undo-uri scot ultimele 2 obiecte
    if len(undo_list) > 0:
        lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    if len(undo_list) > 0:
        lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 1
    assert read(lst_cheltuieli, 104) is not None
    assert read(lst_cheltuieli, 105) is None
    assert read(lst_cheltuieli, 106) is None

    # 12 redo anuleaza ultimul redo, daca ultima operatie e undo
    if len(redo_list) > 0:
        lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 2
    assert read(lst_cheltuieli, 104) is not None
    assert read(lst_cheltuieli, 105) is not None
    assert read(lst_cheltuieli, 106) is None

    # 13 redo anuleaza si primul undo
    if len(redo_list) > 0:
        lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 3
    assert read(lst_cheltuieli, 104) is not None
    assert read(lst_cheltuieli, 105) is not None
    assert read(lst_cheltuieli, 106) is not None

    # 14 doua undo-uri scot ultimele 2 obiecte
    if len(undo_list) > 0:
        lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    if len(undo_list) > 0:
        lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 1
    assert read(lst_cheltuieli, 104) is not None
    assert read(lst_cheltuieli, 105) is None
    assert read(lst_cheltuieli, 106) is None

    # 15 adaugam un obiect
    lst_cheltuieli = create(lst_cheltuieli, 107, 9, 25, datetime.date(2021, 7, 14), 'canal', undo_list, redo_list)
    assert len(lst_cheltuieli) == 2
    assert read(lst_cheltuieli, 104) is not None
    assert read(lst_cheltuieli, 105) is None
    assert read(lst_cheltuieli, 106) is None
    assert read(lst_cheltuieli, 107) is not None

    # 16 redo nu face nimic, deoarece ultima operatie nu este un redo
    if len(redo_list) > 0:
        lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 2
    assert read(lst_cheltuieli, 104) is not None
    assert read(lst_cheltuieli, 105) is None
    assert read(lst_cheltuieli, 106) is None
    assert read(lst_cheltuieli, 107) is not None

    # 17 undo anuleaza adaugarea lui o4
    if len(undo_list) > 0:
        lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 1
    assert read(lst_cheltuieli, 104) is not None
    assert read(lst_cheltuieli, 105) is None
    assert read(lst_cheltuieli, 106) is None
    assert read(lst_cheltuieli, 107) is None

    # 18 undo anuleaza stergerea lui o1 - practic se continua sirul de undo de la 14
    if len(undo_list) > 0:
        lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 0
    assert read(lst_cheltuieli, 104) is None
    assert read(lst_cheltuieli, 105) is None
    assert read(lst_cheltuieli, 106) is None
    assert read(lst_cheltuieli, 107) is None

    # 19 se anuleaza ultimele 2 undo-uri
    if len(redo_list) > 0:
        lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    if len(redo_list) > 0:
        lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 2
    assert read(lst_cheltuieli, 104) is not None
    assert read(lst_cheltuieli, 105) is None
    assert read(lst_cheltuieli, 106) is None
    assert read(lst_cheltuieli, 107) is not None

    # 20 redo nu face nimic
    if len(redo_list) > 0:
        lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 2
    assert read(lst_cheltuieli, 104) is not None
    assert read(lst_cheltuieli, 105) is None
    assert read(lst_cheltuieli, 106) is None
    assert read(lst_cheltuieli, 107) is not None

    # test_undo_redo - stergerea tuturor cheltuielilor pentru un apartament dat
    lst_cheltuieli = []
    lst_cheltuieli = create(lst_cheltuieli, 103, 3, 800, datetime.date(2020, 9, 11), 'intretinere', undo_list, redo_list)
    lst_cheltuieli = create(lst_cheltuieli, 104, 4, 111, datetime.date(2020, 9, 23), 'alte cheltuieli', undo_list, redo_list)
    lst_cheltuieli = create(lst_cheltuieli, 105, 5, 22, datetime.date(2021, 10, 7), 'alte cheltuieli', undo_list, redo_list)
    lst_cheltuieli = create(lst_cheltuieli, 106, 6, 247, datetime.date(2021, 8, 12), 'intretinere', undo_list, redo_list)

    nr_apartament = 3
    lst_cheltuieli = delete_all_costs_for_apartement(lst_cheltuieli,nr_apartament, undo_list, redo_list)
    assert len(lst_cheltuieli) == 3
    assert read_by_nr_apartament(lst_cheltuieli, 3) is None
    assert read_by_nr_apartament(lst_cheltuieli, 4) is not None
    assert read_by_nr_apartament(lst_cheltuieli, 5) is not None

    if len(undo_list) > 0:
        lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)

    assert len(lst_cheltuieli) == 4
    assert read_by_nr_apartament(lst_cheltuieli, 3) is not None
    assert read_by_nr_apartament(lst_cheltuieli, 4) is not None
    assert read_by_nr_apartament(lst_cheltuieli, 5) is not None

    if len(redo_list) > 0:
        lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 3
    assert read_by_nr_apartament(lst_cheltuieli, 3) is None
    assert read_by_nr_apartament(lst_cheltuieli, 4) is not None
    assert read_by_nr_apartament(lst_cheltuieli, 5) is not None

    # test_undo_redo - adunarea unei valori la toate cheltuielile dintr-o data citita
    lst_cheltuieli = []
    lst_cheltuieli = create(lst_cheltuieli, 103, 3, 800,
                     datetime.date(2020, 9, 11), 'intretinere',
                     undo_list, redo_list)
    lst_cheltuieli = create(lst_cheltuieli, 104, 4, 111,
                     datetime.date(2020, 9, 23), 'alte cheltuieli',
                     undo_list, redo_list)
    lst_cheltuieli = create(lst_cheltuieli, 105, 5, 22,
                     datetime.date(2021, 10, 7), 'alte cheltuieli',
                     undo_list, redo_list)
    lst_cheltuieli = create(lst_cheltuieli, 106, 6, 247,
                     datetime.date(2021, 8, 12), 'intretinere',
                     undo_list, redo_list)


    data = datetime.date(2020, 9, 11)
    valaore = 100
    lst_cheltuieli = add_sum_to_all_expense_by_date(lst_cheltuieli,data, valaore, undo_list, redo_list)

    assert get_suma(read(lst_cheltuieli, 103)) == 900
    assert get_suma(read(lst_cheltuieli, 104)) == 111
    assert get_suma(read(lst_cheltuieli, 105)) == 22

    lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert get_suma(read(lst_cheltuieli, 103)) == 800
    assert get_suma(read(lst_cheltuieli, 104)) == 111
    assert get_suma(read(lst_cheltuieli, 105)) == 22

    lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    assert get_suma(read(lst_cheltuieli, 103)) == 900
    assert get_suma(read(lst_cheltuieli, 104)) == 111
    assert get_suma(read(lst_cheltuieli, 105)) == 22
