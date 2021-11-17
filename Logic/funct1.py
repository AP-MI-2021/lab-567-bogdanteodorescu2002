from Domain.cheltuiala import get_nr_apartament
from Logic.CRUD import read_by_nr_apartament


def delete_all_costs_for_apartement(lst_cheltuieli, nr_apartament, undo_list, redo_list):
    """
    Sterge toate cheltuielile pentru un apartament dat.
    :param lst_cheltuieli:  lista de cheltuieli.
    :param nr_apartament: Nr-ul apartamentului.
    :return: Lista in care cheltuielile partamentului dat s-au sters.
    """
    if read_by_nr_apartament(lst_cheltuieli, nr_apartament) is None:
        raise ValueError('Numarul apartamentului nu exista! ')
    new_list = []
    for cheltuiala in lst_cheltuieli:
        if get_nr_apartament(cheltuiala) != nr_apartament:
            new_list.append(cheltuiala)
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    return new_list
