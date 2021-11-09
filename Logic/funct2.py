from Domain.cheltuiala import get_data, creeaza_cheltuiala, get_id_cheltuiala, get_nr_apartament, get_suma, get_tipul


def add_sum_to_all_expense_by_date(lst_cheltuieli, data, valoare):
    """
    Aduna o valoare la toate cheltuielile dintr-o data ctita.
    :param lst_cheltuieli: Lista de cheltuieli.
    :param data: Data citita.
    :param valoare: Valoarea ce trebuie adaugata.
    :return: Lista modificata.
    """
    if valoare < 0:
        raise ValueError('Valoarea data trebuie sa fie un numar pozitiv')
    new_lst = []
    for cheltuiala in lst_cheltuieli:
        if get_data(cheltuiala) == data:
            cheltuiala_noua = creeaza_cheltuiala(
                get_id_cheltuiala(cheltuiala),
                get_nr_apartament(cheltuiala),
                get_suma(cheltuiala) + valoare,
                get_data(cheltuiala),
                get_tipul(cheltuiala)
            )
            new_lst.append(cheltuiala_noua)
        else:
            new_lst.append(cheltuiala)
    return new_lst