def do_undo(undo_list: list, redo_list: list, current_list: list):
    """
    Returneaza lista in urma apelarii unui Undo
    :param undo_list: Lista de liste de cheltuieli, modificata in urma apelarii fiecarei functionalitati
    :param redo_list: Lista de liste, modificata in urma apelarii fiecarei Undo, sau devine lista vida cand apelam o alta functionalitate
    :param current_list: Lista curenta de cheltuieli
    :return: Lista noua dupa apelarea Undo-ului
    """
    if undo_list:
        redo_list.append(current_list)
        return undo_list.pop()
    return None


def do_redo(undo_list: list, redo_list: list, current_list: list):
    """
    Returneaza lista in urma apelarii unui Redo
    :param undo_list: Lista de liste de cheltuieli, modificata in urma apelarii fiecarei functionalitati
    :param redo_list: Lista de liste, modificata in urma apelarii fiecarei Undo, sau devine lista vida cand apelam o alta functionalitate
    :param current_list: Lista curenta de cheltuieli
    :return: Lista noua dupa apelarea Redo-ului
    """
    if redo_list:
        top_redo = redo_list.pop()
        undo_list.append(current_list)
        return top_redo
    return None
